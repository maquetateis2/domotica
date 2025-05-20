"""Programa final da fila 2
Autor: Carla Tresandí
Data: 06/05/2025"""

from microbit import *
import neopixel
import music

np = neopixel.NeoPixel(pin13, 2)  

led = pin14 # conectamos a pin
rele = pin16 
np.clear()
c = 0

while True:
    temp = temperature()

    if temp > 20:
        np[0] = (0, 255, 0)  
        np[1] = (0, 255, 0)
        np.show()  
        rele.write_digital(1)  
    else:
        np[0] = (255, 0, 0)  
        np[1] = (255, 0, 0) 
        np.show()  
        rele.write_digital(0)  

    sleep(1000)  
 
while True: 
    luz = pin14.read_analog() 
    
    if luz < 700:             
        led.write_digital(1)

    else:                    
        led.write_digital(0) 
        
    sleep(100)
    
while True:
    if button_a.is_pressed():
        for c in range(3):
            c = c+1
            led.write_digital(1)
            sleep(500)
            led.write_digital(0)
            sleep(500)

    for c in range(2):
        music.play(music.RINGTONE)
        sleep(1000)
