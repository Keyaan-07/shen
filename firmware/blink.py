from machine import Pin
import time


led = Pin("LED", Pin.OUT)

while 1:
    led.toggle()
    time.sleep(0.5)