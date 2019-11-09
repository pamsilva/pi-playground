from time import sleep

from envirophat import leds


def blink(duration):
    leds.on()
    sleep(duration)
    leds.off()


def blinker(duration, n):
    for _ in range(n):
        blink(duration)
        sleep(duration)


if __name__ == '__main__':
    blinker(0.5, 3)
