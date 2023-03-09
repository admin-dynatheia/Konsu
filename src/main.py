#!/usr/bin/python

# Importing needed libraries
from asyncio.base_subprocess import ReadSubprocessPipeProto
from gpiozero import LED
import RPi.GPIO as GPIO
import time
import sys 
import signal

sys.path.insert(0, '/home/rover-delta/rover_core/src/sensor')
sys.path.insert(0, '/home/rover-delta/rover_core/src/terminal')

from sensor.ultrasonic import *
from  terminal.color import *
# Function to blink the LED on GPIO 13
def blink():
    led = LED(13)
    led.off()

    print("Starting LED blinking loop")
    while True:
        led.on()
        print("LED on.")
        time.sleep(.5)
        led.off()
        print("LED off.")
        time.sleep(.5)

# Function to use PWM Brightness control for LED on GPIO 13
def pwm():
    ledpin = 13				# PWM pin connected to LED
    GPIO.setwarnings(False)			#disable warnings
    GPIO.setmode(GPIO.BCM)		#set pin numbering system
    GPIO.setup(ledpin,GPIO.OUT)
    
    pi_pwm = GPIO.PWM(ledpin,1000)		#create PWM instance with frequency
    pi_pwm.start(0)				#start PWM of required Duty Cycle 
    
    print("Starting PWM LED Control!")
    while True:
        for i in range(0, 101, 1):  
            pi_pwm.ChangeDutyCycle(i)
            time.sleep(0.005)
        time.sleep(0.5)

        for i in range(100, -1, -1):
            pi_pwm.ChangeDutyCycle(i)
            time.sleep(0.005)
        time.sleep(0.5)



# Branch function to get user defined program flow
def branch():
    funct = input(bcolors.HEADER + f"MENU"+bcolors.WARNING+"\n\tEnter 'b' to Blink the LED\n\tEnter 'p' to use PWM\n\tEnter 'u' to use Ultrasonic Sensor\n\tEnter 'q' to exit program\n\n"+bcolors.UNDERLINE+bcolors.OKBLUE+"Entry: " + bcolors.ENDC)
    if funct == 'p':
        pwm()
    elif funct == 'u':
        ultrasonic(21, 20)
    elif funct == 'b':
        blink()
    elif funct == 'q':
        exit()
    else:
        print(bcolors.FAIL + f'\nInvalid Entry \n' + bcolors.ENDC)
        branch()

# Control C handler function to continue execution or exit
def signal_handler(signal, frame):
    print(' = You pressed Ctrl+C!')
    val = input("Would you like to end the program? Enter 'q' - or input any other character to continue: ")
    if val == 'q':    
        print(signal) # Value is 2 for CTRL + C
        print(frame) # Where your execution of program is at moment - the Line Number
        sys.exit(0)
    else:
        # Note there is a bug where you cant blink the LED twice in a row, need to find a way to release the resource when interupt occurs
        GPIO.cleanup(13)
        branch()

# Assign Handler Function
signal.signal(signal.SIGINT, signal_handler)

def progress_bar(current, total, bar_length=20):
    fraction = current / total

    arrow = int(fraction * bar_length - 1) * '-' + '>'
    padding = int(bar_length - len(arrow)) * ' '

    ending = '\n' if current == total else '\r'

    print(f'Loading Rover CORE: [{arrow}{padding}] {int(fraction*100)}%', end=ending)

# Main function
def main():
    print(bcolors.OKCYAN+"\n\nWelcome to Rover Delta!\n"+bcolors.ENDC)
    for i in range(0, 101, 1):
        progress_bar(i,100,50)
        time.sleep(0.01)
    

    branch()


# Main function preprocessor
if __name__ == "__main__":
    main()