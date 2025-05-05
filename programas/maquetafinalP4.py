 from microbit import*
 
 servo1 = pin2
 angulos = 1
 
 while True :
     if butto_b.is_pressed():
         angulo +=10
         servo.write_analog(angulo)
         if angulo >= 90:
             angulo = 1
             servo write_analog(angulo)
