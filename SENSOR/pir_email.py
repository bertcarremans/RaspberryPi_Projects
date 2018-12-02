from gpiozero import LED, Buzzer, Button, MotionSensor
from signal import pause
import smtplib
from email.mime.text import MIMEText
import email_config

red = LED(18)
buzzer = Buzzer(17)
button = Button(2)
pir = MotionSensor(4)

motion_sensor_status = False
email_sent = False


def arm_motion_sensor():
    global email_sent
    global motion_sensor_status
    if motion_sensor_status == True:
        motion_sensor_status = False
        red.off()
        buzzer.off()
    else:
        motion_sensor_status = True
        email_sent = False
        red.on()

def send_email():
    global email_sent
    global motion_sensor_status
    if (motion_sensor_status == True and email_sent == False):
        body = "Er is beweging gedetecteerd."
        msg = MIMEText(body)
        
        msg['From'] = email_config.from_email_addr
        msg['To'] = email_config.to_email_addr
        msg['Subject'] = 'Bewegingsalarm'
        
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(email_config.from_email_addr, email_config.from_email_password)
        server.sendmail(email_config.from_email_addr, email_config.to_email_addr, msg.as_string())
        server.quit()
        print('Email sent') 
        email_sent = True
        buzzer.beep(n=10)


button.when_pressed = arm_motion_sensor
pir.when_motion = send_email

pause()

#red.close()
#buzzer.close()
#button.close()
#pir.close()