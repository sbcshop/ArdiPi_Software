from machine import Pin, PWM, I2C, UART  #inbuild libraries import  
from ssd1306 import SSD1306_I2C		#display controller library 
from uhf import UHF					#library for UHF module related methods
import time

WIDTH  = 120   # oled display width
HEIGHT = 32    # oled display height

enable_pin = machine.Pin(4, machine.Pin.OUT) #define enable pin as OUTPUT
enable_pin.value(0) #LOW to Enable UHF module, while HIGH value to disable 

BUZZER_PIN = 2 # Piezo buzzer + is connected to GP2, - is connected to the GND
buzzer = PWM(Pin(BUZZER_PIN, Pin.OUT))

i2c = I2C(0,freq=200000,sda=Pin(20),scl=Pin(21)) 	#configure I2C communication
print("I2C Address      : "+hex(i2c.scan()[0]).upper()) # Display device address
print("I2C Configuration: "+str(i2c))                   # Display I2C config

oled = SSD1306_I2C(WIDTH, HEIGHT, i2c)                  # Init oled display
    
oled.text("SB COMPONENTS",10,10)
oled.show()
time.sleep(2)
oled.fill(0)
oled.show()

baudrate = 115200	# set serial baudrate
uhf = UHF(baudrate)
uhf.multiple_read()
try:
    while 1:
        rev = uhf.read_mul()
        if rev is not None:
            #print(rev)
            oled.text(str("".join(rev[8:20])),10,10)
            oled.show()
            print('EPC = ',"".join(rev[8:20]))
            print('RSSI(dBm) = ',rev[5])
            print('CRC = ',rev[20],rev[21])
            buzzer.duty_u16(5000)  # adjust loudness: smaller number is quieter.
            buzzer.freq(454)
            time.sleep(0.5)
            buzzer.duty_u16(0) # loudness set to 0 = sound off
        time.sleep(0.0009)
        oled.fill(0)
        oled.show()
        
except KeyboardInterrupt:
    uhf.stop_read()
    time.sleep(1)
    print("stop")
