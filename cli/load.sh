# Run the appropriate "save.sh" script, with $scriptsFolder as the parameter so we know where to save things
bash "$(dirname $0)/action.sh" load "$1"
