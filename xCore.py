from microbit import *

class xCore:
    def __init__(self, freq=100000, scl=pin19, sda=pin20):
        self.i2c = i2c.init(freq, sda, scl)     

    def write_read(self, addr, reg, length, repeat=False):
        i2c.write(addr, bytearray([reg]), repeat)
        raw = i2c.read(addr, length, repeat)
        return raw

    def write_bytes(self, addr, *args, repeat=False):
        i2c.write(addr, bytes(args), repeat)

    def write(self, addr, buf, repeat=True):
        i2c.write(addr, buf, repeat)

    def read(self, addr, length, repeat=False):
        raw = i2c.read(addr, length, repeat)
        return raw
    
    def sleep(time):
        sleep(time)
