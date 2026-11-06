**English** | [Español](SECURITY.es.md)

# Security and privacy

These notes describe Home's data use, local installation tools, and known security limits.

## Data and network access

Home lists and launches installed apps through local Tizen APIs. The app inventory stays on the device or in your local configuration.

Weather is disabled by default. If you configure a city, Home requests a forecast from `https://api.open-meteo.com` using its coordinates. Open-Meteo receives those coordinates and your public IP. Home does not require an API key or send the app inventory to the weather service.

The current manifest permits external network origins with `access origin="*"`. The launcher currently uses only the weather endpoint, and no custom Content Security Policy is configured. A narrower policy remains a future improvement.

## Configuration and packages

- Keep `launcher/config.js` and `launcher/apps.js` private if they contain personal settings or your app inventory. Git ignores them, but your built package includes them.
- Store signing certificates, private keys, passwords, and Tizen certificate profiles outside the repository.
- Review the contents of any `.wgt` before sharing it. A signed package may also include signer certificate metadata.
- If you accidentally share a credential, revoke or rotate it with its provider; removing the file alone is insufficient.

The packager uses a fixed asset inventory and rejects unexpected files in `launcher/logos` and `launcher/glow`. It checks source and destination paths before creating configurations or replacing a build, and rejects symbolic links, including dangling links and Windows reparse points. It prepares the package in a private temporary directory.

These checks protect against pre-existing links. They do not isolate the build from malicious software running under the same account and changing directories during execution.

## Connecting to your TV

Use Developer Mode and SDB only with your own TV on a trusted local network. Do not expose the development connection through your router. Turn Developer Mode off when you no longer need it.

The optional Python SDB client is experimental. Its connection does not authenticate the server cryptographically, and incoming responses do not yet have an overall size limit. Use the official Tizen tools for signing and installation; the optional client is not required to install Home.

The installer requires an explicit target for installation or removal. The TV validates signed packages; checking for signature files locally does not replace that validation.

## Checks and compatibility

Run the local installer regression tests with:

```sh
python3 -B -m unittest discover -s tests -v
```

The tests cover unexpected packaged files, symbolic links, package contents, and simulated signing/install commands. They do not validate real certificates or TV firmware.

The maintainer confirms operation on a 2020 Samsung TV. See [limitations](LIMITATIONS.md) for the supported scope and [installation](INSTALL.md) to configure your own device.

## Reporting a security issue

Use the repository's Security tab to report a vulnerability privately if private reporting is available. Otherwise, open an issue asking for a private contact method, without including credentials, certificates, device identifiers, or a working exploit against someone else's device.
