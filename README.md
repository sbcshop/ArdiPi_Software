# ArdiPi_Software
<img src="">
Introducing ArdiPi the ultimate Arduino Uno alternative packed with powerful specs and exciting features in Arduino Uno form factor. You can enjoy a low-cost solution with access to the largest support communities for Raspberry Pi. 
This github provides getting started guide and other working details for ArdiPi.

### Features:
- Arduino UNO Form factor, so you can connect 3.3V compatible Arduino shields  
- SD card slot for storage and data transfer
- Drag-and-drop programming using mass storage over USB
- Multifunction GPIO breakout supporting general I/O, UART, I2C, SPI, ADC & PWM function.
- Multi-tune Buzzer to add audio alert into project
- SWD pins breakout for serial debugging 
- Multi-platform support like Arduino IDE, MicroPython and CircuitPython.
- Comes with HID support, so device can simulate a mouse or keyboard

### Specifications:
- Powered by RP2040 microcontroller which is dual-core Arm Cortex-M0+ processor, 2MB of onboard flash storage, 264kB of RAM
- On-board single-band 2.4GHz wireless interfaces (802.11n) for WiFi and Bluetooth® 5 (LE)
- WPA3 & Soft access point supporting up to four clients
- Operating voltage of pins 3.3V and board supply 5V
- 25 Multipurpose GPIOs breakout in Arduino style for easy peripheral interfacing
- I2C, SPI, and UART communications protocol support
- 2MB of onboard Flash memory
- Cross platform development and multiple programming language support

## Getting Started with ArdiPi
### Hardware Overview
#### Pinout
<img src="https://github.com/sbcshop/ArdiPi_Software/blob/main/images/ArdiPi_pinout.jpg">

- (1) Buzzer 
- (2) RPi Pico W
- (3) Reset Button
- (4) & (8) Multipurpose GPIO breakout 
- (5) Power LED
- (6) SWD & GPIO breakout
- (7) SD card slot
- (9) & (10) Power Pins

#### GPIO Pins Detail
<img src="https://github.com/sbcshop/ArdiPi_Software/blob/main/images/ArdiPI_GPIO_PinDetail.jpg">


### 1. Step to install boot Firmware
   - Every ArdiPi board will be provided with boot firmware already installed, so you can directly go to step 2.
   - If, in any case, you are required to install firmware for your board, then you can follow the guide [here](https://github.com/sbcshop/EnkPi_7.5_Software/blob/main/Downloads/Pico%20W%20Micropython%20Firmware%20Installation%20Steps.pdf)

### 2. Onboard LED Blink 
   - Download **Thonny IDE** from [Download link](https://thonny.org/) as per your OS and install it.
   - Once done start **Thonny IDE application**, Connect Touchsy with a laptop/PC using a micro USB cable and the micro USB port on Pico W present on Touchsy.
   - Select device at the bottom right with a suitable COM port, as shown in the below figure. You might get a different COM port.
      <img src= "https://github.com/sbcshop/EnkPi_2.9_Software/blob/main/images/img1.jpg" />
      <img src= "https://github.com/sbcshop/EnkPi_2.9_Software/blob/main/images/img2.jpg" />
   - Write simple onboard blink Python code or [Download Led blink code](https://github.com/sbcshop/3.2_Touchsy_Pico_W_Capacitive_Software/blob/main/examples/onboard_ledBlink.py), then click on the green run button to make your script run on Touchsy. 
      <img src= "https://github.com/sbcshop/EnkPi_2.9_Software/blob/main/images/img3.jpg" />
     
     Now that we've reached this point, you're executing your script through Thonny IDE, so if you unplug Pico, it will stop running. To run your script without using an IDE, simply power up Touchsy and it should run your script, go to step 3. Once you have transferred your code to the Touchsy board, to see your script running, just plug in power either way using micro USB or Type C, both will work.

### 3. How to move your script on Pico W of Touchsy
   - Click on File -> Save Copy -> select Raspberry Pi Pico , Then save file as main.py
     
      <img src="https://github.com/sbcshop/3.2_Touchsy_Pico_W_Resistive_Software/blob/main/images/transfer_script_pico.gif" />
   
   In similar way you can add various python code files to Pico. Also you can try out sample codes given here in [examples folder](https://github.com/sbcshop/3.2_Touchsy_Pico_W_Capacitive_Software/tree/main/examples). But make sure you have all required library files inside Pico W of Touchsy, if not only then follow below steps otherwise skip.
   
   - Mostly you will receive Touchsy with all required library files preinstalled. But in any case if you need to save library files from [lib](https://github.com/sbcshop/3.2_Touchsy_Pico_W_Capacitive_Software/tree/main/lib) folder into Pico W of Touchsy, then download repo and follow below steps to move lib file into Pico of Touchsy.
      <img src="https://github.com/sbcshop/3.2_Touchsy_Pico_W_Capacitive_Software/blob/main/images/multiple_file_transfer.gif" />
   
**NOTE: Don't rename _lib_ files** and also you will have to move related font file if used inside code.


### Example Codes
   Save whatever example code file you want to try as main.py in pico w as shown in above [step 3](https://github.com/sbcshop/3.2_Touchsy_Pico_W_Capacitive_Software#3-how-to-move-your-script-on-pico-w-of-touchsy), also add related lib files with default name.
   - [Example 1](https://github.com/sbcshop/3.2_Touchsy_Pico_W_Capacitive_Software/blob/main/examples/DisplayDemo.py) : Display demo code
   - [Example 2](https://github.com/sbcshop/3.2_Touchsy_Pico_W_Capacitive_Software/blob/main/examples/TouchDemo.py) : Touch demo code
   - [Example 3](https://github.com/sbcshop/3.2_Touchsy_Pico_W_Capacitive_Software/blob/main/examples/ButtonDemo.py) : Button & Buzzer testing with display code
   - [Example 4](https://github.com/sbcshop/3.2_Touchsy_Pico_W_Capacitive_Software/blob/main/examples/demo_SDcard.py) : How to use sdcard for data write operation
   - [Example 5](https://github.com/sbcshop/3.2_Touchsy_Pico_W_Capacitive_Software/blob/main/examples/colorWheel.py) : Animation colorWheel demo
   - and [Many more...](https://github.com/sbcshop/3.2_Touchsy_Pico_W_Capacitive_Software/tree/main/examples)
   
   Now you are ready to try out your own codes, **_Happy Coding!_**
   
## Resources
  * [Schematic](https://github.com/sbcshop/3.2_Touchsy_Pico_W_Capacitive_Hardware/blob/main/Design%20Data/SCH%20Touchsy%20based%20on%20PICO%20W%20(capacitive).pdf)
  * [Hardware Files](https://github.com/sbcshop/3.2_Touchsy_Pico_W_Capacitive_Hardware/tree/main)
  * [Step File](https://github.com/sbcshop/3.2_Touchsy_Pico_W_Capacitive_Hardware/blob/main/Mechanical%20Data/STEP%20Touchsy%20based%20on%20PICO%20W%20(capacitive).step)
  * [MicroPython getting started for RPi Pico/Pico W](https://docs.micropython.org/en/latest/rp2/quickref.html)
  * [Pico W Getting Started](https://projects.raspberrypi.org/en/projects/get-started-pico-w)
  * [RP2040 Datasheet](https://github.com/sbcshop/HackyPi-Hardware/blob/main/Documents/rp2040-datasheet.pdf)


## Related Products
   * [3.2" Touchsy ESP32](https://shop.sb-components.co.uk/collections/pre-order/products/touchsy-3-2-touch-lcd-display-based-on-esp32-mcu) - 3.2" Touchsy ESP32 with Resistive and Capacitive version. 
   * [3.2" Touchsy Pico W](https://shop.sb-components.co.uk/collections/pre-order/products/touchsy-3-2-touch-lcd-display-based-on-pico-w) - 3.2" Touchsy Pico W with Resistive and Capacitive version.
   * [3.2" Touchsy Breakout](https://shop.sb-components.co.uk/collections/pre-order/products/touchsy-3-2-touch-lcd-display-breakout-board) - 3.2" Touchsy Breakout with Resistive and Capacitive version.
   * [3.2" Touchsy HAT](https://shop.sb-components.co.uk/collections/pre-order/products/touchsy-3-2-touch-lcd-display-for-raspberry-pi) - 3.2" Touchsy HAT with Resistive version for Raspberry Pi.
   * [1.28" Round Touch LCD HAT](https://shop.sb-components.co.uk/products/1-28-round-touch-lcd-hat-for-raspberry-pi?_pos=2&_sid=6c0f5891d&_ss=r) - 1.28" Round Touch LCD HAT for Raspberry Pi.

## Product License

This is ***open source*** product. Kindly check LICENSE.md file for more information.

Please contact support@sb-components.co.uk for technical support.
<p align="center">
  <img width="360" height="100" src="https://cdn.shopify.com/s/files/1/1217/2104/files/Logo_sb_component_3.png?v=1666086771&width=300">
</p>
