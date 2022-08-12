# Delete the current Dock preferences, then re-import the stored Dock preferences
defaults delete com.apple.dock
defaults import com.apple.dock "$1/dock.plist"
# Restart the dock so the changes become effective
killall Dock

# Load the Theme preferences (dark or light)
# Check if we have a file called "AppleInterfaceStyle.txt"- if yes, use dark mode
if [[ -f "$1/AppleInterfaceStyle.txt" ]]
then
	osascript -e 'tell app "System Events" to tell appearance preferences to set dark mode to true'
else
	osascript -e 'tell app "System Events" to tell appearance preferences to set dark mode to false'
fi