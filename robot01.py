import pyautogui as ui
import time
import os

result = input('introduzca una opcion [seguir, noseguir] \n ')

if result =='seguir' :
    #os.chdir('c:\wamp\www')
    madda = True
    
    while madda == True:
        
        seguir = ui.locateCenterOnScreen('follow.png')
        if seguir == None:
            ui.scroll(-200, pause=1.)
            
        if seguir != None:
            x, y = seguir
            ui.moveTo(x,y,.5)
            ui.doubleClick()
elif result == 'noseguir':
    #os.chdir('c:\wamp\www')
    madda = True
    
    while madda == True:
        
        seguir = ui.locateCenterOnScreen('following.png')
        if seguir == None:
            ui.scroll(-200, pause=1.)
        elif seguir != None:
            x, y = seguir
            ui.moveTo(x,y,.5)
            ui.click()
            time.sleep(1)
            confirm = ui.locateCenterOnScreen('confirmation.png')
            print(confirm)
            if confirm != None:
                x, y = confirm
                ui.moveTo(x,y,.5)
                ui.doubleClick()