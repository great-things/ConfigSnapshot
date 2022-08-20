# Performs a given action (first parameter) with a snapshot (second parameter).
# This requires a backend configuration in $HOME/.greatthings/files/ConfigSnapshot/backend.txt
# For more info on how to create the backend configuration, look at the README file in this folder.

# Read parameters
action="$1"
configName="$2"

# Where are all the other scripts? This is needed to load the backend name and to run the appropriate script files
scriptsFolder="$(dirname $0)"

# Create a folder for the configuration
# TODO: If the configuration already exists, there should maybe be some kind of warning or error
configurationFolder="$HOME/.greatthings/files/ConfigSnapshot/snapshots/$configName"
mkdir -p "$configurationFolder"

# Figure out which desktop environment we are using (backend.txt)
environmentName="$(cat $HOME/.greatthings/files/ConfigSnapshot/backend.txt)"

# Run the appropriate "save.sh" script, with $scriptsFolder as the parameter so we know where to save things
bash "$scriptsFolder/backends/$environmentName/$action.sh" "$configurationFolder"
