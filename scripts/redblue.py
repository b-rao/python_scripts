#!/usr/bin/env python3

import random
#
# A urn contains red and blue balls
# if a red ball is drawn it is discarded
# if a blue ball is drawn, the next ball
# will be discarded.

runs = 100000

def red_blue():
    red = 80
    blue = 20
    total = 100
    flag = False

    while(total > 1):
        total = red + blue
        redP = red / total
        blueP = blue / total  
        choice = random.random()
        if flag:
            if choice <= redP:
                red -= 1
            else:
                blue -= 1
            total -=1
            flag = False

        elif choice <= redP:  
            red-=1
            total -=1
        else:
            flag = True
            continue  
            
    return True if red > blue else False

r = 0
b = 0
for i in range (runs):
    if red_blue():
        r += 1
    else:
        b += 1
        
print("Times red is last ball:  {}".format(r))
print("Times blue is last ball: {}".format(b))
print("% times red ball is last : {}%".format((r/runs)* 100))
