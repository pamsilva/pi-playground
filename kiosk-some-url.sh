#!/usr/bin/env bash

export DISPLAY=":0"

function display-up {
    echo Bringing display and Xserver up
    /opt/vc/bin/tvservice -p
    sleep 3
    /etc/init.d/lxdm start
    sleep 3
}

function display-down {
    echo Bringing display and Xserver down

    /etc/init.d/lxdm stop
    sleep 3

    /opt/vc/bin/tvservice -o
    sleep 3
}

function chrome-kiosk {
    chromium-browser --noerrdialogs --kiosk $1 --incognito --disable-translate --no-sandbox
}
