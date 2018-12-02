# Source: 20 Easy Raspberry Pi Projects - Rui Santos & Sara Santos - No Starch Press

from sense_hat import SenseHat
from tkinter import *
from tkinter import ttk

# Instantiate senseHAT object
sense = SenseHat()

# Read temperature, humidity and pressure from SenseHAT
t = round(sense.get_temperature(),1)
h = round(sense.get_humidity(),1)
p = round(sense.get_pressure(),1)

# ----------------------------------------
# Display in window
# ----------------------------------------
window = Tk()
window.title('SenseHAT Measurements')
window.geometry('200x480')

h_label = Label(window, text='Humidity', font=('Helvetica',18), pady=3)
h_label.pack()
humidity = StringVar()
h_value = Label(window, textvariable=humidity, font=('Courier',20), fg='blue', anchor=N, width=200)
h_value.pack()
h_canvas = Canvas(window, width=200, height=200)
h_canvas.pack()
h_bar = DoubleVar()
pbar_h = ttk.Progressbar(h_canvas, variable=h_bar, orient=VERTICAL, length=200, maximum=100)
pbar_h.pack(fill=X, expand=1)

t_label = Label(window, text='Temperature', font = ('Helvetica', 18), anchor=S, width=200, height=2)
t_label.pack()
temperature = StringVar()
t_value = Label(window, textvariable = temperature, font = ('Courier', 20), fg='red', anchor=N, width=200)
t_value.pack()

p_label = Label(window, text='Pressure', font = ('Helvetica', 18), anchor=S, width=200, height=2)
p_label.pack()
pressure = StringVar()
p_value = Label(window, textvariable = pressure, font=('Courier', 20), fg='green', anchor=N, width=200)
p_value.pack()

def update_readings():
    humidity.set(str(h) + ' %')
    h_bar.set(h)
    temperature.set(str(t) + ' C')
    pressure.set(str(p) + ' hPa')
    window.update_idletasks()
    window.after(3000, update_readings)
    
update_readings()
window.mainloop()
