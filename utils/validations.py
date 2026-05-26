import pyautogui
from utils.logger import register_log
from datetime import datetime

def popup_erro_exists():

    popup = pyautogui.locateOnScreen(

        'images/popup_erro.png', 
        confidence=0.8
    )

    return popup is not None

def save_screenshot(name='error'):

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    path = f"{name}_{timestamp}.png"
    pyautogui.screenshot(path)
    register_log(f"Screenshot salva: {path}")