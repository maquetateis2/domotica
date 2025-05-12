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
