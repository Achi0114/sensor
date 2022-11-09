import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
from time import sleep
state = 1
print("Hello")
back = 16
next = 18
ch = 0
def welcome(channel):
    ch = channel
    print(state,channel)
    if state == 1 and channel == next:
       print(state,ch)
       connect_wifi()
       return

    if state == 1 and channel == back:
       print("Hello")
       return

    if state == 2 and channel == next:
       get_sensor()
       return

    if state == 2 and channel == back:
       connect_wifi()
       return

    if state == 3 and channel == back:
       get_sensor()
       return


    if state == 3 and channel == next:
       print("Finish")
       return


def connect_wifi():
    global state
    state = 2
    sleep(1)
    print("ConnectWIFI")
    print(state,ch)

def get_sensor():
    global state
    state = 3
    sleep(1)
    print("Please re-measure")
    print(state,ch)


GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Set pin 10 to be an input pin and set initial value to be pulled low (off)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)

GPIO.add_event_detect(16,GPIO.RISING,callback=welcome) # Setup event on pin 10 rising edge
GPIO.add_event_detect(18,GPIO.RISING,callback=welcome)


message = input("Press enter to quit\n\n") # Run until someone presses enter

GPIO.cleanup() # Clean up
