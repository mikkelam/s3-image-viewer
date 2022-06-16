# s3-image-viewer

Simple utility to randomly shuffle the the newest images inserted into an S3 bucket (currently only jpeg is supported). 
# requirements
make sure to have aws credentials available. 

boto3 should be installed: `pip3 install -r requirements.txt`
# Usage

First, open `index.html` in your browser of choice.

To fetch the `N=5000` newest images.
```bash
python main.py -refresh --bucket my-bucket
```

then, to update update the displayed image
```bash
python main.py -show-random --bucket my-bucket
```

`index.html` continually refreshes `show.jpeg`, so we should now be able to see the newly fetched image.

# Kiosk mode on a raspberry pi 4
install x11 and kiosk display utilities
``` bash
sudo apt update &&
sudo apt-get install --no-install-recommends xserver-xorg x11-xserver-utils xinit  && 
sudo apt-get install matchbox-window-manager xautomation unclutter
```
add `[[ -z $DISPLAY && $XDG_VTNR -eq 1 ]]  && xinit /home/pi/s3-image-viewer/kiosk.sh -- vt$(fgconsole)` to your `~/.profile`. make sure the script path is correct.

An example crontab has been included, this one auto-updates the file list every 24hrs and updates the img every minute
