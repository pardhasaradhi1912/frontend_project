import RPi.GPIO as GPIO
import time
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from picamera import PiCamera

GPIO.setmode(GPIO.BCM)
PIR_PIN = 4
GPIO.setup(PIR_PIN, GPIO.IN)

camera = PiCamera()
camera.rotation = 180

def send_email():
    msg = MIMEMultipart()
    msg['From'] = 'pardhasaradhireddy2002@gmail.com'
    msg['To'] = 'dpardha_csb213217@mgit.ac.in'
    msg['Subject'] = 'Motion Detected'
    camera.capture('/home/pi/image.jpg')
    with open('/home/pi/image.jpg', 'rb') as f:
        img = MIMEImage(f.read())
        msg.attach(img)
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login('pardhasaradhireddy2002@gmail.com', '*******')
        server.sendmail('pardhasaradhireddy2002@gmail.com', 'dpardha_csb213217@mgit.ac.in', msg.as_string())

try:
    while True:
        if GPIO.input(PIR_PIN):
            send_email()
            time.sleep(10)
        time.sleep(1)
except KeyboardInterrupt:
    GPIO.cleanup()
