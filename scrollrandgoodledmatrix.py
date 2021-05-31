from machine import Pin
from neopixel import NeoPixel
import time
import random

ledpin = Pin(14, Pin.OUT)
numled = 8 * 32


class LedMatrix:
    
    from flydigit import flydigit
    fg = (0,1,1)
    bg = (0,0,0)
    scrollbuff = [(0,0,0)]*8
    lcs = [32,32,32,32,32]
    trans = "random"

    def __init__(self, fontbitmap, ledmap, width):
        self.width = width
        self.maxdigits = int(32/width)
        self.font = fontbitmap
        self.map = ledmap
        self.led = NeoPixel(ledpin, numled)
        self.clear()

    def clear(self):
        for i in range(numled):
            self.led[i] = self.bg 
        self.led.write()
        self.lcs = [32,32,32,32,32]

    def show(self,newnum=32, digit=0, speed=50):
        if self.trans == "scroll":
            r=1
            for i in range(8):
                self.display(ordnum=newnum,digit=digit, digitrow=7-r, displayrow=0, refresh=False)
                if i < 7:
                    self.display(ordnum=self.lcs[digit],digit=digit, displayrow=r+1)
                time.sleep_ms(speed)
                r += 1
                if r > 7:
                    r=0
            self.display(ordnum=newnum, digit=digit, displayrow=1)

        if self.trans == "random":
            if newnum != 32:
                for d in range(5):
                    self.display(ordnum=48+random.getrandbits(8) % 9,digit=digit)
                    time.sleep_ms(speed)
            self.display(ordnum=newnum,digit=digit)
  
    def display(self, ordnum=32, digit=0, displayrow=1, digitrow=0, refresh=True ):
        #displayrow can be negative
        columns = self.width
        achar = self.font[ordnum]
        for x in range(columns):
            for y in range(digitrow, 8-displayrow):
                if ( achar[x] & 1 << y):
                    self.led[(digit*8*columns) + self.map[y + displayrow - digitrow + (x*8)]] = self.fg
                if not ( achar[x] & 1 << y):
                    self.led[(digit*8*columns) + self.map[y + displayrow - digitrow + (x*8)]] = self.bg
        if refresh:
            self.led.write()
            self.lcs[digit] = ordnum

