#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# layout of the word see the .svg file for a printable overlay 
# the svg image will have to be resized to fit on the sense hat
# it was oroginal created for an 8x8 spi led matrix and I don't have a sense hat
#   01234567
# 0 STWENTYS
# 1 FIVEHALF
# 2 FIFTEEN*
# 3 PASTO***
# 4 FIVEIGHT
# 5 SIXTHREE
# 6 TWELEVEN
# 7 FOURNINE
#

import datetime
# if you dont have this hat you can emulate it on your pi comment out if your using the hat
# from sense_emu import SenseHat
# if you have a sense hat use the line below comment out if you emulate
from sense_hat import SenseHat
from random import randint

def getadd(minute):  # make an additive of 4 or less to add to the five minutes displayed
    while 5:
        if minute > 5:
            minute -= 5
        else:
            break
    additive = minute
    return additive

def randomizer():
    value = randint(1, 255)
    return value
    
def pixel(x,y):
    # create random colors for each pixel
    red = randomizer()
    green = randomizer()
    blue = randomizer()
    hat = SenseHat()
    # if you want a single color set the rgb components in the color variable
    color = (red, green, blue)    
    hat.set_pixel(x, y, color)
    

def face(hour, minute): # draw the face according to the current time
    # clear the rgb matrix
    hat = SenseHat()
    hat.clear()
    # to the new hour or passing the old hour
    if minute > 0 and minute < 31: #past
        # print('past')
        pixel(0, 3)            
        pixel(0, 3)
        pixel(1, 3)
        pixel(2, 3)
        pixel(3, 3)
    if minute > 30 and minute < 60:  # to
        # print('to')
        pixel(3, 3)
        pixel(4, 3)
        hour += 1
    if hour > 12:
        hour -= 12
    # display five minute increments for minutes
    if minute > 4 and minute < 10  or minute < 30 and minute > 24 or minute < 36 and \
           minute > 30 or minute > 50 and minute < 56:
        pixel(0,1)
        pixel(1,1)
        pixel(2,1)
        pixel(3,1)
        # print('five')
    if minute < 15 and minute > 9 or minute < 51 and minute > 45:
        pixel(1,0)
        pixel(3,0)
        pixel(4,0)
        # print('ten')
    if minute < 20 and minute > 14 or minute < 46 and minute > 40:
        pixel(0,2)
        pixel(1,2)
        pixel(2,2)
        pixel(3,2)
        pixel(4,2)
        pixel(5,2)
        pixel(6,2)
        # print('fifteen')
    if minute < 30 and minute > 19 or minute < 41 and minute > 30:
        pixel(1,0)
        pixel(2,0)
        pixel(3,0)
        pixel(4,0)
        pixel(5,0)
        pixel(6,0)
        # print('twenty')
    if minute < 31 and minute > 29:
        pixel(4,1)
        pixel(5,1)
        pixel(6,1)
        pixel(7,1)
        # print('half')
    # display the hour in munbers
    if hour == 1:  # one
        pixel(1,7)
        pixel(4,7)
        pixel(7,7)
    if hour == 2:  # two
        pixel(0,6)
        pixel(1,6)
        pixel(1,7)
    if hour == 3:  # three
        pixel(3,5)
        pixel(4,5)
        pixel(5,5)
        pixel(6,5)
        pixel(7,5)
    if hour == 4:  # four
        pixel(0,7)
        pixel(1,7)
        pixel(2,7)
        pixel(3,7)
    if hour == 5:  # five
        pixel(0,4)
        pixel(1,4)
        pixel(2,4)
        pixel(3,4)
    if hour == 6:  # six
        pixel(0,5)
        pixel(1,5)
        pixel(2,5)
    if hour == 7:  # seven
        pixel(0,5)
        pixel(4,6)
        pixel(5,6)
        pixel(6,6)
        pixel(7,6)
    if hour == 8:  # eight
        pixel(3,4)
        pixel(4,4)
        pixel(5,4)
        pixel(6,4)
        pixel(7,4)
    if hour == 9:  # nine
        pixel(4,7)
        pixel(5,7)
        pixel(6,7)
        pixel(7,7)
    if hour == 10:  # ten
        pixel(7,4)
        pixel(7,5)
        pixel(7,6)
    if hour == 11:  # eleven
        pixel(2,6)
        pixel(3,6)
        pixel(4,6)
        pixel(5,6)
        pixel(6,6)
        pixel(7,6)
    if hour == 12:  # twelve
        pixel(0,6)
        pixel(1,6)
        pixel(2,6)
        pixel(3,6)
        pixel(5,6)
        pixel(6,6)

    # fine tune the minutes
    # light up the astericks 
    additive = getadd(minute)
    if additive < 5:
        !
        if additive == 1:
            if minute < 31:
                pixel(5,3)
            elif minute > 30:
                pixel(5,3)
                pixel(6,3)
                pixel(7,3)
                pixel(7,2)
        if additive == 2:
            if minute < 31:
                pixel(5,3)
                pixel(6,3)
            elif minute > 30:
                pixel(5,3)
                pixel(6,3)
                pixel(7,3)
        if additive == 3:
            if minute < 31:
                pixel(5,3)
                pixel(6,3)
                pixel(7,3)
            elif minute > 30:
                pixel(5,3)
                pixel(6,3)
        if additive == 4:
            if minute < 31:
                pixel(5,3)
                pixel(6,3)
                pixel(7,3)
                pixel(7,2)
            elif minute > 30:
                pixel(5,3)
    # set up the next minute and pass it back 
    newminute = minute + 1
    if newminute == 60:
        newminute = 0
    return newminute

def main():
    # draw the first clock face
    now = datetime.datetime.now()
    hour = now.hour
    minute = now.minute
    newminute = face(hour, minute)
    
    while True:
        # if it a new minute then re-draw the face
        now = datetime.datetime.now()
        hour = now.hour
        minute = now.minute
        if minute == newminute:
            newminute = face(hour, minute)
        else:
            pass

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        hat = SenseHat()
        hat.clear()
        pass
    
