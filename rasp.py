import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(8,GPIO.OUT)
while True:
    GPIO.output(8,1)
    time.sleep(2)
    print("led on")
    GPIO.output(8,0)
    time.sleep(2)
    print("led off")
