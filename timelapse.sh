#!/bin/bash

# Wrapper for timelapse.py to be used with cron

t=$(date +%H%M)

python3 ~/Projects/plantlapse/lightswitch.py on

#python3 ~/Projects/plantlapse/plantlapse.py ~/plantlapse_data

if [[ $t -gt 2300 || $t -lt 800 ]]; then
	echo $(date)": Turning off the light"
	python3 ~/Projects/plantlapse/lightswitch.py off	
	echo $(date)": Complete"
fi

echo $(date)": Converting images to GIF"
#convert -delay 20 -resize 40% -loop 0 ~/plantlapse_data/img*.jpg ~/plantlapse_data/timelapse.gif
echo $(date)": Complete"

echo "================================================================================"
