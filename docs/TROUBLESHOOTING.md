**English** | [Español](TROUBLESHOOTING.es.md)

# Common issues

Start with the step-by-step [installation guide](INSTALL.md) and identify which step failed. Home has been used successfully on a 2020 Samsung TV; menus and supported features can differ on other models and firmware versions.

| Symptom | Check |
| --- | --- |
| `tizen` or `sdb` not found | Official install and PATH. Restart your terminal after changing it; check the installed versions. |
| Won't connect / shows offline | TV is on, same network, no Wi-Fi/VPN client isolation; correct computer IP set in Developer Mode, restart done, and the right target in `sdb devices`. Check your local firewall without exposing ports to the internet. |
| Can't find 12345 | Try Apps, and App Settings if it exists; use the remote's numeric keypad. Check your model's documentation. |
| Signing or installation error | Samsung TV profile, distributor certificate matching the correct DUID, valid dates, and install permission enabled on the device. Check the full message locally. Don't post certificates or logs without sanitizing them. |
| Can't update Home | Author certificate differs from the previous one. Keep a backup; you may need to uninstall the app before reinstalling. |
| Uninstalling fails | Try **Remove** from the TV Apps menu. Confirm that the command uses the exact serial from `sdb devices`. |
| Asset or symbolic link rejected by the builder | Use the original asset files and real directories. Remove unrelated files from `launcher/logos` and `launcher/glow`; keep personal files outside those folders. Replace symbolic links with regular project files. |
| Apps missing from the panel | Check visibility and names, or try the optional `panel_apps.py` listing. To restore automatic discovery, set `PANEL_APPS` to `[]` in `launcher/apps.js`, then rebuild, sign and reinstall. |
| Weather not showing | It's disabled by default. Set a city and coordinates in `launcher/config.js`, then rebuild, sign and reinstall. Check your connection, the clock, and Open-Meteo's availability. |
| HDMI or settings don't respond | That API or system app isn't available on that firmware. Use Samsung's regular menu instead. |
| Error in `minisdb.py` | It's experimental. Use the official SDB/Tizen Studio tools instead; don't assume every firmware accepts `vd_*` commands. |

If you report a bug, include your model, Tizen version, the step you were on, and a sanitized message. Hide IP addresses, serial numbers, DUID, usernames/paths, hostname, keys, and certificate metadata. Don't attach your personalized `.wgt` file.

Sources: [Samsung TV Device](https://developer.samsung.com/smarttv/develop/getting-started/using-sdk/tv-device.html) and [Samsung certificates](https://developer.samsung.com/smarttv/develop/getting-started/setting-up-sdk/creating-certificates.html).
