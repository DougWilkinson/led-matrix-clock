import random
import time

def flydigit(self, speed=0, bits=2, minval=2):
    unclear = True
    left = 255
    while unclear:
        unclear = False
        pixels = 0
        for p in range(256):
            if self.led[p] != self.bg:
                pixels += 1
                unclear = True
                px = int(p/8)
                py = (p % 8)
                if px % 2 == 1:
                    py = 7-py
                if random.getrandbits(3) <= py or left < 10:
                    px = px - min(random.getrandbits(bits),minval)
                    py = py + min(random.getrandbits(bits),minval)
                if px > 0 and py < 8:
                    if px % 2 == 1:
                        newp = px*8+(7-py)
                    else:
                        newp = px*8+py
                    if self.led[newp] == self.bg:
                        self.led[newp] = (7-py,0,0)
                        self.led[p] = self.bg
                else:
                    self.led[p] = self.bg
        self.led.write()
        time.sleep_ms(speed)
        left = pixels

