import cv2
from pyzbar.pyzbar import decode
import RPi.GPIO as GPIO
import time

BuzzerPin = 20
GPIO.setmode(GPIO.BCM)
GPIO.setup(BuzzerPin, GPIO.OUT)
#GPIO.setwarning(false)

global buzz
buzz = GPIO.PWM(BuzzerPin, 440) #instance af buzzer klassen

def barcode_read():
    cam = cv2.VideoCapture(0) #instance af videocapture klassen
    cam.set(3,640) # width is 3 (plads, pixel størrelse) definere størrelsen af billedet den tager
    cam.set(4,480) # Height is 4 (plads, pixel størrelse) definere størrelsen af billedet den tager
    while True:
        success, img = cam.read()
        if not decode(img):
            print("No barcode detected")
            pass
        else:
            buzz.start(10)
            for barcode in decode(img):
                barcode_data = barcode.data.decode('utf-8')
                cam.release()
                cv2.destroyAllWindows()
                print(barcode.data.decode('utf-8'))                #cv2.destroyAllWindows()
                buzz.stop()
                return barcode_data
                #break
                        
    
        cv2.imshow('Result',img)
        cv2.waitKey(1)