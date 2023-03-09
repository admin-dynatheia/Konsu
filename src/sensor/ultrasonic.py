

import time
import RPi.GPIO as GPIO
from main import *

import sys 
sys.path.insert(0, '../')
from main import *

# Function to use the Ultrasonic sensor for distance measurements
def ultrasonic(TRIG, ECHO):
    # TRIG=21
    # ECHO=20
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    print("Starting ultra sonic sensor distance measurements!")
    while True:
        # print("distance measurement in progress")
        GPIO.setup(TRIG,GPIO.OUT)
        GPIO.setup(ECHO,GPIO.IN)
        GPIO.output(TRIG,False)
        # print("waiting for sensor to settle")
        # time.sleep(0.01)
        GPIO.output(TRIG,True)
        time.sleep(0.00001)
        GPIO.output(TRIG,False)
        while GPIO.input(ECHO)==0:
            pulse_start=time.time()
        while GPIO.input(ECHO)==1:
            pulse_end=time.time()
        pulse_duration=pulse_end-pulse_start
        distance=pulse_duration*17150
        distance=round(distance,2)
        # print("distance:",distance,"cm")
        progress_bar(distance, 1500, 100)
        time.sleep(0.05)