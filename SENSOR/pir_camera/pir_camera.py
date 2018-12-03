from gpiozero import Button, MotionSensor
from picamera import PiCamera
from time import sleep
from signal import pause
import sys
sys.path.append('..')
import email_config
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart


button = Button(2)
pir = MotionSensor(4)
camera = PiCamera()

camera.start_preview()


i = 0

def stop_camera():
    camera.stop_preview()
    exit()
    
def send_email(ImgFileName):
    img_data = open(ImgFileName, 'rb').read()
    msg = MIMEMultipart()
    msg['From'] = email_config.from_email_addr
    msg['To'] = email_config.to_email_addr
    msg['Subject'] = 'Bewegingsalarm'
    body = MIMEText('Er is beweging gedetecteerd.')
    msg.attach(body)
    image = MIMEImage(img_data, name=ImgFileName)
    msg.attach(image)   
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(email_config.from_email_addr, email_config.from_email_password)
    server.sendmail(email_config.from_email_addr, email_config.to_email_addr, msg.as_string())
    server.quit()
    print('Email sent') 

    
def take_photo():
    global i
    i = i + 1
    ImgFileName = '/home/pi/Projecten/SENSOR/pir_camera/image_%s.jpg' % i
    camera.capture(ImgFileName)
    print('Photo taken')
    send_email(ImgFileName)
    sleep(10)


button.when_pressed = stop_camera
pir.when_motion = take_photo

pause()