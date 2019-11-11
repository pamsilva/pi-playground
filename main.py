from time import sleep

from envirophat import leds

MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...',
    'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-',
    'L': '.-..', 'M': '--', 'N': '-.',
    'O': '---', 'P': '.--.', 'Q': '--.-',
    'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--',
    'X': '-..-', 'Y': '-.--', 'Z': '--..',
    '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....',
    '7': '--...', '8': '---..', '9': '----.',
    '0': '-----', ', ': '--..--', '.': '.-.-.-',
    '?': '..--..', '/': '-..-.', '-': '-....-',
    '(': '-.--.', ')': '-.--.-', ' ': ' '
}


def blink(duration):
    leds.on()
    sleep(duration)
    leds.off()


def blinker(duration, n):
    for _ in range(n):
        blink(duration)
        sleep(duration)


def to_morse(text):
    morse_res = [
        MORSE_CODE_DICT[char.upper()]
        for char in text
    ]

    return morse_res


def send_morse_message(message):
    morse_message = to_morse(message)

    for morse_char in morse_message:
        print(f"sending '{morse_char}' in morse")
        for signal in morse_char:

            if signal == '.':
                blink(0.25)

            elif signal == '-':
                blink(0.6)

            else:
                sleep(0.6)

            sleep(0.25)


if __name__ == '__main__':
    # blinker(0.5, 3)
    send_morse_message('this is sparta')
