import pyautogui
import time
import pygetwindow as gw

from utils.logger import register_log

pyautogui.FAILSAFE = True

time = 0.5

def cooldown():

    time.sleep(time)

def focus_cd1409():

    register_log("Focando na cd1409...")

    janelas = gw.getWindowsWithTitle("Adicionar nome cd1409")

    if janelas:

        janela = janelas[0]
        janela.activate()  # traz para frente

    else:

        register_log("Janela não encontrada!")
    

def fill_request(request):

    register_log(

        f"Processando requisição: {request['requisicao']}"
    )

    pyautogui.write(str(request['requisicao']))
    pyautogui.press("enter")
    
    cooldown()

    pyautogui.write(str(request['item']))
    pyautogui.press('tab')

    cooldown()

    pyautogui.write(str(request['quantidade']))
    pyautogui.press('enter')

    cooldown()
    
    pyautogui.write(str(request['funcionario']))
    pyautogui.press('tab')
    
    time.sleep(1)

def confirm():

    register_log("Confirmando operação...")

    pyautogui.press('ctrl', 's')
    time.sleep(2)