#!/usr/bin/bash
convert -delay 20 -resize 20% -loop 0 ~/plantlapse_data/img*.jpg ~/plantlapse_data/timelapse.gif
