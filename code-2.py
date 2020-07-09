from mcpi.minecraft import Minecraft
from time import sleep
import RPi.GPIO as GPIO
from rpi_ws281x import PixelStrip, Color


mc = Minecraft.create()

class RGB_Matrix:

    def __init__(self):

        # LED strip configuration:
        self.LED_COUNT = 64        # Number of LED pixels.
        self.LED_PIN = 12          # GPIO pin connected to the pixels (18 uses PWM!).
        self.LED_FREQ_HZ = 800000  # LED signal frequency in hertz (usually 800khz)
        self.LED_DMA = 10          # DMA channel to use for generating signal (try 10)
        self.LED_BRIGHTNESS = 10  # Set to 0 for darkest and 255 for brightest
        self.LED_INVERT = False    # True to invert the signal
        self.LED_CHANNEL = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53

    # Define functions which animate LEDs in various ways.
    def clean(self,strip,color):
        # wipe all the LED's at once
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, color)
        strip.show()

    def run(self):
         # Create NeoPixel object with appropriate configuration.
         strip = PixelStrip(
            self.LED_COUNT, 
            self.LED_PIN, 
            self.LED_FREQ_HZ, 
            self.LED_DMA, 
            self.LED_INVERT, 
            self.LED_BRIGHTNESS, 
            self.LED_CHANNEL)
         try:
             return strip
         except KeyboardInterrupt:
             # clean the matrix LED before interruption
             self.clean(strip)

matrixObject =  RGB_Matrix()
strip = matrixObject.run()
strip.begin()
# Rainbow Colors
rainbow_colors = {
    "0":Color(0,0,0), #hei
    "1":Color(128,128,128), #hui 
    "2":Color(0,255,0), #lv
    "3":Color(160,82,45), #huang tu se
    "4":Color(128,128,128), #hui
    "22":Color(0,0,255) #lan se
}

wool_colors = {
    "6":Color(255,105,180), #fen hong
    "5":Color(0,255,0), #lv
    "4":Color(255,255,0), #huang 
    "14":Color(255,0,0), #hong
    "2":Color(255,0,255), #fen hong
    "11":Color(0,0,255),
    "10":Color(255,0,255),
    "0":Color(255,255,255),
    "1":Color(255,127,0)
}

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
    blockType, data = mc.getBlockWithData(x, y-1, z)  # block ID
    print(blockType)
    if blockType == 35:
        # custom wool colors
        matrixObject.clean(strip,wool_colors[str(data)])
    if str(blockType) in rainbow_colors:
        print(rainbow_colors[str(blockType)])
        matrixObject.clean(strip,rainbow_colors[str(blockType)])
    sleep(0.2)
