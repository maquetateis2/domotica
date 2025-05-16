"""Programa final da fila 2
Autor: Carla Tresandí
Data: 06/05/2025"""

from microbit import *
import neopixel

np = neopixel.NeoPixel(pin13, 2)  

rele = pin16 
np.clear()
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
