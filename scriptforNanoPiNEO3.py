import forecruxGPIO3 as GPIO
import urllib.request
import time

pin = 203
url = "http://www.kashing.hk/photo/button.txt"
whileloopsleeptimeurl = "http://192.168.1.50/whileloopsleeptime.txt"
whileloopsleeptime = urllib.request.urlopen(whileloopsleeptimeurl).read().decode('UTF-8')

GPIO.setup(pin, GPIO.OUTPUT)

while(1):
    #time.sleep(whileloopsleeptime)
    status = urllib.request.urlopen(url).read().decode('UTF-8')

    if status=='ON':
        GPIO.output(pin,1)
        time.sleep(2)
    elif status=='OFF':
        GPIO.output(pin,0)
        time.sleep(2)
    else:
        GPIO.clear(pin)
