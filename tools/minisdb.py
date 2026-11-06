"""Cliente SDB mínimo (protocolo tipo ADB) para la TV en modo desarrollador.

Uso:
  python minisdb.py shell "0 vd_applist"
  python minisdb.py install paquete.wgt <packageId>
  python minisdb.py uninstall <packageId>
"""
import os, socket, struct, sys

TV = None  # Se requiere un destino explícito; nunca se detecta ni conecta al importar.
CMD = {k: struct.unpack("<I", k.encode())[0] for k in ("CNXN", "OPEN", "OKAY", "WRTE", "CLSE")}
NAME = {v: k for k, v in CMD.items()}
REMOTE_TMP = "/home/owner/share/tmp/sdk_tools/package.wgt"


def pkt(cmd, a0, a1, data=b""):
    c = CMD[cmd]
    return struct.pack("<6I", c, a0, a1, len(data), sum(data) & 0xFFFFFFFF, c ^ 0xFFFFFFFF) + data


def recv_exact(s, n):
    buf = b""
    while len(buf) < n:
        chunk = s.recv(n - len(buf))
        if not chunk:
            raise EOFError
        buf += chunk
    return buf


def read(s):
    c, a0, a1, n, checksum, magic = struct.unpack("<6I", recv_exact(s, 24))
    if n > 1024 * 1024 or magic != (c ^ 0xFFFFFFFF):
        raise ValueError("Cabecera SDB inválida")
    data = recv_exact(s, n)
    if (sum(data) & 0xFFFFFFFF) != checksum:
        raise ValueError("Checksum SDB inválido")
    return NAME.get(c, hex(c)), a0, a1, data


class Conn:
    def __init__(self, timeout=60):
        if TV is None:
            raise ValueError("Indica TV_IP con la dirección de tu TV")
        self.s = socket.create_connection(TV, timeout=timeout)
        self.s.sendall(pkt("CNXN", 0x02000000, 256 * 1024, b"host::\0"))
        cmd, *_, data = read(self.s)
        if cmd != "CNXN":
            raise SystemExit(f"Respuesta inesperada: {cmd} {data[:200]}")

    def open(self, service, local=1):
        self.s.sendall(pkt("OPEN", local, 0, service.encode() + b"\0"))
        while True:
            cmd, a0, a1, data = read(self.s)
            if cmd == "OKAY":
                return a0  # id remoto
            if cmd == "CLSE":
                raise SystemExit(f"La TV rechazó {service}")

    def write(self, local, remote, data):
        self.s.sendall(pkt("WRTE", local, remote, data))
        while True:  # esperar el OKAY de ese paquete
            cmd, a0, a1, d = read(self.s)
            if cmd == "OKAY":
                return
            if cmd == "WRTE":
                self.s.sendall(pkt("OKAY", local, a0))
                self.pending = getattr(self, "pending", b"") + d
            if cmd == "CLSE":
                raise EOFError

    def shell(self, command):
        remote = self.open(f"shell:{command}", local=2)
        out = b""
        try:
            while True:
                cmd, a0, a1, data = read(self.s)
                if cmd == "WRTE":
                    out += data
                    self.s.sendall(pkt("OKAY", 2, a0))
                elif cmd == "CLSE":
                    break
        except (socket.timeout, EOFError):
            pass
        return out.decode(errors="replace")

    def push(self, data, path):
        remote = self.open("sync:", local=3)
        spec = f"{path},33188".encode()
        self.write(3, remote, b"SEND" + struct.pack("<I", len(spec)) + spec)
        for i in range(0, len(data), 32 * 1024):
            chunk = data[i:i + 32 * 1024]
            self.write(3, remote, b"DATA" + struct.pack("<I", len(chunk)) + chunk)
        self.write(3, remote, b"DONE" + struct.pack("<I", 0x15F2B865))
        reply = getattr(self, "pending", b"")
        while len(reply) < 8:
            cmd, a0, a1, d = read(self.s)
            if cmd == "WRTE":
                reply += d
                self.s.sendall(pkt("OKAY", 3, a0))
        self.write(3, remote, b"QUIT" + struct.pack("<I", 0))
        if not reply.startswith(b"OKAY"):
            raise SystemExit(f"Fallo al subir el archivo: {reply[:200]!r}")


class Sync:
    """Canal sync: listar y descargar archivos."""

    def __init__(self, conn):
        self.c, self.buf = conn, b""
        self.remote = conn.open("sync:", local=4)

    def _send(self, tag, payload):
        self.c.s.sendall(pkt("WRTE", 4, self.remote, tag + struct.pack("<I", len(payload)) + payload))

    def _need(self, n):
        while len(self.buf) < n:
            cmd, a0, a1, d = read(self.c.s)
            if cmd == "WRTE":
                self.buf += d
                self.c.s.sendall(pkt("OKAY", 4, a0))
            elif cmd == "CLSE":
                raise EOFError
        out, self.buf = self.buf[:n], self.buf[n:]
        return out

    def ls(self, path):
        self._send(b"LIST", path.encode())
        items = []
        while True:
            tag = self._need(4)
            if tag == b"DONE":
                self._need(16)
                return items
            mode, size, mtime, namelen = struct.unpack("<4I", self._need(16))
            items.append((self._need(namelen).decode(errors="replace"), size, mode))

    def pull(self, path):
        self._send(b"RECV", path.encode())
        data = b""
        while True:
            tag, n = self._need(4), struct.unpack("<I", self._need(4))[0]
            if tag == b"DATA":
                data += self._need(n)
            elif tag == b"DONE":
                return data
            else:
                raise IOError(self._need(n).decode(errors="replace"))


if __name__ == "__main__":
    import ipaddress
    TV = (str(ipaddress.ip_address(os.environ["TV_IP"])), 26101)
    op = sys.argv[1] if len(sys.argv) > 1 else "shell"
    if op == "shell":
        print(Conn().shell(" ".join(sys.argv[2:]) or "0 vd_applist"))
    elif op == "install":
        wgt, pkg_id = sys.argv[2], sys.argv[3]
        Conn().push(open(wgt, "rb").read(), REMOTE_TMP)
        print(Conn().shell(f"0 vd_appinstall {pkg_id} {REMOTE_TMP}"))
    elif op == "uninstall":
        print(Conn().shell(f"0 vd_appuninstall {sys.argv[2]}"))
