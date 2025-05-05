"Programa 2: Control de luz en la casa"
"Autor: Dementiev Oleksasndr"
"Data: 30/04/2025"

from microbit import *

led = pin14

while True:
    luz = pin1.read_analog()

    if luz < 700:
        led.write_digital(1)

    else:
        led.write_digital(0)

    sleep(1000)
