from sense_hat import SenseHat
from time import asctime
from flask import Flask, render_template

# Instantiate senseHAT object
sense = SenseHat()

# Read temperature, humidity and pressure from SenseHAT
t = round(sense.get_temperature(),1)
h = round(sense.get_humidity(),1)
p = round(sense.get_pressure(),1)

# Compose currentWeather
thp = "Temperature: {} -- Humidity: {} -- Pressure: {}".format(t, h, p)
now = str(asctime())
currentWeather = now + " " + thp + "\n"


# ----------------------------------------
# Create Flask app and template
# ----------------------------------------
app = Flask(__name__)
@app.route('/')
def index():   
    weatherData = {
            'weather': currentWeather
            }
    return render_template('index.html', **weatherData)


# ----------------------------------------
# Display message on LED matrix
# ----------------------------------------
def display_led():
    sense.show_message(thp, scroll_speed=0.3)
    sense.clear()


# ----------------------------------------
# Write to a file
# ----------------------------------------
def write_txt():
    log = open('thp.txt', 'a')
    log.write(currentWeather)
    log.close()
    

if __name__ == '__main__':
    print(currentWeather)
    app.run(debug=True, host='0.0.0.0')
    write_txt()
    display_led()