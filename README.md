# ArdiPi_Software
<img src="https://cdn.shopify.com/s/files/1/1217/2104/files/ARDIPI_bannerRev.jpg?v=1688463003">
Introducing ArdiPi the ultimate Arduino Uno alternative packed with powerful specs and exciting features in Arduino Uno form factor. You can enjoy a low-cost solution with access to the largest support communities for Raspberry Pi. 
This github provides getting started guide and other working details for ArdiPi.

ArdiPi Compatible Shields are [Relay](https://shop.sb-components.co.uk/products/ardi-relay-shield-for-arduino-uno?_pos=4&_sid=961a5887c&_ss=r), [RFID](https://shop.sb-components.co.uk/products/ardi-rfid-shield-for-arduino-uno?_pos=5&_sid=b4e4b2ef1&_ss=r), [Display](https://shop.sb-components.co.uk/products/ardi-display-shield-for-arduino-uno?_pos=5&_sid=961a5887c&_ss=r) and [UHF](https://shop.sb-components.co.uk/products/ardi-uhf-shield-for-arduino-uno?variant=40791294836819) which you can use to add more functionality into projects. 

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

### Interfacing Details
  | Pico W | Hardware Pin | Function |
  |---|---|---|
  |GP18 | SCLK | Clock pin of SPI interface for microSD card |
  |GP19 | DIN  | MOSI (Master OUT Slave IN) data pin of SPI interface for microSD card|
  |GP16 | DOUT | MISO (Master IN Slave OUT) data pin of SPI interface for microSD card|
  |GP17 | CS   | Chip Select pin of SPI interface for microSD card|
  |GP22 | Buzzer| Buzzer PWM pin connection|

Note: When SD card not connected, then above related pins can be used for normal GPIO operations.


### 1. Step to install boot Firmware
   - Every ArdiPi board will be provided with boot firmware already installed, so you can skip this step and directly go to step 2.
   - If in case you want to install firmware for your board, Push and hold the BOOTSEL button and plug your Pico W into the USB port of your computer. Release the BOOTSEL button after your Pico is connected.
   <img src="https://github.com/sbcshop/ArdiPi_Software/blob/main/images/pico_bootmode.gif">
   
   - It will mount as a Mass Storage Device called RPI-RP2.
   - Drag and drop the MicroPython UF2 - [ArdiPi_firmware](https://github.com/sbcshop/ArdiPi_Software/blob/main/ArdiPi_firmware.uf2) file provided in this github onto the RPI-RP2 volume. Your Pico will reboot. You are now running MicroPython on ArdiPi.

### 2. Onboard LED Blink 
   - Download **Thonny IDE** from [Download link](https://thonny.org/) as per your OS and install it.
   - Once done start **Thonny IDE application**, Connect ArdiPi to laptop/PC.
   - Select device at the bottom right with a suitable COM port, as shown in the below figure. You might get a different COM port.
     
      <img src= "https://github.com/sbcshop/EnkPi_2.9_Software/blob/main/images/img1.jpg" />
      <img src= "https://github.com/sbcshop/EnkPi_2.9_Software/blob/main/images/img2.jpg" />
      
   - Write simple onboard blink Python code or [Download Led blink code](https://github.com/sbcshop/ArdiPi_Software/blob/main/examples/onboard_ledBlink.py), then click on the green run button to make your script run on ArdiPi.
     
      <img src= "https://github.com/sbcshop/EnkPi_2.9_Software/blob/main/images/img3.jpg" />
     
     Now that we've reached this point, you're executing your script through Thonny IDE, so if you unplug Pico, it will stop running. To run your script without using an IDE, simply power up ArdiPi and it should run your script, go to step 3. Once you have transferred your code to the ArdiPi board, to see your script running, just plug in power either way using micro USB or via Vin, both will work.

### 3. How to move your script on Pico W of ArdiPi
   - Click on File -> Save Copy -> select Raspberry Pi Pico , Then save file as main.py
     
      <img src="https://github.com/sbcshop/3.2_Touchsy_Pico_W_Resistive_Software/blob/main/images/transfer_script_pico.gif" />
   
      In similar way you can add various python code files to Pico. Also you can try out sample codes given here in [examples folder](https://github.com/sbcshop/ArdiPi_Software/tree/main/examples). 
   
   - But in case if you want to move multiple files at one go, example suppose you are interested to save library files folder into Pico W, below image demonstrate that
     
      <img src="https://github.com/sbcshop/3.2_Touchsy_Pico_W_Capacitive_Software/blob/main/images/multiple_file_transfer.gif" />
   
**NOTE: Don't rename _lib_ files** or and other files, only your main code script should be rename as main.py for standalone execution without Thonny.


### Example Codes
   Save whatever example code file you want to try as main.py in pico w as shown in above [step 3](https://github.com/sbcshop/ArdiPi_Software/tree/main#3-how-to-move-your-script-on-pico-w-of-ardipi), also add related lib files with default name.
   In [example](https://github.com/sbcshop/ArdiPi_Software/tree/main/examples) folder you will find demo example script code to test onboard components of ArdiPi like 
   - [Buzzer](https://github.com/sbcshop/ArdiPi_Software/blob/main/examples/BuzzerDemo.py), 
   - [SD card](https://github.com/sbcshop/ArdiPi_Software/blob/main/examples/sdcardDemo.py),
   
   Also, sample codes are available for ArdiPi shields
   - [Relay](https://github.com/sbcshop/ArdiPi_Software/blob/main/examples/relay_shield_demo.py) : code test switching of relays in sequence 
   - [RFID](https://github.com/sbcshop/ArdiPi_Software/blob/main/examples/RFID_shield_demo.py) : code to test RFID module scan and switching of Relay
   - [Display](https://github.com/sbcshop/ArdiPi_Software/blob/main/examples/display_shield_Demo.py) : testing of display and programmable buttons
   - [UHF]() : testing onboard UHF module , buzzer and display unit of shield 
   
   Using this sample code as a guide, you can modify, build, and share codes!!  
   
## Resources
  * [Schematic](https://github.com/sbcshop/ArdiPi_Hardware/blob/main/Design%20Data/SCH_ArdiPi.pdf)
  * [Hardware Files](https://github.com/sbcshop/ArdiPi_Hardware/tree/main)
  * [Step File](https://github.com/sbcshop/ArdiPi_Hardware/blob/main/Mechanical%20Data/STEP_ArdiPi.step)
  * [MicroPython getting started for RPi Pico/Pico W](https://docs.micropython.org/en/latest/rp2/quickref.html)
  * [Pico W Getting Started](https://projects.raspberrypi.org/en/projects/get-started-pico-w)
  * [RP2040 Datasheet](https://github.com/sbcshop/HackyPi-Hardware/blob/main/Documents/rp2040-datasheet.pdf)


## Related Products
   * [ArdiFi](https://shop.sb-components.co.uk/products/ardi32-uno-r3-alternative-board-based-on-esp32-s3-wroom?_pos=6&_sid=90d9cefb0&_ss=r) - Arduino Uno Form factor with latest powerful ESP32 S3
   * [Ardi Relay Shield](https://shop.sb-components.co.uk/products/ardi-relay-shield-for-arduino-uno?_pos=4&_sid=961a5887c&_ss=r) - Relay Shield with Screw terminal and Relay ON/OFF Status LED
   * [Ardi Display Shield](https://shop.sb-components.co.uk/products/ardi-display-shield-for-arduino-uno?_pos=5&_sid=961a5887c&_ss=r) - 2.0" Display Shield with onboard Programmable Buttons and Joystick
   * [Ardi UHF Shield](https://shop.sb-components.co.uk/products/ardi-uhf-shield-for-arduino-uno?variant=40791294836819) - UHF based shield with Oled display and Buzzer onboard
   * [Ardi RFID Shield](https://shop.sb-components.co.uk/products/ardi-rfid-shield-for-arduino-uno?_pos=5&_sid=b4e4b2ef1&_ss=r) - Ardi RFID Shield with onbard Relay and Status LED
   
   Shields are compatible with ArdiPi, Ardi-32 and Other Arduino Uno Compatible boards.

## Product License

This is ***open source*** product. Kindly check LICENSE.md file for more information.

Please contact support@sb-components.co.uk for technical support.
<p align="center">
  <img width="360" height="100" src="https://cdn.shopify.com/s/files/1/1217/2104/files/Logo_sb_component_3.png?v=1666086771&width=300">
</p>
