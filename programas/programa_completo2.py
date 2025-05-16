"""Programa completo da fila 1 para a maqueta domótica. 
Autores: Isabelly, Sara Aguado, Leyla y Tresandí
Data: 16/05/2025
"""
""" Práctica 1 Python Micro:bit. LED Neopixel
Autor: Maria Isabelly Da Silva Cavalcante
Data:05/05/2025
"""
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

"""Programa 2: Control de luz en la casa
Autor: Dementiev Oleksasndr
Data: 30/04/2025"""

from microbit import * # importamos libreria

led = pin14 # conectamos a pin

while True: # facemos que trabaja siempre
    luz = pin1.read_analog() # leemos el balor

    if luz < 700:            # si luz < que 700 es noche 
        led.write_digital(1) # y Led encendemos

    else:                    # en otro caso 
        led.write_digital(0) # lo apagamos

    sleep(100)


