#!/bin/bash

# download all files to "Files/"R
wget -r -N -nd --no-parent -A *.jpg,*.tsv -P Files/ http://192.168.1.147/files/

# Create the gif

convert -resize 50% -monitor -delay 15 -loop 0 Files/img*.jpg timelapse.gif

# send it over to the Pi
scp timelapse.gif pi@192.168.1.147:~/plantlapse_data/
