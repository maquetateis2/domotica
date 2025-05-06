"Programa 2: Control de luz en la casa"
"Autor: Dementiev Oleksasndr"
"Data: 30/04/2025"

from microbit import * # importamos libreria

led = pin14 # conectamos a pin

while True: # para siempre
    luz = pin1.read_analog()

    if luz < 700:
        led.write_digital(1)

    else:
        led.write_digital(0)

    sleep(1000)
