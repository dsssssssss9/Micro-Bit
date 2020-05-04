from microbit import *
import random

Dice1 = Image("00000:"
              "00000:"
              "00900:"
              "00000:"
              "00000")
              
Dice2 = Image("00009:"
              "00000:"
              "00000:"
              "00000:"
              "90000")

Dice3 = Image("00009:"
              "00000:"
              "00900:"
              "00000:"
              "90000")

Dice4 = Image("90009:"
              "00000:"
              "00000:"
              "00000:"
              "90009")

Dice5 = Image("90009:"
              "00000:"
              "00900:"
              "00000:"
              "90009")

Dice6 = Image("90009:"
              "00000:"
              "90009:"
              "00000:"
              "90009")

all_Dice = [Dice1, Dice2, Dice3, Dice4, Dice5, Dice6]

display.scroll("Micro:Bit Dice - Shake for Number ", delay=100, wait=False)

while True:
    gesture = accelerometer.current_gesture()
    if gesture == "shake":
        rnum = (random.randint(1, 6))
        display.show(random.choice(all_Dice))




