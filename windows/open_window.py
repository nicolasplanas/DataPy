import time
import pyautogui
import pygetwindow as gw

def open_window(windows):

    system = gw.getWindowsWithTitle("DATASUL Interactive")

    if not system:

        print("Sistema fechado!!")

    datasul = system[0]
    datasul.activate()
    time.sleep(0.5)

    pyautogui.hotkey("ctrl", "alt", "x")
    time.sleep(0.5)

    pyautogui.write(windows)
    time.sleep(0.5)

    pyautogui.press("enter")
    time.sleep(3)