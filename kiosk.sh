#!/bin/sh
xset -dpms     # disable DPMS (Energy Star) features.
xset s off     # disable screen saver
xset s noblank # don't blank the video device
firefox --display=:0 -kiosk -private-window /home/user/s3-image-viewer/index.html