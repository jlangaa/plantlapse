#!/bin/bash

# Wrapper for timelapse.py to be used with cron

t=$(date +%H:%M)

python3 ~/Projects/plantlapse/lightswitch.py on

python3 ~/Projects/plantlapse/timelapse.py 23 ~/plantlapse

if [[ $t > 23:00 || $t < 8:00 ]]; then
	echo $(date)": Turning off the light"
	python3 ~/Projects/plantlapse/lightswitch.py off	
	echo $(date)": Complete"
fi

echo $(date)": Converting images to GIF"
convert -delay 20 -resize 20% -loop 0 ~/plantlapse/img*.jpg ~/plantlapse/timelapse.gif
echo $(date)": Complete"

echo "================================================================================"
