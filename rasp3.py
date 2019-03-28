import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(7,GPIO.IN)
GPIO.setup(8,GPIO.OUT)
while True:
    if GPIO.input(7)==1:
        GPIO.output(8,1)
        print("led is on now")
        
    else:
        GPIO.output(8,0)
        print("led is off now")
        
