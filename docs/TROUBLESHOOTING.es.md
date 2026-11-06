**Español** | [English](TROUBLESHOOTING.md)

# Problemas habituales

Empieza por la [guía de instalación](INSTALL.es.md) e identifica el paso que ha fallado. Home se ha usado con éxito en una Samsung de 2020; los menús y las funciones disponibles pueden variar en otros modelos y versiones de firmware.

| Síntoma | Comprobar |
| --- | --- |
| `tizen` o `sdb` no encontrado | Instalación oficial y PATH. Reinicia terminal tras cambiarlo; comprueba las versiones locales. |
| No conecta / offline | TV encendida, misma red, sin aislamiento Wi-Fi/VPN; IP del ordenador correcta en Developer Mode, reinicio y destino correcto en `sdb devices`. Revisa firewall local sin exponer puertos a Internet. |
| No aparece 12345 | Prueba Apps y, si existe, App Settings; usa teclado numérico del mando. Consulta documentación del modelo. |
| Error de firma o instalación | Perfil Samsung TV, distribuidor para el DUID correcto, fechas y permiso de instalación del dispositivo. Consulta el mensaje completo localmente. No publiques certificados ni logs sin sanear. |
| No puede actualizar Home | Certificado de autor distinto al anterior. Conserva backup; puede requerir desinstalación de la app antes de reinstalar. |
| Falla la desinstalación | Prueba **Eliminar** desde Apps. Comprueba que el comando usa el serial exacto de `sdb devices`. |
| El preparador rechaza una imagen o un enlace simbólico | Usa las imágenes originales y directorios reales. Retira archivos ajenos de `launcher/logos` y `launcher/glow`; guarda los archivos personales fuera de esas carpetas. Sustituye los enlaces simbólicos por archivos normales del proyecto. |
| Apps ausentes | Revisa visibilidad y nombres, o prueba el listado opcional `panel_apps.py`. Para recuperar la detección automática, pon `PANEL_APPS` en `[]` dentro de `launcher/apps.js` y vuelve a preparar, firmar e instalar. |
| Tiempo ausente | Por defecto está desactivado. Configura una ciudad y sus coordenadas en `launcher/config.js`, vuelve a preparar, firmar e instalar, y revisa conexión, reloj y disponibilidad de Open-Meteo. |
| HDMI o ajustes no responden | API o aplicación del sistema no disponible en ese firmware. Usa el menú normal de Samsung. |
| Error en `minisdb.py` | Es experimental. Usa SDB/Tizen Studio oficiales; no supongas que todos los firmware aceptan comandos `vd_*`. |

Si reportas un fallo, indica modelo, versión de Tizen, paso y mensaje saneado. Oculta IP, serial, DUID, usuario/rutas, hostname, claves y metadatos de certificados. No adjuntes tu `.wgt` personalizado.

Fuentes: [Samsung TV Device](https://developer.samsung.com/smarttv/develop/getting-started/using-sdk/tv-device.html) y [certificados Samsung](https://developer.samsung.com/smarttv/develop/getting-started/setting-up-sdk/creating-certificates.html).
