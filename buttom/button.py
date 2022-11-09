import RPi.GPIO as GPIO
from time import sleep
#Set warnings off (optional)
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
#Set Button and LED pins
Button1 = 23
Button2 = 24
#Setup Button and LED
GPIO.setup(Button1,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(Button2,GPIO.IN,pull_up_down=GPIO.PUD_UP)

while True:
    button_state1 = GPIO.input(Button1)
    button_state2 = GPIO.input(Button2)
   # print(button_state)
    if button_state1 == 0:
        print("Hello1")
    if button_state2 == 0:
        print("Hello2")

    sleep(0.1)
