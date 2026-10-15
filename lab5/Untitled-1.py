from machine import Pin, I2C
i2c = I2C(1, sda=Pin(14), scl=Pin(15))
devices = i2c.scan()
for d in devices:
 print("0x{:02x}".format(d))