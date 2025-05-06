"""Programa 4 da fila 2 para a maqueta domótica. 
Autores: Sara Aguado Pedrido
Data: 30/04/2025"""

from microbit import*
 pin2.set_analog_period(20) # Declaramos que e pin 2 es analógico
 pin2.write_analog(1) # Servo a 1º para comenzar coa porta pechada
 pin2.write_analog(90)
 angulos = 0
 
 while True :
     if button_b.is_pressed():
         angulo +=10
         servo.write_analog(angulos)
     if angulo >= 90:
        angulo = 1
        servo write_analog(angulos)
sleep(1000)
