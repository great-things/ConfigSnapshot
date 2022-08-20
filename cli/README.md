This folder contains terminal tools to store and restore snapshots of your desktop config.

Snapshots are stored in `~/.greatthings/files/ConfigSnapshot/snapshots`.

## action.sh
Performs an action using the given backend from "backend.txt" and a configuration name. Can be run from any folder.

## save.sh
This script is used to save a snapshot. Same as `action.sh save ...`

## load.sh
This script is used to save a snapshot. Same as `action.sh load ...`

## backends/
This folder contains the specific commands for each desktop environment to save and load its settings.

## backend.txt
This file has previously been located in this folder, but now it is in `$HOME/.greatthings/files/ConfigSnapshot/backend.txt`.

The "backend.txt" file is used to specify which desktop environment is in use, so the appropriate actions can be taken. That is needed since all the desktop environments save their settings in different places.

### How to create the backend configuration
To create the "backend.txt" file on Linux, run the `configureLinuxBackend.sh` script from anywhere. That will create a correct configuration, but only if your Desktop environment is supported and can be detected correctly.

On macOS, you can create the needed file using these two commands:
```
mkdir -p $HOME/.greatthings/files/ConfigSnapshot
echo mac > $HOME/.greatthings/files/ConfigSnapshot/backend.txt
```

This also works on Linux if you replace `mac` with the name of a supported backend (`cinnamon` or `xfce4`, for example).
