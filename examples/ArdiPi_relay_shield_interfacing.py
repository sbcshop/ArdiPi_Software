# import library for Pin control and time module
from machine import Pin
import time

# Define 4, 3, 11, & 10 GPIO Pins as OUTPUT
relay1 = machine.Pin(4, machine.Pin.OUT)
relay2 = machine.Pin(3, machine.Pin.OUT)
relay3 = machine.Pin(11, machine.Pin.OUT)
relay4 = machine.Pin(10, machine.Pin.OUT)

# Set LOW, Switch OFF each relay initially
relay1.value(0)
relay2.value(0)
relay3.value(0)
relay4.value(0)


while 1:
    relay1.value(1) # Set High to Switch ON relay
    time.sleep(0.5)	# Wait half second
    relay2.value(1)	
    time.sleep(0.5)
    relay3.value(1)	
    time.sleep(0.5)
    relay4.value(1)	
    time.sleep(0.5)

    relay1.value(0) # Set LOW to Switch OFF relay
    relay2.value(0)
    relay3.value(0)
    relay4.value(0)
    time.sleep(1)
