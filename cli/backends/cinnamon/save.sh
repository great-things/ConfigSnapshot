# Store the desktop settings - does not include applet settings
dconf dump / > "$1/dconf-dump.txt"

# Store the applet settings
rm -rf "$1/DOT_CINNAMON"
cp -r ~/.cinnamon "$1/DOT_CINNAMON"
