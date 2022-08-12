# Save the Dock preferences
defaults export com.apple.dock "$1/dock.plist"

# Save the Theme preferences (dark or light)
defaults read -g AppleInterfaceStyle > "$1/AppleInterfaceStyle.txt" || rm "$1/AppleInterfaceStyle.txt"