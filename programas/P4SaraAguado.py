"""Programa 4 da fila 2 para a maqueta domótica. 
Autora: Sara Aguado Pedrido
Data: 30/04/2025"""

from microbit import*

pin2.set_analog_period(20) # Servo coenctado al pin 2
pin2.write_analog(1) 
porta = 0 
 
while True :
    if button_b.is_pressed():
        if porta == 0:
            pin2.write_analog(90)
            porta=1
        else:
            pin2.write_analog(1)
            porta=0

    sleep(100)
       
        
        
         
       
