"""Programa final da fila 2
Autor: Carla Tresandí
Data: 06/05/2025"""

from microbit import *
import neopixel

np = neopixel.NeoPixel(pin13, 2)  # 2 LED neopixel conectados ao pin 13
led = pin14     # LED branco conectado ao pin 14
luz = pin1.read_analog()     # Sensor de luz conecrtado ao pin 1
np.clear()

while True:
    temperatura = temperature()    # gardamos valor da temperatura

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

while True:    # facemos que trabaja siempre
       
    if luz < 700:              # Si luz < que 700 es noche 
        led.write_digital(1)   # Encedemos o LED

    else:                     
        led.write_digital(0)   # Apagamos o LED

    sleep(1000)
