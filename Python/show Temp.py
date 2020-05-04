from microbit import *

display.scroll("Space The Final Frontier", delay = 64)

t1 = 0

while True:
    t1 = str(temperature())

    display.scroll("Temp = " + t1, delay = 100)
