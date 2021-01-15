# take timelapse photos of plants... like a nerd
import time
import sys
import os
from datetime import datetime
import picamera as pc

OUT_DIR = sys.argv[1]

def dateprint(msg):
    d = datetime.now().strftime("%a %-d %b %H:%M:%S EST %Y")
    print("{}: {}".format(d, msg))

dateprint("START")
dateprint("Output Directory: {}".format(OUT_DIR))

dateprint("Capturing image")

with pc.PiCamera(resolution = (3280, 2464)) as cam:
    cam.iso = 20
    cam.rotation = 270
    time.sleep(2)
    cam.exposure_mode = 'off'
    cam.awb_mode = 'off'
    cam.awb_gains = (1.2, 1.4)
    cam.shutter_speed = 8000

    cam.annotate_text = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    img_name = "img_test.jpg"
    #img_name = "test.jpg"
    cam.capture(os.path.join(OUT_DIR,img_name))
dateprint("success")

