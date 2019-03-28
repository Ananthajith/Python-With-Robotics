import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
a=3
b=5
c=7
d=11
e=12
f=13
g=15
h=16
s=0
GPIO.setup(16,GPIO.IN)
GPIO.setup(a,GPIO.OUT)
GPIO.setup(b,GPIO.OUT)
GPIO.setup(c,GPIO.OUT)
GPIO.setup(d,GPIO.OUT)
GPIO.setup(e,GPIO.OUT)
GPIO.setup(f,GPIO.OUT)
GPIO.setup(g,GPIO.OUT)
GPIO.setup(h,GPIO.OUT)
while True:
    if GPIO.input(16)==1:
        if s==0:
            GPIO.output(a,0)
            GPIO.output(b,0)
            GPIO.output(c,0)
            GPIO.output(d,0)
            GPIO.output(e,0)
            GPIO.output(f,0)
            GPIO.output(g,1)
            GPIO.output(h,1)
            print("zero")
            s=s+1
            time.sleep(2)
       
        elif s==1:
            #one#
            GPIO.output(a,1)
            GPIO.output(b,0)
            GPIO.output(c,0)
            GPIO.output(d,1)
            GPIO.output(e,1)
            GPIO.output(f,1)
            GPIO.output(g,1)
            GPIO.output(h,1)
            print("one")
            s=s+1
            time.sleep(2)
        elif s==2:
             #two#
            GPIO.output(a,0)
            GPIO.output(b,0)
            GPIO.output(c,1)
            GPIO.output(d,0)
            GPIO.output(e,0)
            GPIO.output(f,1)
            GPIO.output(g,0)
            GPIO.output(h,1)
            print("two")
            s=s+1
            time.sleep(2)
            #three#
        elif s==3:
            GPIO.output(a,0)
            GPIO.output(b,0)
            GPIO.output(c,0)
            GPIO.output(d,0)
            GPIO.output(e,1)
            GPIO.output(f,1)
            GPIO.output(g,0)
            GPIO.output(h,1)
            print("three")
            s=s+1
            time.sleep(2)
        elif s==4:
            #four#
            GPIO.output(a,1)
            GPIO.output(b,0)
            GPIO.output(c,0)
            GPIO.output(d,1)
            GPIO.output(e,1)
            GPIO.output(f,0)
            GPIO.output(g,0)
            GPIO.output(h,1)
            print("four")
            s=s+1
            time.sleep(2)
        elif s==5:
            #five#
            GPIO.output(a,0)
            GPIO.output(b,1)
            GPIO.output(c,0)
            GPIO.output(d,0)
            GPIO.output(e,1)
            GPIO.output(f,0)
            GPIO.output(g,0)
            GPIO.output(h,1)
            print("five")
            s=s+1
            time.sleep(2)
        elif s==6:
            #six#
            GPIO.output(a,0)
            GPIO.output(b,1)
            GPIO.output(c,0)
            GPIO.output(d,0)
            GPIO.output(e,0)
            GPIO.output(f,0)
            GPIO.output(g,0)
            GPIO.output(h,1)
            print("six")
            s=s+1
            time.sleep(2)
        elif s==7:
            #seven#
            GPIO.output(a,0)
            GPIO.output(b,0)
            GPIO.output(c,0)
            GPIO.output(d,1)
            GPIO.output(e,1)
            GPIO.output(f,1)
            GPIO.output(g,1)
            GPIO.output(h,1)
            print("seven")
            s=s+1
            time.sleep(2)
        elif s==8:
            #eight#
            GPIO.output(a,0)
            GPIO.output(b,0)
            GPIO.output(c,0)
            GPIO.output(d,0)
            GPIO.output(e,0)
            GPIO.output(f,0)
            GPIO.output(g,0)
            GPIO.output(h,1)
            print("eight")
            s=s+1
            time.sleep(2)
        elif s==9:
            #nine#
            GPIO.output(a,0)
            GPIO.output(b,0)
            GPIO.output(c,0)
            GPIO.output(d,1)
            GPIO.output(e,1)
            GPIO.output(f,0)
            GPIO.output(g,0)
            GPIO.output(h,1)
            print("nine")
            s=s+1
            time.sleep(2)
            
 
