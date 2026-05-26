import pyautogui
import time

from utils.logger import register_log

pyautogui.FAILSAFE = True

time = 0.5

def cooldown():

    time.sleep(time)

def focus_datasul():

    register_log("Focando o Datasul...")

    # ALT + TAB para focar o Datasul
    pyautogui.hotkey("alt", "tab")
    cooldown()

def open_cd1409():

    register_log("Abrindo tela CD1409...")

    pyautogui.hotkey("ctrl","alt", "e")
    cooldown()

    pyautogui.write("cd1409")
    pyautogui.press("enter")

    time.sleep(3)

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