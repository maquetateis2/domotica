"""Programa completo da fila 1 para a maqueta domótica. 
Autores: Isabelly, Sasha, Leyla, Sara.A, Carla.
Data: 9/05/2025
"""


from microbit import *
import neopixel

temp = temperature()
np = neopixel.NeoPixel(pin13,2)
np.clear()
while True:
   if temp> 24:
     np[0]= (0, 255, 0)
     np[1]= (0, 255, 0)
     np.show()
     pin16.write_digital(1)


   elif 20<=temp:
     np[0]= (0, 0, 255)
     np[1]= (0, 0, 255)
     pin16.write_digital(0)
     np.clear()

   elif temp>20 and temp<=22:
     np[0]= (255, 0, 0)
     np[1]= (255, 0, 0)
     pin16.write_digital(0)
     np.clear()

   elif temp>22 and temp<=24:
     np[0]= (255, 165, 0)
     np[1]= (255, 165, 0)
     pin16.write_digital(0)
     np.clear()
   else:
     np[0]= (0, 0, 0)
     np[1]= (0, 0, 0)
     pin16.write_digital(0)
     np.clear()

sleep(1000)


led = pin14 # conectamos a pin

while True: # facemos que trabaja siempre
    luz = pin1.read_analog() # leemos el balor

    if luz < 700:            # si luz < que 700 es noche 
        led.write_digital(1) # y Led encendemos

    else:                    # en otro caso 
        led.write_digital(0) # lo apagamos

    sleep(1000)

servo1 = pin2
 angulos = 0
 
 while True :
     if butto_b.is_pressed():
         angulo +=10
         servo.write_analog(angulo)
         if angulo >= 90:
             angulo = 0
             servo write_analog(angulo)

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
