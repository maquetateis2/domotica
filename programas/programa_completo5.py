"""Programa 5 da fila 2 para a maqueta domótica. 
Autora: Carla Tresandí Otero
Data: 05/05/2025"""

from microbit import *
import neopixel
import music

np = neopixel.NeoPixel(pin13, 2)    # Crea unha tira de 1 LED NeoPixel conectado ao pin 13
led = pin14                         # Define o pin 14 como "led"
sensor = pin15.read_digital()       # Define o pin 15 como "sensor"

while True:                           # Bucle infinito
    if sensor == 1:                   # Se o sensor PÎR detecta movemento
        music.play(music.RINGTONE)       # Reproduce un ton de llamada
        sleep(500)     
        music.play(music.RINGTONE)
        
        for i in range(5):               # Repite 5 veceso seguinte bloque
            np[0] = (0, 255, 0)          # Acende o LED NeoPixel en vermello
            np[1] = (0, 255, 0)
            np.show()                    # Mostra o cambio do color no LED
            led.write_digital(1)         # Acende o LED branco conectadoao pin 14
            display.show(Image.ANGRY)    # Mostra unha cara enfadada na pantalla da microbit    
            sleep(500)                   # Espera 500 milisegundos
            np[0] = (0, 0, 0)            # Apaga o LED NeoPixel
            np[1] = (0, 0, 0)
            np.show()                    # Actualiza o estado do LED
            led.write_digital(0)         # Apaga o LED branco
            display.clear()              # Borra o que se mostra na pantalla
            sleep(500)
        
    else:                             # Se non detecta movemento
        display.show(Image.HOUSE)     # Mostra unha imaxe dunha casa na pantalla
    sleep(100) 
      
