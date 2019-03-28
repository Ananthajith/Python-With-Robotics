import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False) 
GPIO.setmode(GPIO.BOARD)
s1=3
s2=15
s3=2
l1=8
l2=10
l3=12
GPIO.setup(3,GPIO.IN)
GPIO.setup(15,GPIO.IN)
GPIO.setup(18,GPIO.IN)
GPIO.setup(8,GPIO.OUT)
GPIO.setup(10,GPIO.OUT)
GPIO.setup(12,GPIO.OUT)

while True:
    if GPIO.input(3)==1:
        GPIO.output(l1,1)
        GPIO.output(l2,0)
        GPIO.output(l3,0)
        print("led 1 is on")
    elif GPIO.input(15)==1:
        GPIO.output(l1,0)
        GPIO.output(l2,1)
        GPIO.output(l3,0)
        print("led 2 is on")
    elif GPIO.input(18)==1:
        GPIO.output(l1,0)
        GPIO.output(l2,0)
        GPIO.output(l3,1)
        print("led 3 is on")
