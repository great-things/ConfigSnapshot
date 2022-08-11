# Restore the desktop settings - does not include applet settings
dconf load / < "$1/dconf-dump.txt"

# Restore the applet settings
cp -r $1/DOT_CINNAMON/* ~/.cinnamon
