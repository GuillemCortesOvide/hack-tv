"""Lista opcional del panel usando el cliente experimental; destino explícito."""
import argparse
import ipaddress
import json
from pathlib import Path
import re
import minisdb


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--tv', required=True)
    args = parser.parse_args()
    minisdb.TV = (str(ipaddress.ip_address(args.tv)), 26101)
    conn = minisdb.Conn()
    try:
        text = conn.shell('0 vd_applist')
    finally:
        conn.s.close()
    apps = []
    for block in text.split('app_id   ')[1:]:
        fields = dict(re.findall(r'-{5,}([A-Za-z_]+)\s*=(.*?)-{5,}', '-----app_id   ' + block))
        fields = {k: v.strip() for k, v in fields.items()}
        if fields.get('is_hidden') == '1' or not fields.get('app_tizen_id'):
            continue
        apps.append({'id': fields['app_tizen_id'], 'name': fields.get('app_title', '')})
    if not apps:
        raise SystemExit('No hay apps válidas; se conserva apps.js. Usa el listado dinámico de Tizen.')
    output = Path(__file__).resolve().parent.parent / 'launcher/apps.js'
    output.write_text('var PANEL_APPS = ' + json.dumps(apps, ensure_ascii=True) + ';\n')
    print('Lista local actualizada. No publiques tu inventario personal de apps.')


if __name__ == '__main__':
    main()
