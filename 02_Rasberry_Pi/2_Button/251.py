import RPi.GPIO as GPIO
import time
count = 0

GPIO.cleanup()
GPIO.setmode(GPIO.BCM)
GPIO.setup(9, GPIO.IN, pull_up_down=GPIO.PUD_UP)
while True:
    if(GPIO.input(9)==0):
        count = count + 1
        print("Count: " + str(count))
        while(GPIO.input(9)==0):
            time.sleep(0.1)

