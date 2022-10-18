from m5stack import *
from m5ui import *
from uiflow import *

zMode = 0

lcd.setRotation(3)
# lcd.clear(lcd.GREEN)
# lcd.text(lcd.CENTER, lcd.CENTER, 'Online')
img = M5Img(0, 0, "img/Online.jpg", True)

def buttonA_wasPressed():
    while zMode == 0:
        # lcd.clear(lcd.GREEN)
        # lcd.text(lcd.CENTER, lcd.CENTER, 'Online')
        img = M5Img(0, 0, "img/Online.jpg", True)
        global zMode
        zMode = 1
        wait_ms(2)
        pass
        return
    while zMode == 1:
        # lcd.clear(lcd.RED)
        # lcd.text(lcd.CENTER, lcd.CENTER, 'Unstable')
        img = M5Img(0, 0, "img/Unstable.jpg", True)
        global zMode
        zMode = 2
        wait_ms(2)
        pass
        return
    while zMode == 2:
        # lcd.clear(lcd.GREEN)
        # lcd.text(lcd.CENTER, lcd.CENTER, 'Online')
        img = M5Img(0, 0, "img/Offline.jpg", True)
        global zMode
        zMode = 0
        wait_ms(2)
        pass
        return
btnA.wasPressed(buttonA_wasPressed)