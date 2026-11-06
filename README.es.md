[English](README.md) | **Español**

# Home para Samsung Tizen TV

Una pantalla de inicio personalizada para televisores Samsung Tizen. Reúne tus apps favoritas, las entradas de la TV, el reloj y el tiempo opcional en una sola pantalla.

**Home se abre como una aplicación normal.** No sustituye Samsung Smart Hub ni cambia lo que abre el botón Home del mando.

## Funciones

- Un dock de apps favoritas y una lista de apps instaladas.
- Navegación con el mando de la TV.
- Accesos a las entradas de la TV y los ajustes, cuando el firmware lo permite.
- Reloj y tiempo opcional de Open-Meteo.
- Configuración local, sin cuenta ni clave API para Home.

La interfaz actual de la TV está en español. La documentación está disponible en inglés y español.

## Compatibilidad

El creador confirma que Home funciona en su Samsung de 2020. El modelo de referencia es Samsung UE55TU7125KXXC con Tizen 5.5, que también es la versión mínima declarada por la app.

No se han verificado otros modelos o versiones de Tizen. El cambio de entradas, los accesos a ajustes y la visibilidad de apps pueden variar según el firmware. Este proyecto es para Samsung Tizen; no ofrece soporte para LG webOS ni Android TV.

## Empezar

Necesitas Python 3.9 o superior para preparar el paquete:

```sh
git clone https://github.com/GuillemCortesOvide/hack-tv.git
cd hack-tv
python3 instalar.py
```

Esto crea los archivos de configuración locales y `build/Home-unsigned.wgt`. **El paquete no está firmado y todavía no se puede instalar.** La preparación no descarga dependencias ni se conecta a tu TV.

Para firmarlo e instalarlo necesitas Tizen Studio, las extensiones Samsung TV y Samsung Certificate, una cuenta Samsung Developer y tus propios certificados para la TV.

Sigue la [guía de instalación](docs/INSTALL.es.md) para completar los pasos de modo desarrollador, certificados, configuración e instalación en tu propia TV.

## Documentación

- [Instalación](docs/INSTALL.es.md)
- [Problemas habituales](docs/TROUBLESHOOTING.es.md)
- [Compatibilidad y limitaciones](docs/LIMITATIONS.es.md)
- [Seguridad y privacidad](docs/SECURITY.es.md)
- [Créditos y licencias de imágenes](docs/CREDITS.es.md)

## Privacidad y seguridad

El tiempo está desactivado por defecto. Si configuras una ciudad, se envían sus coordenadas a Open-Meteo mediante HTTPS; el servicio también recibe tu IP pública. El launcher no envía tu inventario de apps a ese servicio.

Los archivos locales de configuración e inventario se ignoran en Git, pero se incluyen en tu paquete. Guarda los certificados y las claves de firma fuera del repositorio y revisa el paquete antes de compartirlo. Consulta las [notas de seguridad](docs/SECURITY.es.md).

## Créditos y licencia

Desarrollado con ayuda de Claude Code y Codex, a partir del interés por personalizar televisores. [Free My TV](https://github.com/simbasjungles/free-my-tv) fue una referencia. [TizenBrew](https://github.com/reisxd/TizenBrew) es un proyecto independiente; Home puede mostrar un acceso si está instalado y se detecta.

El código del proyecto tiene licencia [MIT](LICENSE). Los logos de terceros y las imágenes incluidas tienen derechos propios; sus licencias individuales de redistribución no están documentadas aquí. Consulta los [créditos](docs/CREDITS.es.md) antes de redistribuir esos assets.
