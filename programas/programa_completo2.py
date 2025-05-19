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


#P2 Control de luz

led = pin14 # conectamos a pin

while True: # facemos que trabaja siempre
    luz = pin1.read_analog() # leemos el balor

    if luz < 700:            # si luz < que 700 es noche 
        led.write_digital(1) # y Led encendemos

    else:                    # en otro caso 
        led.write_digital(0) # lo apagamos

    sleep(100)

#P3  Programa que simula un timbre dunha casa
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



