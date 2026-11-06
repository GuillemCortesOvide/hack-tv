**Español** | [English](LIMITATIONS.md)

# Limitaciones

- Home se abre como una aplicación web de Tizen. No se convierte en el inicio predeterminado ni sustituye Smart Hub, las apps de fábrica o las funciones del firmware.
- El autor ha utilizado Home en una Samsung de 2020 con Tizen 5.5. El manifiesto de la app requiere Tizen 5.5; otros modelos y versiones no están verificados.
- Este proyecto utiliza SDB, la herramienta de desarrollo de Samsung para Tizen. No utiliza ADB, y conectarse mediante SDB no proporciona acceso root.
- Las fuentes HDMI, los ajustes, la visibilidad de las apps instaladas y su apertura dependen del firmware y los permisos de la TV. Las fuentes solo se muestran si la API de la TV las comunica; abrir una fuente puede fallar.
- La navegación y el rendimiento deben comprobarse en la TV. Un navegador de escritorio no reproduce las API ni el rendimiento del televisor.
- El tiempo es opcional y permanece desactivado hasta que configures una ubicación. Necesita acceso a Internet y envía las coordenadas de la ubicación configurada a Open-Meteo. Los servicios externos pueden fallar, limitar peticiones o cambiar sus condiciones.
- TizenBrew y Pi-hole son herramientas independientes que se instalan y administran por separado. Home no elimina anuncios dentro de los servicios de streaming ni anonimiza la TV.
- La instalación y el funcionamiento dependen del SDK de Samsung, los certificados, los permisos de la TV y el firmware. Comprueba de nuevo la compatibilidad después de actualizar el firmware.
