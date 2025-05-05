"""Programa 5 da fila 2 para a maqueta domótica. 
Autor: Carla Tresandí Otero
Data: 05/05/2025
"""

from microbit import *
import neopixel

np = neopixel.neoPixel(pin13, 1)
led_blanco = pin14
sensor_pir = pin15

    for _ in range(5):
        np[0] = (255, 0, 0)
        np.show()
        led_blanco.write_digital(1)
        display.show(Image.ANGRY)
        sleep(500)
        np[0] = (0, 0, 0)
        np.show()
        led_blanco.write_digital(0)
        display.clear()
        sleep(500)
        
while True:
    if sensor_pir.read_digital() == 1:
     music.play(music.RINGTONE)
     sleep(500)
     music.play(music.RINGTONE)()
    else:
        display.show(Image.HOUSE)
    sleep(100)
