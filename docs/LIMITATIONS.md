**English** | [Español](LIMITATIONS.es.md)

# Limitations

- Home opens as a Tizen web app. It does not become the default launcher or replace Smart Hub, factory apps, or firmware features.
- The author has used Home on a 2020 Samsung TV running Tizen 5.5. The app manifest requires Tizen 5.5; other models and versions have not been verified.
- This project uses SDB, Samsung's development tool for Tizen. It does not use ADB, and connecting through SDB does not provide root access.
- HDMI sources, settings, installed app visibility, and app launching depend on the TV's firmware and permissions. Sources are shown only when the TV's API reports them; opening a source can fail.
- Navigation and performance need to be checked on the TV. A desktop browser does not reproduce the TV's APIs or performance.
- Weather is optional and disabled until you configure a location. It requires internet access and sends the configured location's coordinates to Open-Meteo. External services can fail, limit requests, or change their terms.
- TizenBrew and Pi-hole are independent tools, installed and managed separately. Home does not remove ads inside streaming services or anonymize the TV.
- Installation and operation depend on Samsung's SDK, certificates, TV permissions, and firmware. Check compatibility again after firmware updates.
