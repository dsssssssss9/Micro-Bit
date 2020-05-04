# from microbit import *

# import neopixel

Binary_Bits = 16
# Setup the Neopixel strip on pin0 with a length of 3 pixels
# np = neopixel.NeoPixel(pin0, 3)

 #define function to pad number with leading zeros


##def zfill(number, total):
##    if len(number) < total:
##        return ("0" * (total - len(number))) + i
##    else:
##        return i


# Define Function to return Binary Number In string format

def getBin(number, total):
    return bin(number)[2:].zfill(total)


result = [map(int, getBin(i, 4)) for i in range(10)]

#print(result)

Num_Array = []
for i in range(2 ** Binary_Bits):
    n = getBin(i, Binary_Bits)
    Num_Array.append(n)
print(Num_Array)
