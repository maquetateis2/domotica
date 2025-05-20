"""Programa completo da fila 1 para a maqueta domótica. 
Autores: Sasha,Isabely,Leyla,Sara,Carla
Data: 19/05/2025
"""
from microbit import *
import music
import neopixel


#P1 Medicion de temperatura

np = neopixel.NeoPixel(pin13, 2)  
rele = pin16 

np.clear()
while True:
    temp = temperature()

    if temp > 20:
        np[0] = (0, 255, 0)  
        np[1] = (0, 255, 0)
        np.show()  
        rele.write_digital(0)  
    else:
        np[0] = (255, 0, 0)  
        np[1] = (255, 0, 0) 
        np.show()  
        rele.write_digital(1)  

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


#P4 iyefgeirhfiurehgfu4ehj
pin2.set_analog_period(20) # Servo coenctado al pin 2
pin2.write_analog(1) #La puerta comienza cerrada
porta = 0 
 
while True :
    if button_b.is_pressed(): #Si el botón b esta presionado
        if porta == 0:
            pin2.write_analog(90) #Puerta abierta a 90º
            porta=1
        else:
            pin2.write_analog(1) 
            porta=0

    sleep(100)



#Programa 5 da fila 2 para a maqueta domótica. 

np = neopixel.NeoPixel(pin13, 2)    # Crea unha tira de 1 LED NeoPixel conectado ao pin 13
led = pin14                         # Define o pin 14 como "led"


while True:                           # Bucle infinito
    sensor = pin15.read_digital()       # Define o pin 15 como "sensor"
    if sensor == 1:                   # Se o sensor PÎR detecta movemento
        music.play(music.RINGTONE)       # Reproduce un ton de llamada
        sleep(500)     
        music.play(music.RINGTONE)
        
        for i in range(5):               # Repite 5 veceso seguinte bloque
            display.show(Image.ANGRY)    # Mostra unha cara enfadada na pantalla da microbit  
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
      

