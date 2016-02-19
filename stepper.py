import RPi.GPIO as GPIO
import time
import sys

#11/12/15/16 to step motor 1/2/3/4
GPIO.setmode(GPIO.BOARD)
#pins = [17,18,22,23]
pins = [16,15,12,11]
GPIO.setup(pins,GPIO.OUT)
interval = 0.005

clockwise = 0
if len(sys.argv) > 1:
        clockwise = int(sys.argv[1])
if clockwise == 1:
        pins = [11,12,15,16]
#for a in range(5):
while (True):
        for i in range(len(pins)):
                GPIO.output(pins[i],0)
                if i+1 >= len(pins):
                        i = -1
                GPIO.output(pins[i+1],1)
                time.sleep(interval)
GPIO.cleanup()
