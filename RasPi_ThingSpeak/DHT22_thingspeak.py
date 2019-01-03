# --------------------------------------
#           Air Quality Logger
#  Read data from a a set of sensors
#  and send to Thingspeak.com.
#
# Author : Bert Carremans
# Date   : 03/01/2018
# --------------------------------------

import Adafruit_DHT
import time
import config as cfg
import urllib3
import json

running = True

# Creating log file
file = open('sensor_readings.txt', 'w')
file.write('Time and date, temperature, humidity\n')


while running:
    try:
        humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT22, cfg.SENSOR_PIN)
        if humidity is not None and temperature is not None:
            print('Writing data to sensor_readings.txt')
            log_msg = time.strftime('%H:%M:%S %d/%m/%Y') + ',' + str(temperature) + ',' + str(humidity)
            print(log_msg)
            file.write(log_msg + '\n')

            # Preparing data for ThingSpeak Channel
            values = { 'api_key' : cfg.API_KEY,
                        'field1' : temperature,
                        'field2' : humidity
            }
            # JSON encoding
            encoded_body = json.dumps(values).encode('utf-8')

            print('Sending data to ThingSpeak.')
            http = urllib3.PoolManager()
            try:
                http.request('POST'
                            , cfg.THINGSPEAK_UPDATE_URL
                            , headers={'Content-Type': 'application/json'}
                            , body=encoded_body
                            , timeout=5.0)
            except urllib3.exceptions.NewConnectionError:
                print('Connection failed.')
            except urllib3.exceptions.HTTPError:
                print('ThingSpeak server could not fulfill request.')
            except:
                print('Unknown error.')


        else:
            print('No valid sensor readings available')

        # ThingSpeak Free account allows to send data every 15 seconds
        time.sleep(15)
    except KeyboardInterrupt:
        print('Program stopped')
        running = False
        file.close()
        
        
