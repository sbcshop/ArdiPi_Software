from machine import Pin,SPI
import time
import st7789 #library of TFT display controller uses SPI interface
import vga1_bold_16x32 as font 

# Define buttons as INPUT Pull UP to read status button pressed status
button1 = Pin(3,Pin.IN, Pin.PULL_UP)
button2 = Pin(11, Pin.IN, Pin.PULL_UP)

joy_up = Pin(4, Pin.IN, Pin.PULL_UP)
joy_down = Pin(0, Pin.IN, Pin.PULL_UP)
joy_left = Pin(5, Pin.IN, Pin.PULL_UP)
joy_right = Pin(2, Pin.IN, Pin.PULL_UP)
joy_centre = Pin(1, Pin.IN, Pin.PULL_UP)

# configure SPI communication for Display
spi = SPI(0, baudrate=40000000, sck=Pin(18), mosi=Pin(19))
tft = st7789.ST7789(spi,240,320,reset=Pin(14, Pin.OUT),cs=Pin(17, Pin.OUT),dc=Pin(15, Pin.OUT),backlight=Pin(16, Pin.OUT),rotation=1)#SPI interface for tft screen

def displayTest():
    tft.init()
    time.sleep(0.5)#time delay
    tft.text(font,"2.0\" LCD SHIELD", 10,40,st7789.YELLOW)# print on tft screen
    tft.fill_rect(0, 72, 320,8, st7789.RED)#display red line on tft screen
    
    tft.text(font,"SB Components", 10,120,st7789.WHITE)
    tft.fill_rect(0, 152, 320,10, st7789.CYAN)
    
time.sleep(1)

displayTest()
while 1:
    val1 = button1.value()
    val2 = button2.value()
    
    val3 = joy_up.value()
    val4 = joy_down.value()
    val5 = joy_left.value()
    val6 = joy_right.value()
    val7 = joy_centre.value()
    print("val1 = ",val1)
    if val1 == 0:
        print("val1 = ",val1)
        tft.text(font,"BT1 Pressed!", 10,180,st7789.WHITE)
    elif val2 == 0:
        print("val2 = ",val2)
        tft.text(font,"BT2 Pressed!", 10,180,st7789.WHITE)
    elif val3 == 0:
        print("val3 = ",val3)
        tft.text(font,"RIGHT", 10,180,st7789.WHITE)
    elif val4 == 0:
        print("val4 = ",val4)
        tft.text(font,"DOWN", 10,180,st7789.WHITE)
    elif val5 == 0:
        print("val5 = ",val5)
        print("val4 = ",val4)
        tft.text(font,"LEFT", 10,180,st7789.WHITE)
    elif val6 == 0:
        print("val6 = ",val6)
        print("val4 = ",val4)
        tft.text(font,"UP", 10,180,st7789.WHITE)
    elif val7 == 0:
        print("val7 = ",val7)
        print("val4 = ",val4)
        tft.text(font,"Centre", 10,180,st7789.WHITE)
    else :
        tft.text(font,"             ", 10,180,st7789.WHITE)
        
    time.sleep(0.2)
