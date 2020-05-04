
from microbit import *
# from random import randint
import neopixel
# Setup the Neopixel strip on pin0 with a length of 3 pixels
np = neopixel.NeoPixel(pin0, 3)

# Define string to hold each bit value for numbers from 0 to 7 for each led
Num_Array = ([0, 0, 0], [0, 0, 1], [0, 1, 0],
             [0, 1, 1], [1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 1])

while True:
# Loop index from 0-7     
    for index in range(0, 7):
        # for pixel_id in range(0, 2):
            for num_index in (Num_Array):
                np[0] = ((num_index[2]) * 50, 0, 0)
                np[1] = ((num_index[1]) * 50, 0, 0)
                np[2] = ((num_index[0]) * 50, 0, 0)
                np.show()
                sleep(1000)
