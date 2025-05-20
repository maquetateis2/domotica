"""Programa completo da fila 1 para a maqueta domótica. 
Autores: Isabelly, Sasha, Sara Aguado, Leyla y Tresandí
Data: 16/05/2025
"""
# importamos librerias 
from microbit import *
import neopixel
import music

# --- Configuración de pines e variables ---
np = neopixel.NeoPixel(pin13, 2)  # LED NeoPixel
rele = pin16                      # Relé
led = pin14                       # LED branco
porta = 0                         # Estado da porta
pin2.set_analog_period(20)        # Servo motor
pin2.write_analog(26)             # Pechamos a porta inicialmente

np.clear() # Apagamos todos os LEDs NeoPixel ao comezo
np.show()
 
while True:
 
    # 1. Control de temperatura: luces e relé

    temp = temperature()  # Le a temperatura ambiente en ºC

    if temp > 20:
        # Se a temperatura é maior de 20ºC, acendemos LEDs verdes e activamos o relé
        np[0] = (0, 255, 0)  
        np[1] = (0, 255, 0)
        rele.write_digital(1)  # Activamos o relé (por exemplo, un ventilador)
    else:
        # Se a temperatura é 20ºC ou menor, acendemos LEDs vermellos e apagamos o relé
        np[0] = (255, 0, 0)
        np[1] = (255, 0, 0)
        rele.write_digital(0)

    np.show()  # Actualizamos os LEDs NeoPixel

    # 2. Control de luz segundo a luminosidade
    luz = pin1.read_analog()  # Le a luminosidade do sensor conectado ao pin 1

    if luz < 700:             # Se a luminosidade é baixa (é de noite)
        led.write_digital(1)  # Acende o LED branco
    else:                     # Se hai luz suficiente
        led.write_digital(0)  # Apaga o LED branco

    # 3. Simulación de timbre de casa co botón A
    if button_a.is_pressed():  # Se se preme o botón A
        for _ in range(3):     # Repite 3 veces o parpadeo do LED
            led.write_digital(1)
            sleep(500)
            led.write_digital(0)
            sleep(500)

        for _ in range(2):     # Reproduce o ton de timbre dúas veces
            music.play(music.RINGTONE)
            sleep(1000)

    # 4. Apertura e peche da porta co botón B
    if button_b.is_pressed():     # Se se preme o botón B
        if porta == 0:            # Se a porta está pechada
            pin2.write_analog(77) # Abrimos a porta a ~90º
            porta = 1
        else:                     # Se está aberta
            pin2.write_analog(26) # Pechamos a porta (~0º)
            porta = 0
        sleep(500)  # Pequena pausa para evitar rebotes no botón

    # Programa 5: Alarma con sensor de movemento PIR
    sensor = pin15.read_digital()       # Define o pin 15 como "sensor"
    if sensor == 1:                   # Se o sensor PIR detecta movemento
        music.play(music.RINGTONE)       # Reproduce un ton de chamada
        sleep(500)     
        music.play(music.RINGTONE)
        
        for i in range(5):               # Repite 5 veces o seguinte bloque
            display.show(Image.ANGRY)    # Mostra unha cara enfadada na pantalla da microbit  
            np[0] = (255, 0, 0)          # Acende o LED NeoPixel en vermello
            np[1] = (255, 0, 0)
            np.show()                    # Mostra o cambio do color no LED
            led.write_digital(1)         # Acende o LED branco conectado ao pin 14
            sleep(500)                   # Espera 500 milisegundos
            np[0] = (0, 0, 0)            # Apaga o LED NeoPixel
            np[1] = (0, 0, 0)
            np.show()                    # Actualiza o estado do LED
            led.write_digital(0)         # Apaga o LED branco
            display.clear()              # Borra o que se mostra na pantalla
            sleep(500)
        
    else:                             # Se non detecta movemento
        display.show(Image.HOUSE)     # Mostra unha imaxe dunha casa na pantalla


    
       
