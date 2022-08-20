This folder contains everything that has to do with the GUI.

The GUI is very basic right now - it has a list, as well as a text field to type a name, and an "add" button.
To make a snapshot of your current desktop configuration, type a name into the text field and hit the button.
To load a snapshot, double-click on an item in the list.

Currently, there is a bug which causes a little star to be displayed in the list when it should be empty. You can just ignore that for now (or maybe fix it, if you want to).

## logic
This is an executable shell script which is the logic portion of the UI.
In that file, there is a comment which explains how to send and receive events from the actual GUI.

## ui.py
This is a python script that creates a GTK UI and connects it to the logic script. Usage: `python3 ui.py logic`.

## run.sh
This script can be used to start the GUI. Just run it from anywhere using `bash`.

## addToLinuxMenu.sh
This script is used to create a .desktop file for this app and add it to the menu.
Known bug: the app might only show up in the menu after logging out and back in.

## linuxDesktopFileTemplate.txt
This contains a template for a .desktop file, which is used by `addToLinuxMenu.sh`.
The template file contains things that do not change on a per-user basis, like the app version, title and description.
It does not contain anything about what the desktop file should execute when run, because that is user-specific (it depends on where the app is located).
