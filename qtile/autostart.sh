#!/bin/sh
picom --daemon
nitrogen --restore &
clipton watcher &
/usr/lib/xfce-polkit/xfce-polkit &
