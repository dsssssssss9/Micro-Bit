from microbit import *
while True:
    display.clear()
    for y in range(5):
        for x in range (5):
        
            display.set_pixel(x,y,9)
            display.set_pixel(y,x,9)
            sleep(64)
            
            for bright in range (9,-1,-1):
                display.set_pixel(y,x,bright)
                sleep(32)
            