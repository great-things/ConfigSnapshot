# Read parameters
savedConfig="$1"

# Save the panel settings (how many bars, what icons are in them)
# TODO: This requires xfce4-panel-profiles; make sure this exists
xfce4-panel-profiles save "$savedConfig/panel-profile"

# Save the current theme
xfconf-query -c xsettings -p /Net/ThemeName > "$savedConfig/xsettings-theme.txt"
xfconf-query -c xsettings -p /Net/IconThemeName > "$savedConfig/xsettings-icon-theme.txt"
xfconf-query -c xfwm4 -p /general/theme > "$savedConfig/xfwm4-theme.txt"
