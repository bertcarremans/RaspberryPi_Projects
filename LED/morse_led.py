from gpiozero import LED
from time import sleep

# LED connected to GPIO pin 25
led = LED(25)


# Time length for morse signs
# There's a silence lasting exactly as long as a dash, between letters. 
# And, between words, a pause that lasts exactly as long as seven dots.
# More info on : https://www.quora.com/How-do-you-separate-letters-in-Morse-code-How-do-you-separate-words
dot = 0.25
dash = 0.5
between_letters = dash
between_words = 7*dot
between_signs = dot/2

# Morse code for letterss
morse = {
        'A': '.-',     
        'B': '-...',   
        'C': '-.-.', 
        'D': '-..',    
        'E': '.',      
        'F': '..-.',
        'G': '--.',    
        'H': '....',   
        'I': '..',
        'J': '.---',   
        'K': '-.-',    
        'L': '.-..',
        'M': '--',     
        'N': '-.',     
        'O': '---',
        'P': '.--.',   
        'Q': '--.-',   
        'R': '.-.',
        'S': '...',    
        'T': '-',      
        'U': '..-',
        'V': '...-',   
        'W': '.--',    
        'X': '-..-',
        'Y': '-.--',   
        'Z': '--..'
}

for s in '---':
    print(s)

def morse_to_led(letter):
    morse_letter = morse[letter.upper()]
    print('{} in morse : {}'.format(letter, morse_letter))
    for sign in morse_letter:
        print(sign)
        led.on()
        if sign == '.':
            sleep(dot)
        else:
            sleep(dash)
        led.off()
        sleep(between_signs)
        
    
msg = 'Hello World'

words = [w for w in msg.split(" ")]

for word in words:
    print(word)
    for letter in word:
        morse_to_led(letter)
        sleep(between_letters)
    sleep(between_words)

# Releasing PIN 
led.close()
