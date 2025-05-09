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
