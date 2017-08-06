from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

yellow = (255, 255, 0)
blue = (0, 0, 255)

message = "Astro Pi is Awesome"

speed = 0.05

while True:
    sense.clear()
    sleep(5)
    sense.show_message(message, speed, text_colour=yellow, back_colour=blue)
