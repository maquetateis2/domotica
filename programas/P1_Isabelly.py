""" Práctica 1 Python Micro:bit. LED Neopixel
Autor: Maria Isabelly Da Silva Cavalcante
Data:05/05/2025
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
