import Adafruit_DHT
import time


sensor = Adafruit_DHT.DHT22
sensor_pin = 4


running = True

file = open('sensor_readings.txt', 'w')
file.write('Time and date, temperature, humidity\n')


while running:
    try:
        humidity, temperature = Adafruit_DHT.read_retry(sensor, sensor_pin)
        if humidity is not None and temperature is not None:
            print('Writing humidity and temperature')
            file.write(time.strftime('%H:%M:%S %d/%m/%Y') + ',' + str(temperature) + ',' + str(humidity) + '\n')
        else:
            print('No valid measurement available')

        time.sleep(10)
    except KeyboardInterrupt:
        print('Program stopped')
        running = False
        file.close()
        
        
