# Figures out which desktop environment is in use and writes that info to a file
# This only works on Linux, and it only has an effect when a supported desktop environment is detected
mkdir -p $HOME/.greatthings/files/ConfigSnapshot

case "$XDG_CURRENT_DESKTOP" in
    *XFCE*) echo xfce4 > $HOME/.greatthings/files/ConfigSnapshot/backend.txt;;
    *Cinnamon*) echo cinnamon > $HOME/.greatthings/files/ConfigSnapshot/backend.txt;;
esac
