import RPi.GPIO as GPIO
import time
import os
GPIO.setmode(GPIO.BOARD)
GPIO.setup(16,GPIO.IN)
GPIO.setwarnings(False) 
while True:
    if GPIO.input(16)==1:
        os.system("sudo fswebcam /home/pi/%H%H%S.jpg")
