from microbit import *
import neopixel
import music

np = neopixel.NeoPixel(pin13, 2)    # Crea unha tira de 1 LED NeoPixel conectado ao pin 13
led = pin14                         


while True:                          
    sensor = pin15.read_digital()       # Define o pin 15 como "sensor"
    if sensor == 1:                     #Sensor PÎR detecta movemento
        music.play(music.RINGTONE)      # Reproduce un ton de llamada
        sleep(500)     
        music.play(music.RINGTONE)
        
        for i in range(5):               # Se repite 5 veceso seguinte bloque
            display.show(Image.ANGRY)    # Mostra unha cara enfadada na pantalla  
            np[0] = (0, 255, 0)          # Acende o LED NeoPixel en vermello
            np[1] = (0, 255, 0)
            np.show()                    # Mostra o cambio do color no LED
            led.write_digital(1)         
            sleep(500)                   # Espera 500 milisegundos
            np[0] = (0, 0, 0)            # Apaga o LED NeoPixel
            np[1] = (0, 0, 0)
            np.show()                    # Actualiza o estado do LED
            led.write_digital(0)         
            display.clear()              # Borra o que se mostra na pantalla
            sleep(500)
        
    else:                             
        display.show(Image.HOUSE)     # Mostra unha imaxe dunha casa na pantalla
    sleep(100) 
      
