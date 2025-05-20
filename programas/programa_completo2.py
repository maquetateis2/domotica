"""Programa completo da fila 1 para a maqueta domótica. 
Autores: Sasha, Isabely, Leyla, Sara, Carla
Data: 19/05/2025
"""

from microbit import *      # Importamos todas as funcións necesarias da placa Micro:bit
import music                # Importamos o módulo para melodías
import neopixel             # Importamos o módulo para NeoPixel

rele = pin16                # O relé está conectado ao pin 16
led = pin14                 # Un LED está conectado ao pin 14
pin2.set_analog_period(20)  # O pin 2 para un servo motor
np = neopixel.NeoPixel(pin13, 2)  # NeoPixel conectados ao pin 13

porta = 0                   # Variable para gardar o estado da porta
pin2.write_analog(1)        # porta pechada
np.clear()                  # Apagamos todos os LEDs NeoPixel ao comezo

while True:

# --- P1: Medición de temperatura ---
    temp = temperature()   # Lemos a temperatura
    
    if temp > 20:
        np[0] = (0, 255, 0)    # Verde nos LEDs NeoPixel
        np[1] = (0, 255, 0)
        np.show()             # Actualizamos os LEDs
        rele.write_digital(0) # Apagamos o relé
    else:
        np[0] = (255, 0, 0)    # Vermello nos LEDs NeoPixel
        np[1] = (255, 0, 0)
        np.show()             # Actualizamos os LEDs
        rele.write_digital(1) # Acendemos o relé 

# --- P2: Control de luz ambiente ---
    luz = pin1.read_analog()  # Lemos a luz (sensor LDR)
    
    if luz < 700:             # Se hai pouca luz (de noite)
        led.write_digital(1)  # Encendemos o LED
    else:                     # Se hai luz suficiente (de día)
        led.write_digital(0)  # Apagamos o LED branco

# --- P3: Timbre da casa ---
    if button_a.is_pressed():        # Se se preme o botón A
        for c in range(3):           # Parpadea o LED 3 veces
            led.write_digital(1)
            sleep(500)
            led.write_digital(0)
            sleep(500)

        for c in range(2):           # Reproduce o timbre 2 veces
            music.play(music.RINGTONE)
            sleep(1000)

# --- P4: Control da porta con servo ---
    if button_b.is_pressed():        # Se se preme o botón B
        if porta == 0:               # Se a porta está pechada
            pin2.write_analog(90)    # Abrímosla
            porta = 1                # Actualizamos o estado
        else:                        # Se xa está aberta
            pin2.write_analog(1)     # Pechámosla
            porta = 0                # Actualizamos o estado
            sleep(500)               # Esperamos un pouco para evitar rebotes do botón

# --- P5: Alarma de movemento con sensor PIR ---
    sensor = pin15.read_digital()     # Lemos o estado do sensor (PIR)
    
    if sensor == 1:                   # Se detecta movemento
        music.play(music.RINGTONE)    # Reproducimos un son de alarma
        sleep(500)
        music.play(music.RINGTONE)
        
        for i in range(5):            # Repetimos a alarma 5 veces
            display.show(Image.ANGRY) # Amosamos cara enfadada na pantalla
            np[0] = (0, 255, 0)       # Encendemos os NeoPixel en verde
            np[1] = (0, 255, 0)
            np.show()
            led.write_digital(1)      # Encendemos o LED branco
            sleep(500)
            np[0] = (0, 0, 0)         # Apagamos os NeoPixel
            np[1] = (0, 0, 0)
            np.show()
            led.write_digital(0)      # Apagamos o LED branco
            display.clear()           # Borramos a pantalla
            sleep(500)
    else:
        display.show(Image.HOUSE)     # Se non hai movemento, amosamos unha casa tranquila

    sleep(100)  # Pequena pausa para evitar que o bucle sexa demasiado rápido
