import RPi.GPIO as GPIO
import time
import sys
from hx711 import HX711

# Force Python 3 ###########################################################

if sys.version_info[0] != 3:
    raise Exception("Python 3 is required.")

############################################################################
GPIO.setwarnings(False)

hx = HX711(5, 6)


def cleanAndExit():
    print("Cleaning...")
    GPIO.cleanup()
    print("Bye!")
    sys.exit()


def setup():
    """
    code run once
    """
    #Pasted Offset and Scale I got from calibration..
    hx.set_offset(8608276.3125)
    hx.set_scale(19.828315054835493)


def loop():
    """
    code run continuosly
    """
   
    try:

        val = hx.get_grams()
        print(val)
        hx.power_down()
        time.sleep(0.001)
        hx.power_up()


    except (KeyboardInterrupt, SystemExit):
        cleanAndExit()


##################################

if __name__ == "__main__":

    setup()
    while True:
        loop()