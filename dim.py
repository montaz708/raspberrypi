from gpiozero import PWMLED
from time import sleep
from signal import pause

if __name__ == '__main__':
    led = PWMLED(17)
    led.pulse()
    pause()