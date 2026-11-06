[English](SECURITY.md) | **Español**

# Seguridad y privacidad

Estas notas explican qué datos usa Home, cómo funcionan las herramientas locales de instalación y cuáles son sus límites de seguridad conocidos.

## Datos y acceso a la red

Home lista y abre apps instaladas mediante APIs locales de Tizen. El inventario de apps permanece en el dispositivo o en tu configuración local.

El tiempo está desactivado por defecto. Si configuras una ciudad, Home consulta `https://api.open-meteo.com` con sus coordenadas. Open-Meteo recibe esas coordenadas y tu IP pública. Home no necesita una clave API ni envía el inventario de apps al servicio del tiempo.

El manifiesto actual permite orígenes externos con `access origin="*"`. El launcher solo utiliza actualmente el servicio del tiempo y no define una política propia de seguridad de contenido (CSP). Restringir esta política queda como mejora futura.

## Configuración y paquetes

- Mantén privados `launcher/config.js` y `launcher/apps.js` si contienen ajustes personales o tu inventario de apps. Git los ignora, pero se incluyen en el paquete generado.
- Guarda certificados de firma, claves privadas, contraseñas y perfiles de certificados Tizen fuera del repositorio.
- Revisa el contenido de cualquier `.wgt` antes de compartirlo. Un paquete firmado también puede incluir metadatos del certificado del firmante.
- Si compartes una credencial por accidente, revócala o rótala en su proveedor; borrar el archivo por sí solo no basta.

El empaquetador usa un inventario fijo de imágenes y rechaza archivos inesperados en `launcher/logos` y `launcher/glow`. Comprueba las rutas de origen y destino antes de crear configuraciones o reemplazar un build, y rechaza enlaces simbólicos, incluidos los colgantes y los puntos de redirección de Windows. Prepara el paquete en una carpeta temporal privada.

Estas comprobaciones protegen frente a enlaces preexistentes. No aíslan el build de programas maliciosos que usen la misma cuenta y cambien directorios durante la ejecución.

## Conexión con tu TV

Utiliza el modo desarrollador y SDB solo con tu propia TV y en una red local de confianza. No expongas la conexión de desarrollo mediante el router. Desactiva el modo desarrollador cuando ya no lo necesites.

El cliente Python opcional de SDB es experimental. Su conexión no autentica criptográficamente al servidor y las respuestas entrantes todavía no tienen un límite total de tamaño. Usa las herramientas oficiales de Tizen para firmar e instalar; el cliente opcional no es necesario para instalar Home.

El instalador exige indicar un destino para instalar o desinstalar. La TV valida los paquetes firmados; comprobar localmente que existen archivos de firma no sustituye esa validación.

## Comprobaciones y compatibilidad

Ejecuta las pruebas locales del instalador con:

```sh
python3 -B -m unittest discover -s tests -v
```

Las pruebas cubren archivos inesperados, enlaces simbólicos, contenido del paquete y comandos simulados de firma e instalación. No validan certificados reales ni el firmware de la TV.

El creador confirma que funciona en una Samsung de 2020. Consulta las [limitaciones](LIMITATIONS.es.md) y la [instalación](INSTALL.es.md) para configurar tu dispositivo.

## Comunicar un problema de seguridad

Usa la pestaña Security del repositorio para comunicar una vulnerabilidad en privado si esa opción está disponible. Si no lo está, abre una incidencia solicitando un medio de contacto privado, sin incluir credenciales, certificados, identificadores de dispositivos ni un ataque funcional contra dispositivos ajenos.
