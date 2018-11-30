from sense_hat import SenseHat
from time import sleep
from time import asctime
from flask import Flask, render_template

# Instantiate senseHAT object
sense = SenseHat()

# Read temperature, humidity and pressure
t = round(sense.get_temperature(),1)
h = round(sense.get_humidity(),1)
p = round(sense.get_pressure(),1)

# Compose message
msg = "Temperature: {} -- Humidity: {} -- Pressure: {}".format(t, h, p)

# Display message on LED matrix
sense.show_message(msg, scroll_speed=0.3)
sense.clear()
    

# Create Flask app and template
app = Flask(__name__)

@app.route('/')
def index():
    now = str(asctime())
    currentWeather = now + " " + msg + "\n"
    weatherData = {
            'weather': currentWeather
            }
    return render_template('index.html', **weatherData)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')


'''
while True:
    # write message to file
    log = open('weather.txt', 'a')
    now = str(asctime())
    log.write(currentWeather)
    print(msg)
    log.close()
    
    sleep(30)
'''

