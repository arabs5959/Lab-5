GAME!!!

from machine import Pin, I2C
import time
i2c = I2C(1, sda=Pin(14), scl=Pin(15)) #Set up I2C pins
RTC_ADDRESS = 0x68 #Set up RTC address
button = Pin(13, Pin.IN, Pin.PULL_UP) #Sets up the button pin 
log = open("log.txt", "a")

def bcd_to_int(b): return (b >> 4) * 10 + (b & 0x0F)

def read_sec():
    try:
        return bcd_to_int(i2c.readfrom_mem(RTC_ADDRESS, 0x00, 1)[0])
    except OSError:
        print("RTC reads error."); return None #Print error message if RTC read fails

print("Press middle button to start 15s count...") #Gives user instructions

while True: #Just keep everything running 
    while button.value(): 
        start_time = read_sec()
        if start_time is None: continue 
        while button.value(): pass
        end = read_sec()
        if end is None: continue

        t = (end - start) % 60
        z = 15 - t
        
        print("You counted:", t, " seconds.", "You were off by:", 
              abs(z), " seconds.")
        log.write(f"{t}\n"); log.flush()
        print("Press to retry or Ctrl+C to stop")
        while not button.value(): pass
        while button.value(): pass


    log.close(); print("Log saved.")

