#! /usr/bin/env python
import pyautogui as ui
import time
import os
import threading

#Default configs
ui.FAILSAFE = True

#Abrir el panel seleccionado de seguidores o de seguidos
def openPanel(type):
        try:
                x, y = ui.locateOnScreen(type+'.png', confidence=0.5)
                ui.moveTo(x, y, .5)
                ui.click()
                wait(.5)
        except:
                print('No se encuentra la opcion de: '+ type)
                wait(.5)
                openPanel(type)

#Esperar unos segundos
def wait(secs):
        time.sleep(secs)

#Click de seguir a las personas
def clickFollow():
    try:
        x, y = ui.locateCenterOnScreen('follow.png', grayscale=False)
        ui.moveTo(x, y, .5)
        ui.doubleClick()
        wait(.5)
    except:
        print('Scrolling for more Follows')
        ui.scroll(-200, pause=1.)

#Click de dejar de seguir
def clickUnfollow():
    try:
        x, y  = ui.locateCenterOnScreen('following.png', grayscale=False)
        ui.moveTo(x,y,.5)
        ui.click()
        wait(.5)
    except:
        print('Scrolling for more Unfollow')
        ui.scroll(-200, pause=1.)

#Click de confirmar dejar de seguir
def confirmUnfollow():
    try:
        x, y = ui.locateCenterOnScreen('confirmation.png', grayscale=False)
        ui.moveTo(x,y,.5)
        ui.click()
        wait(.5)
    except:
        print('No confirmation popup shown, looking for more unfollows')
        clickUnfollow()


def seguir():
        wait(.5)
        while True:
                print('comenzando nuevo proceso')
                processRestart = threading.Thread(target=restartSeguir)
                processRestart.daemon = True
                processRestart.start()
                time.sleep(.3*60)
        pass

def restartSeguir():
        wait(2)
        ui.hotkey('F5')
        print('Reiniciando pagina')
        wait(1)
        openPanel('seguidores')
        wait(1)
        while True:
                clickFollow()
        pass

def noseguir():
        openPanel('seguidos')
        wait(.5)
        while True:
                clickUnfollow()
                confirmUnfollow()
        pass


result = input('introduzca una opcion [seguir, noseguir] \n ')
period = int(input('Enter the amount of minutes to run \n'))

if result =='seguir':
        process = threading.Thread(target=seguir)
        process.daemon = True
        process.start()
        time.sleep(period*60)
elif result == 'noseguir':
        process = threading.Thread(target=noseguir)
        process.daemon = True
        process.start()
        time.sleep(period*60)
        
            
