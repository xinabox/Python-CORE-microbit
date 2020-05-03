from microbit import *

class xCore:
    def __init__(self, freq=100000, scl=pin19, sda=pin20):
        self.i2c = microbit.i2c.init(freq, sda, scl)     

    def write_read(self, addr, reg, length, repeat=False):
        microbit.i2c.write(addr, bytearray([reg]), repeat)
        raw = microbit.i2c.read(addr, length, repeat)
        return raw

    def write_bytes(self, addr, *args, repeat=False):
        microbit.i2c.write(addr, bytes(args), repeat)

    def write(self, addr, buf, repeat=True):
        microbit.i2c.write(addr, buf, repeat)

    def read(self, addr, length, repeat=False):
        raw = microbit.i2c.read(addr, length, repeat)
        return raw

    def sleep(time):
        microbit.sleep(time)
