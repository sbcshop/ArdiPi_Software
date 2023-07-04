'''
For this example code library file used -> sdcard.py
https://github.com/sbcshop/ArdiPi_Software/blob/main/examples/lib/sdcard.py
----------------------------------------------------------------------------------------------------
This simple demo code creates new file as File.txt into SD card and writes 'Hello World!' text inside file 
'''                

from machine import Pin, SPI ,UART
import sdcard
import os
import utime

uart = UART(0,baudrate = 9600,tx = Pin(0),rx = Pin(1))

def sdtest(data):
    #define and configure SPI interfacing of sdcard with Pico
    spi=SPI(0,sck=Pin(2),mosi=Pin(3),miso=Pin(4))
    sd=sdcard.SDCard(spi,Pin(5))

    #mount file system
    vfs = os.VfsFat(sd)
    os.mount(vfs, "/fc") 
    print("Filesystem check")
    print(os.listdir("/fc"))

    #file name 
    fn = "/fc/File.txt"
    print()
    print("Single block read/write")

    #write operation 
    with open(fn, "a") as f:
        n = f.write(data)  
        print(n, "bytes written")

    #read operation
    with open(fn, "r") as f:
        result2 = f.read()
        print(len(result2), "bytes read")

    os.umount("/fc")
while True:
    sdtest('Hello World!')
    utime.sleep(0.5)
