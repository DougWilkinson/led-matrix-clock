from sensorclass import Sensor
from ledmatrix import LedMatrix
import font6a
#import font8a
import time
import random

# matrix clock and text view
# Started 10/8/2020

smallfont = LedMatrix(font6a.bitmap,font6a.map,6)
#largefont = LedMatrix(font8a.bitmap,font8a.map,8)

brightness = Sensor("brightness", initval=1)
mode = Sensor("mode", initval='clock')
trans = Sensor("trans", initval='scroll')
speed = Sensor("speed", initval=50)
delay = Sensor("delay", initval=1)
text = Sensor("text", initval="Hello World!!")

def main():
    lastmode = mode.value
    Sensor.MQTTSetup("matrix")
    Sensor.lastminute = 99
    h='??'
    while mode.value != 'halt':
        if text.triggered:
            smallfont.clear()
            smallfont.text(text.value)
            text.triggered = False
            if mode.value != "text":
                lastmode = mode.value
            mode.setvalue("text")
        if smallfont.uptext() and mode.value == 'text':
            mode.setvalue(lastmode)
        if mode.value == 'clock':
            if Sensor.lastminute < 90:
                h = ' ' + str(Sensor.lasthour)
            else:
                Sensor.lastminute += 1
            m = '0' + str(Sensor.lastminute)

            smallfont.show(ord(m[-1]),0,speed.value)
            smallfont.show(ord(m[-2]),1,speed.value)
            smallfont.show(ord(h[-1]),3,speed.value)
            smallfont.show(ord(h[-2]),4,speed.value)
            smallfont.show(58, digit=2, notrans=True)
            time.sleep(delay.value)
        if trans.triggered:
            smallfont.trans = trans.value
            trans.triggered = False
        Sensor.Spin()
