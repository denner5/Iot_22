import drebar
import dbhandler
import RPi.GPIO as GPIO
import time

Button = 16
Pad = 24

GPIO.setmode(GPIO.BCM)
GPIO.setup(Button, GPIO.IN)
GPIO.setup(Pad, GPIO.IN)
#GPIO.setwarnings(False)


def butsta():
    while True:
        if GPIO.input(16) == GPIO.LOW:
            print("trykket")
            dbhandler.dbdata.Stregkode = str(drebar.barcode_read())
            dbhandler.control()
            
        elif GPIO.input(24) == GPIO.LOW:
            print("sletter")
            dbhandler.dbdata.Stregkode = str(drebar.barcode_read())
            dbhandler.delete()
            dbhandler.nulstil_variabler()
            
        else:
            GPIO.input(16) == GPIO.HIGH
            print("ikke trykket")
        time.sleep(0.5)
        
butsta()
# dbhandler.dbdata.Stregkode = "0701197205291"
# dbhandler.delete()