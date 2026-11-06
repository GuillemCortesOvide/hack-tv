**English** | [Español](README.es.md)

# Home for Samsung Tizen TV

A custom home screen app for Samsung Tizen TVs. Keep your favorite apps, TV inputs, clock, and optional weather together on one screen.

**Home opens as a regular app.** It does not replace Samsung Smart Hub or change what the remote's Home button opens.

## Features

- A dock for your favorite apps and a list of installed apps.
- Navigation with the TV remote.
- Shortcuts to TV inputs and settings, where supported by the firmware.
- A clock and optional weather from Open-Meteo.
- Local configuration, with no account or API key required by Home.

The current TV interface is in Spanish. Documentation is available in English and Spanish.

## Compatibility

The maintainer confirms that Home works on a 2020 Samsung TV. The reference model is Samsung UE55TU7125KXXC with Tizen 5.5, which is also the minimum version declared by the app.

Other models and Tizen versions have not been verified. Input switching, settings shortcuts, and app visibility can vary by firmware. This project is for Samsung Tizen; LG webOS and Android TV are not supported.

## Get started

You need Python 3.9 or newer to prepare the package:

```sh
git clone https://github.com/GuillemCortesOvide/hack-tv.git
cd hack-tv
python3 instalar.py
```

This creates local configuration files and `build/Home-unsigned.wgt`. **The package is unsigned and cannot be installed yet.** Preparation does not download dependencies or connect to your TV.

To sign and install it, you need Tizen Studio, the Samsung TV and Samsung Certificate extensions, a Samsung Developer account, and your own TV certificates.

Follow the [installation guide](docs/INSTALL.md) for the complete steps, including Developer Mode, certificates, configuration, and installation on your own TV.

## Documentation

- [Installation](docs/INSTALL.md)
- [Troubleshooting](docs/TROUBLESHOOTING.md)
- [Compatibility and limitations](docs/LIMITATIONS.md)
- [Security and privacy](docs/SECURITY.md)
- [Credits and asset licensing](docs/CREDITS.md)

## Privacy and security

Weather is off by default. If you configure a city, its coordinates are sent to Open-Meteo over HTTPS; the service also receives your public IP. The launcher does not send your installed app inventory to that service.

Local configuration and app inventory files are ignored by Git but included in your own package. Keep certificates and signing keys outside the repository, and review a package before sharing it. See the [security notes](docs/SECURITY.md).

## Credits and license

Built with help from Claude Code and Codex, inspired by exploring TV customization. [Free My TV](https://github.com/simbasjungles/free-my-tv) was a reference. [TizenBrew](https://github.com/reisxd/TizenBrew) is an independent project; Home can show a shortcut when it is installed and detected.

The project code is licensed under [MIT](LICENSE). Third-party logos and bundled images have separate rights; their individual redistribution licenses are not documented here. See [credits](docs/CREDITS.md) before redistributing those assets.
