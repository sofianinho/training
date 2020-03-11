#!/usr/bin/env python3

# This code shows an example where you can use python
# with pyFirmata to control your Arduino Uno. You 
# should first load the 'StandardFirmata' program
# in your Arduino uno and install pyfirmata

import pyfirmata
import time

LED_PIN = 13
LED_HIGH = 1
LED_LOW = 0
loop = 0

print("Loading the Arduino board")
board = pyfirmata.Arduino('/dev/ttyACM0')

try:
    while True:
        print("Turn On")
        board.digital[LED_PIN].write(LED_HIGH)
        time.sleep(2)
        print("Turn Off")
        board.digital[LED_PIN].write(LED_LOW)
        time.sleep(2)
        loop = loop + 1
        print(f"looped {loop}")
except KeyboardInterrupt:
    board.digital[LED_PIN].write(LED_LOW)
    print("Goodbye")