from mcpi.minecraft import Minecraft
from time import sleep
import RPi.GPIO as GPIO

mc = Minecraft.create()
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(0)

# Rainbow Colors
WHITE = 0xFFFFFF
RED = 0xFF0000
ORANGE = 0xFF7F00
YELLOW = 0xFFFF00
GREEN = 0x00FF00
CYAN = 0x00FFFF
BLUE = 0x0000FF
PURPLE = 0xFF00FF
MAGENTA = 0xFF0090

# Wool color code
W_WHITE = 0
W_RED = 14
W_ORANGE = 1
W_YELLOW = 4
W_GREEN = 5
W_CYAN = 9
W_BLUE = 11
W_PURPLE = 10
W_MAGENTA = 2

# Wool block ID
WOOL = 35

# Pin numbers
red_pin = 17
green_pin = 18
blue_pin = 27

# Pin setup
GPIO.setup(red_pin, GPIO.OUT, initial=1)
GPIO.setup(green_pin, GPIO.OUT, initial=1)
GPIO.setup(blue_pin, GPIO.OUT, initial=1)

# PWM setup
red = GPIO.PWM(red_pin, 100)
green = GPIO.PWM(green_pin, 100)
blue = GPIO.PWM(blue_pin, 100)
red.start(0)
green.start(0)
blue.start(0)

# Map values from 255 to 100
def map2hundred(value):
    return int(value * 100 / 255)

# Decode color and light it up!
def set_color(color_code):
    # Decode
    red_value =   color_code >> 16 & 0xFF
    green_value = color_code >> 8 & 0xFF
    blue_value =  color_code >> 0 & 0xFF

    # Map values
    red_value = map2hundred(red_value)
    green_value = map2hundred(green_value)
    blue_value = map2hundred(blue_value)


    # Reverse values
    '''red_value = red_value #100 - red_value
    green_value = green_value #100 - green_value
    blue_value = blue_value # 100 - blue_value'''

    # Light up!
    red.ChangeDutyCycle(red_value)
    green.ChangeDutyCycle(green_value)
    blue.ChangeDutyCycle(blue_value)

last_data = 0
try:
    x,y,z = mc.player.getPos()
    mc.setBlocks(x,y,z,x+1,y,z+2,35,14)
    mc.setBlocks(x+2,y+1,z,x+3,y+1,z+2,35,11)
    mc.setBlocks(x+4,y+2,z,x+5,y+2,z+2,35,2)
    mc.setBlocks(x+6,y+3,z,x+7,y+3,z+2,35,5)
    mc.setBlocks(x+8,y+4,z,x+9,y+4,z+2,35,4)
    mc.setBlocks(x+10,y+5,z,x+11,y+5,z+2,35,10)
    mc.setBlocks(x+12,y+6,z,x+13,y+6,z+2,35,1)
    mc.setBlocks(x+14,y+5,z,x+15,y+5,z+2,35,10)
    mc.setBlocks(x+16,y+4,z,x+17,y+4,z+2,35,4)
    mc.setBlocks(x+18,y+3,z,x+19,y+3,z+2,35,5)
    mc.setBlocks(x+20,y+2,z,x+21,y+2,z+2,35,2)
    mc.setBlocks(x+22,y+1,z,x+23,y+1,z+2,35,11)
    mc.setBlocks(x+24,y,z,x+25,y,z+2,35,14)
    while True:
        x, y, z = mc.player.getPos()  # player position (x, y, z)
        block = mc.getBlockWithData(x, y-1, z)  # block ID
        #print(block)
        if block.id == WOOL and last_data != block.data:
            if block.data == W_RED:
                print("Red!")
                set_color(RED)
            if block.data == W_ORANGE:
                print("Orange!")
                set_color(ORANGE)
            if block.data == W_YELLOW:
                print("Yellow!")
                set_color(YELLOW)
            if block.data == W_GREEN:
                print("Green!")
                set_color(GREEN)
            if block.data == W_CYAN:
                print("Cyan!")
                set_color(CYAN)
            if block.data == W_BLUE:
                print("Blue!")
                set_color(BLUE)
            if block.data == W_PURPLE:
                print("Purple!")
                set_color(PURPLE)
            if block.data == W_MAGENTA:
                print("Magenta!")
                set_color(MAGENTA)
            if block.data == W_WHITE:
                print("White!")
                set_color(WHITE)
            last_data = block.data
        sleep(0.05)
except KeyboardInterrupt:
    pass

GPIO.cleanup()

