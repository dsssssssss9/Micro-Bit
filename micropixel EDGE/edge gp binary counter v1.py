from microbit import *
# from random import randint
# import string
import neopixel
# Setup the Neopixel strip on pin0 with a length of 3 pixels
np = neopixel.NeoPixel(pin0, 3)

# define function to pad number with leading zeros


def zfill(s, width):
    if len(b) < width:
        return ("0" * (width - len(s))) + b
    else:
        return b


for number in range(0, 8):
        b = bin(number)[2:]
        c = zfill(b, 3)
        print(number, b, c)
