#!/usr/bin/python

# Importing needed libraries
from asyncio.base_subprocess import ReadSubprocessPipeProto
from gpiozero import LED
import RPi.GPIO as GPIO
import time
import sys 
import signal

ledpin = 13				# PWM pin connected to LED
GPIO.setwarnings(False)			#disable warnings
GPIO.setmode(GPIO.BCM)		#set pin numbering system
GPIO.setup(ledpin,GPIO.OUT)

pi_pwm = GPIO.PWM(ledpin,1000)		#create PWM instance with frequency
pi_pwm.start(0)				#start PWM of required Duty Cycle 

print("Starting PWM LED Control!")
while True:
	for i in range(0, 50, 1):  
		pi_pwm.ChangeDutyCycle(i)
		time.sleep(0.5)
	time.sleep(0.5)

	# for i in range(100, -1, -1):
	# 	pi_pwm.ChangeDutyCycle(i)
	# 	# time.sleep(0.005)
	# time.sleep(0.5)
