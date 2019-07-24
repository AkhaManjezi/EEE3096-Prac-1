#!/usr/bin/python3
"""
Python Practical Template
Keegan Crankshaw
Readjust this Docstring as follows:
Names: Akha Manjezi
Student Number: MNJSIN002
Prac: 1
Date: 23/07/2019
"""

# import Relevant Librares
import RPi.GPIO as GPIO

led_1 = 17 #physical pin 11
led_2 = 23 #physical pin 16
led_3 = 24 #physical pin 18
button_up = 27 #physical pin 13
button_down = 22 #physical pin 15


GPIO.setmode(GPIO.BCM)
GPIO.setup(led_1, GPIO.OUT)
GPIO.setup(led_2, GPIO.OUT)
GPIO.setup(led_3, GPIO.OUT)
GPIO.setup(button_up, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(button_down, GPIO.IN, pull_up_down=GPIO.PUD_UP)

values = ["000", "001", "010", "011", "100", "101", "110", "111"]
global x
x = 0

def increment(channel):
    global x
    if x == 7:
        x = 0
    else:
        x += 1
    GPIO.output(led_1, int(values[x][0]))
    GPIO.output(led_2, int(values[x][1]))
    GPIO.output(led_3, int(values[x][2]))

def decrement(channel):
    global x
    if x == 0:
        x = 7
    else:
        x -= 1
    GPIO.output(led_1, int(values[x][0]))
    GPIO.output(led_2, int(values[x][1]))
    GPIO.output(led_3, int(values[x][2]))

GPIO.add_event_detect(button_up, GPIO.FALLING, callback=increment, bouncetime=200)
GPIO.add_event_detect(button_down, GPIO.FALLING, callback=decrement, bouncetime=200)


# Only run the functions if 
if __name__ == "__main__":
    # Make sure the GPIO is stopped correctly
    try:
        while True:
            pass 
    except KeyboardInterrupt:
        print("Exiting gracefully")
        # Turn off your GPIOs here
        GPIO.cleanup()
    except e:
        GPIO.cleanup()
        print("Some other error occurred")
        print(e.message)
