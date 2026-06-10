import pyautogui
import time
import pygetwindow as gw

from utils.logger import register_log

pyautogui.FAILSAFE = True

time = 0.5

def cooldown():

    time.sleep(time)

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
    pyautogui.press("tab", "tab")
    
    cooldown()

    pyautogui.write(str(request['Dep 1']))
    pyautogui.press("tab", "tab")
    
    cooldown()

    pyautogui.write(str(request['Dep 2']))
    pyautogui.press("tab")
    
    cooldown()

    pyautogui.write(str(request['Localiz.']))
    pyautogui.press("tab", "tab")
    
    cooldown()

    pyautogui.write(str(request['Quant.']))
    pyautogui.press("enter", "enter")
    
    cooldown()

    
    time.sleep(1)

def confirm():

    register_log("Confirmando operação...")

    pyautogui.press('ctrl', 's')
    time.sleep(2)