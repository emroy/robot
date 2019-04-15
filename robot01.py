import pyautogui as ui
import time
import os

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
        wait(1)
    except:
        print('Scrolling for more Follows')
        ui.scroll(-200, pause=1.)

#Click de dejar de seguir
def clickUnfollow():
    try:
        x, y  = ui.locateCenterOnScreen('following.png')
        ui.moveTo(x,y,.5)
        ui.click()
        wait(1)
    except:
        print('Scrolling for more Unfollow')
        ui.scroll(-200, pause=1.)

#Click de confirmar dejar de seguir
def confirmUnfollow():
    try:
        x, y = ui.locateCenterOnScreen('confirmation.png')
        ui.moveTo(x,y,.5)
        ui.click()
        wait(1)
    except:
        print('No confirmation popup shown, looking for more unfollows')
        clickUnfollow()


result = input('introduzca una opcion [seguir, noseguir] \n ')


if result =='seguir' :
    while True:
        clickFollow()
elif result == 'noseguir':
    while True:
        clickUnfollow()
        confirmUnfollow()
            