from machine import Pin, I2C
import time 
i2c = I2C(1, sda=Pin(14), scl=Pin(15)) #Set Up I2C Pins
i2c.writeto_mem(0x68, 0x00, b"\x15\x14\x03\x02\x10\x10\x23")
data = i2c.readfrom_mem(0x68, 0x00, )
print(data)
