# ConfigSnapshot - Store and reuse your desktop configuration
## What is this about?
People use their computers for a lot of things. They use them to do work, to be creative, to play games, to watch or produce movies, and much more.
Personally, I do not want the same environment for work and my free time. I may need an office suite and a mail app for work, but when I am done working, I do not wish to see the mail app - as that would remind me of work again.

If you are like that as well, this ConfigSnapshot app is for you. It allows you to take a snapshot of your current desktop configuration - your pinned apps and other status widgets, as well as your GUI theme, and potentially more in the future - and you can then switch to it later. With multiple saved configurations, you can then easily switch between modes.

Apparently an app like this does not exist, or I have been unable to find it - so I decided to make it.

## Notes and opportunities to help
Note: this is a very early version with a *very* unfinished UI. If you want to help me make it nicer, please do. I tried to document the main project structure somewhat well, so hopefully you can figure out what is going on.

Currently, the app only works on Linux with the XFCE desktop, or with Cinnamon. If you want to help me add support for another environment, please take a look at the `cli/backends` folder, where you can find the implementations for XFCE and Cinnamon - it should be possible to create another supported backend based on that.

## Installation
Currently, the app only works on Linux with the XFCE desktop, or with Cinnamon.

* Clone this repo and navigate into the cloned folder
* Make sure you have the following dependencies installed:
	* `python3`
	* `decoupled-connect` (https://github.com/great-things/decoupled-connect), which depends on `node` (https://nodejs.org/)
	* `xfce4-panel-profiles` (if you use XFCE) installed
* Run `bash ./cli/configureLinuxBackend.sh` to detect the desktop environment you are running
* Run `bash "$(pwd)/gui/addToLinuxMenu.sh"` if you want to add a shortcut to your menu. This shortcut is called "ConfigSnapshot"; it might only show up after you log out and back in.
* Either click on the menu shortcut, or run `bash ./gui/run.sh` to start the app
