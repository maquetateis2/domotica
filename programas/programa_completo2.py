"""Programa completo da fila 2 para a maqueta domótica. 
Autores: 
Data: 
"""
from microbit import *
import neopixel

np = neopixel.NeoPixel(pin13, 2)  # 2 LED neopixel conectados ao pin 13

led = pin14 # LED branco conectado ao pin14
np.clear()
while True:
    temperatura = temperature() # gardamos valor da temperatura

    if temperatura > 20:
        np[0] = (0, 255, 0)  # Acender os Neopixel en vermello
        np[1] = (0, 255, 0)
        np.show()  # Mostrar a cor nos neopixel
        led.write_digital(1)  # Acender o LED normal
    else:
        np[0] = (255, 0, 0)  # Apagar os Neopixel
        np[1] = (255, 0, 0)  # Acender os Neopixel en verde
        np.show()  # Mostrar a cor nos neopixel
        led.write_digital(0)  # Apagar o LED normal

    sleep(1000)  # Esperar 1 segundo

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

led = pin14 # conectamos a pin

while True: # facemos que trabaja siempre
    luz = pin1.read_analog() # leemos el balor

    if luz < 700:            # si luz < que 700 es noche 
        led.write_digital(1) # y Led encendemos

    else:                    # en otro caso 
        led.write_digital(0) # lo apagamos

    sleep(100)



