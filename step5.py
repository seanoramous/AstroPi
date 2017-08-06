from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

red = (255, 0, 0)
yellow = (255, 255, 0)
blue = (0, 0, 255)
green = (0, 255, 0)
black = (0, 0, 0)
white = (255, 255, 255)

sense.show_letter("O", red)
sleep(1)
sense.show_letter("M", blue)
sleep(1)
sense.show_letter("G", green)
sleep(1)
sense.show_letter("!", black, white)
sleep(1)
sense.clear()
