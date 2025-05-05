"""Programa 4 da fila 2 para a maqueta domótica. 
Autores: Sara Aguado Pedrido
Data: 30/04/2025"""

from microbit import*
 pin2_set_analog_period(20)
 pin2.writte_analog(1)
 servo1 = pin2
 angulos = 1
 
 while True :
     if butto_b.is_pressed():
         angulo +=10
         servo.write_analog(angulo)
         if angulo >= 90:
             angulo = 1
             servo write_analog(angulo)
