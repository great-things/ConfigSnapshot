# Creates a user-specific .desktop file for this app, so it can show up in the menu.

## Move the desktop file template to the correct location
mkdir -p $HOME/.greatthings/files/ConfigSnapshot
cp "$(dirname $0)/linuxDesktopFileTemplate.txt" "$HOME/.local/share/applications/app.desktop.ConfigSnapshot.desktop"

## Add some user-specific lines to the desktop file, so it has an executable
echo Exec=bash "$(dirname $0)/run.sh" >> "$HOME/.local/share/applications/app.desktop.ConfigSnapshot.desktop"

## Make the desktop file executable, otherwise it appears to be broken
chmod +x "$HOME/.local/share/applications/app.desktop.ConfigSnapshot.desktop"
