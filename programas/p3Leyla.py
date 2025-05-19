""" Programa que simula un timbre dunha casa
Autora: Leyla Fernández
Data: 10/5/2025"""

from microbit import *
import music

led = pin14
c = 0

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
