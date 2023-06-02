from picamera2 import Picamera2
from time import sleep
import time
picam2 = Picamera2()
from datetime import datetime
from libcamera import controls
#import datetime

datet = datetime.now()

ts = datetime.timestamp(datett)

date_time = datetime.fromtimestamp(ts)

str_date_time = date_time.strftime("%d-%m-%Y_%H:%M:%S")

now = datetime.now()

path = "/home/here/the/name"


picam2.still_configuration.size = (2028, 1520)
picam2.options["quality"] = 95
picam2.set_controls({"AeEnable": False})    #True
picam2.set_controls({"AeExposureMode": controls.AeExposureModeEnum.Long})   #Normal, Short
picam2.set_controls({"ExposureTime": 15000})

number = 3
interval = 30

picam2.start()
picam2.set_controls({"ExposureTime": 15000})

metadata = picam2.capture_metadata()
controls = {c: metadata[c] for c in ["ExposureTime", "AnalogueGain", "ColourGains"]}
print(controls)

picam2.set_controls(controls)

for x in range(number):   #0, 1, 2
    print(x)
    now = datetime.now()
    print(now)
    #sleep(3)    
    picam2.capture_file(path + str_date_time + '_number_' + str(x) + '.jpg')
    request = picam2.capture_request()
    metadata = request.get_metadata()
    request.release()
    print(metadata["ExposureTime"], metadata["ColourGains"], metadata["AnalogueGain"], metadata["Lux"])
    if x == number-1:
        sleep(1)
    else:
        sleep(interval)

sleep(5)
picam2.stop()
picam2.close()
