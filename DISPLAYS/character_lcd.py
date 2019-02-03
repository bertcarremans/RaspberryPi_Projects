import Adafruit_CharLCD as LCD
from time import sleep

# GPIO configuration
lcd_rs = 27
lcd_en = 22
lcd_d4 = 25
lcd_d5 = 24
lcd_d6 = 23
lcd_d7 = 18
lcd_backlight = 4

# LCD size: 16 columns and 2 rows
lcd_columns = 16
lcd_rows = 2

# initialize the LCD
lcd = LCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, lcd_columns, lcd_rows, lcd_backlight)


# messages
title = "Don't forget!"
reminder = "You have an appointment at the doctor."

# set delay time
delay = 0.3

lcd.clear()  # clear screen
lcd.home()  # set cursor to first column on the first row
lcd.message(title)  # display the static message

def scroll_text(reminder, delay):
    padding = ' ' * lcd_columns  # add padding for a whole row to start with an empty row
    reminder_msg = padding + reminder + ' '

    for i in range(len(reminder_msg)):
        lcd.set_cursor(0,1)
        lcd.message(reminder_msg[i:i+lcd_columns])
        sleep(delay)

while True:
    scroll_text(reminder, delay)
