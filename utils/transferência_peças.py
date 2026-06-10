import pyautogui
import time
import pygetwindow as gw

from utils.logger import register_log

pyautogui.FAILSAFE = True

delay = 0.5

def cooldown():

    time.sleep(delay)

def focus_ce0206():

    register_log("Focando na ce0206...")

    janelas = gw.getWindowsWithTitle("Adicionar nome ce0206")

    if janelas:

        janela = janelas[0]
        janela.activate()  # traz para frente

    else:

        register_log("Janela não encontrada!")
    

def fill_request(request):

    register_log(

        f"Transferindo peça: {request['item']}"
    )

    pyautogui.write(str(request['item']))
    pyautogui.press("tab", presses=2)
    
    cooldown()

    pyautogui.write(str(request['dep_origem']))
    pyautogui.press("tab", presses=2)
    
    cooldown()

    pyautogui.write(str(request['dep_destino']))
    pyautogui.press("tab", presses=1)
    
    cooldown()

    pyautogui.write(str(request['localizacao']))
    pyautogui.press("tab", presses=2)
    
    cooldown()

    pyautogui.write(str(request['quantidade']))
    pyautogui.press("enter", presses=2)
    
    cooldown()

    
    time.sleep(1)