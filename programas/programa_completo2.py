"""Programa completo da fila 1 para a maqueta domótica. 
Autores: Sasha,Isabely,Leyla,Sara,Carla
Data: 19/05/2025
"""
from microbit import *
import music
import neopixel

#P1 medicion de temperatura

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
