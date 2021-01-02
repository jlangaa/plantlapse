# take timelapse photos of plants... like a nerd
import time
import sys
import os
import Adafruit_DHT
from datetime import datetime
import picamera as pc

OUT_DIR = sys.argv[1]
OUTFILENAME = 'hum_temp_log.tsv'
OUTFILE = os.path.join(OUT_DIR,OUTFILENAME)
DHT_PIN = 23

def dateprint(msg):
    d = datetime.now().strftime("%a %d %b %H:%M:%S EST %Y")
    print("{}: {}".format(d, msg))

dateprint("START")
dateprint("Output Directory: {}".format(OuT_DIR))
dateprint("Log file name: {}".format(OUTFILENAME))
dateprint("DHT PIN: {}".format(DHT_PIN))

try:
    os.mkdir(OUT_DIR)
except FileExistsError:
    dateprint("Output directory exists")

if not os.path.exists(OUTFILE):
    dateprint("Creating output file")
    with open(OUTFILE, 'w') as f:
        f.writelines('IDX\tDate\tTemp (C)\tHumidity\r\n')

dateprint("Reading sensor data")
sensor = Adafruit_DHT.AM2302
hum, temp = Adafruit_DHT.read_retry(sensor, DHT_PIN)
dateprint("success")
dateprint("writing sensor data to file")

with open(OUTFILE, 'a') as f:
    f.seek(0,0)
    n_lines = len(f.readlines())
    f.writelines('{}\t{}\t{}\t{}\r\n'.format(n_lines, datetime.now(), temp, hum))
dateprint("success")
dateprint("Capturing image")

cam = pc.PiCamera(resolution = (3280, 2464))
cam.iso = 200
cam.exposure_mode = 'off'
cam.awb_mode = 'off'
cam.awb_gains = (1.4, 1.3)
cam.shutter_speed = 3000

cam.start_preview()
time.sleep(2)

img_name = "img_{:04d}.jpg".format(n_lines)
cam.capture()
dateprint("success")

