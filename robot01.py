import pyautogui as ui
import time
import os
import threading

#Default configs
ui.FAILSAFE = True

def wait(secs):
    time.sleep(secs)

#Click de seguir a las personas
def clickFollow():
    try:
        x, y = ui.locateCenterOnScreen('follow.png')
        ui.moveTo(x, y, .5)
        ui.doubleClick()
        wait(.5)
    except:
        print('Scrolling for more Follows')
        ui.scroll(-200, pause=1.)

#Click de dejar de seguir
def clickUnfollow():
    try:
        x, y  = ui.locateCenterOnScreen('following.png')
        ui.moveTo(x,y,.5)
        ui.click()
        wait(.5)
    except:
        print('Scrolling for more Unfollow')
        ui.scroll(-200, pause=1.)

#Click de confirmar dejar de seguir
def confirmUnfollow():
    try:
        x, y = ui.locateCenterOnScreen('confirmation.png')
        ui.moveTo(x,y,.5)
        ui.click()
        wait(.5)
    except:
        print('No confirmation popup shown, looking for more unfollows')
        clickUnfollow()

def seguir():
    while True:
        clickFollow()
        pass

def noseguir():
    while True:
        clickUnfollow()
        confirmUnfollow()
        pass


result = input('introduzca una opcion [seguir, noseguir] \n ')
period = int(input('Enter the amount of seconds to run \n'))

if result =='seguir' :
    process = threading.Thread(target=seguir)
    process.daemon = True
    process.start()
    time.sleep(period)
elif result == 'noseguir':
    process = threading.Thread(target=noseguir)
    process.daemon = True
    process.start()
    time.sleep(period)
        
            