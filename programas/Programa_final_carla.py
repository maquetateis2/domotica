"""Programa final da fila 2
Autor: Carla Tresandí
Data: 06/05/2025"""

from microbit import *
import neopixel
import music

np = neopixel.NeoPixel(pin13, 2)  
np.clear()
pin2.write_analog(1)   # La puerta comienza cerrada
pin2.set_analog_period(20)     # Servo coenctado al pin 2
sensor = pin15.read_digital()  # Define o pin 15 como "sensor"
led = pin14   # conectamos a pin
rele = pin16 
c = 0
porta = 0 

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

       
    led = pin14.read_analog() 
    
    if led < 700:             
        led.write_digital(1)

    else:                    
        led.write_digital(0) 
        
    sleep(100)
    
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

if button_b.is_pressed():     # Si el botón b esta presionado
    if porta == 0:
        pin2.write_analog(90)     # Puerta abierta a 90º
        porta = 1
    else:
        pin2.write_analog(1) 
        porta = 0

    if sensor == 1:  
        display.show(Image.ANGRY)    # Mostra unha cara enfadada na pantalla  
        music.play(music.RINGTONE)       # Reproduce un ton de llamada
        sleep(500)     
        music.play(music.RINGTONE)
        
        for i in range(5):               # Repite 5 veceso seguinte bloque
            np[0] = (0, 255, 0)          # Acende o LED NeoPixel en vermello
            np[1] = (0, 255, 0)
            np.show()                    # Mostra o cambio do color no LED
            led.write_digital(1)         # Acende o LED branco conectadoao pin 14
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


  
       
