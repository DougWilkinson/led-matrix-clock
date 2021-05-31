from sensorclass import Sensor
from ledmatrix import LedMatrix
import font6a
#import font8a
import time
import random

# fob - halloween costume for Emelia
# Started 10/8/2020

smallfont = LedMatrix(font6a.bitmap,font6a.map,6)
#largefont = LedMatrix(font8a.bitmap,font8a.map,8)

def randomdigit(digit, font=smallfont, row=1, minmax=(48,57)):
    font.display(minmax[0]+random.getrandbits(8) % (minmax[1] - minmax[0]),digit, displayrow=row)
    
def randisp(count=1000, font=smallfont, startrow=1, minmax=(48,57)):
    font.clear()
    for i in range(count):
        for digit in range(font.maxdigits):
            font.display(minmax[0]+random.getrandbits(8) % (minmax[1] - minmax[0]),digit)

def fobdisplay(font=smallfont):
    font.clear()
    for i in range(font.maxdigits):
        for d in range(5):
            randomdigit(i, font=font)

brightness = Sensor("brightness", initval=1)
mode = Sensor("mode", initval='clock')

def main(delay=1,speed=50):
    Sensor.MQTTSetup("fob")
    cc = 58
    Sensor.lastminute = 99
    h='??'
    lh='  '
    lm='  '
    while mode.value != 'reset':
        if mode.value == 'clock':
            if Sensor.lastminute < 90:
                h = ' ' + str(Sensor.lasthour)
            else:
                Sensor.lastminute += 1
            m = '0' + str(Sensor.lastminute)

            smallfont.scrolldigit(num=ord(lm[-1]),newnum=ord(m[-1]),digit=0,speed=speed)
            smallfont.scrolldigit(num=ord(lm[-2]),newnum=ord(m[-2]),digit=1,speed=speed)
            smallfont.scrolldigit(num=ord(lh[-1]),newnum=ord(h[-1]),digit=3,speed=speed)
            smallfont.scrolldigit(num=ord(lh[-2]),newnum=ord(h[-2]),digit=4,speed=speed)
            smallfont.doscroll = True
            smallfont.display(58, digit=2)
            lh=h
            lm=m
            time.sleep(delay)
        if mode.value == 'fob':
            fobdisplay()
            time.sleep(delay)
        Sensor.Spin()
