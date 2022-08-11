This folder contains terminal tools to store and restore snapshots of your desktop config.

Snapshots are stored in `~/.greatthings/files/ConfigSnapshot/snapshots`.

## backend.txt
The "backend.txt" file is used to specify which desktop environment is in use, so the appropriate actions can be taken. That is needed since all the desktop environments save their settings in different places.

## action.sh
Performs an action using the given backend from "backend.txt" and a configuration name. Can be run from any folder.

## save.sh
This script is used to save a snapshot. Same as `action.sh save ...`

## load.sh
This script is used to save a snapshot. Same as `action.sh load ...`

## backends/
This folder contains the specific commands for each desktop environment to save and load its settings.
