from requests import get
import json
import RPi.GPIO as GPIO
import keyboard
from time import sleep
# from picamera import PiCamera

GPIO.setmode(GPIO.BCM)
GPIO.setup(6,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)
GPIO.setup(19,GPIO.OUT)
GPIO.setup(26,GPIO.OUT)

def reset():
    GPIO.output(6,GPIO.LOW)
    GPIO.output(13,GPIO.LOW)
    GPIO.output(19,GPIO.LOW)
    GPIO.output(26,GPIO.LOW)
    sleep(0)
    
def forward():
    GPIO.output(6,GPIO.HIGH)
    GPIO.output(13,GPIO.LOW)
    GPIO.output(19,GPIO.HIGH)
    GPIO.output(26,GPIO.LOW)
    sleep(0)
    
def backward():
    GPIO.output(6,GPIO.LOW)
    GPIO.output(13,GPIO.HIGH)
    GPIO.output(19,GPIO.LOW)
    GPIO.output(26,GPIO.HIGH)
    sleep(0)
    
def left():
    GPIO.output(6,GPIO.HIGH)
    GPIO.output(13,GPIO.LOW)
    GPIO.output(19,GPIO.LOW)
    GPIO.output(26,GPIO.HIGH)
    sleep(0)

def right():
    GPIO.output(6,GPIO.LOW)
    GPIO.output(13,GPIO.HIGH)
    GPIO.output(19,GPIO.HIGH)
    GPIO.output(26,GPIO.LOW)
    sleep(0)
    
#https://qmoki89va7.execute-api.us-east-2.amazonaws.com/test/key?up=h&down=b&left=l&right=r

#camera = PiCamera()
#camera.resolution = (1024,768)
#camera.start_preview()

#sleep(2)

while True:
    
    sth = get('http://ec2-3-80-22-87.compute-1.amazonaws.com:8080/products').json()
        
    for key in sth[0]:
        value= sth[0].get(key,'name')
        print(key,value)
        
        if value == 'f':
            forward()
        elif value == 'b':
            backward()
        elif value == 'l':
            left()
        elif value =='r':
            right()
        #elif value == 's':
            #camera.stop_preview()
        else:  
            reset()
    sleep(0)
   
    


