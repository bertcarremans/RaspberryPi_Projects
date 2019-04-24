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
import datetime

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

running = True

# Creating log file
file = open('sensor_readings.txt', 'w')
file.write('Time and date, temperature, humidity\n')

# Initialize Firebase app with credentials
cred = credentials.Certificate(cfg.FIREBASE_CREDS_JSON)
firebase_admin.initialize_app(cred)

# Create Firestore object
db = firestore.client()


while running:
    try:
        humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT22, cfg.SENSOR_PIN)
        if humidity is not None and temperature is not None:
            print('Writing data to sensor_readings.txt')
            log_msg = time.strftime('%H:%M:%S %d/%m/%Y') + ',' + str(temperature) + ',' + str(humidity)
            print(log_msg)
            file.write(log_msg + '\n')

            # Sending data to Firebase
            values = {
                u'date' : datetime.datetime.now(),
                u'temperature' : temperature,
                u'humidity' : humidity
            }
            print('Adding data to Firebase.')
            # add method will use auto-generated document ID
            db.collection(u'sensor_readings').add(values)
        else:
            print('No valid sensor readings available')

        # Send data every 15 seconds
        time.sleep(15)
    except KeyboardInterrupt:
        print('Program stopped')
        running = False
        file.close()


'''
Code to read data from Firebase
docs = db.collection(u'sensor_readings').order_by(u'date').limit(3).get()

for doc in docs:
    print()
    print(u'{} => {}'.format(doc.id, doc.to_dict()))
'''