from open_window import open_window

import time
import pyautogui
import pygetwindow as gw

print("Focando na ce0206...")

windows = [w for w in gw.getAllWindows() if "ESST0596" in w.title]

if not windows:

    open_window(windows="esst0596")

    windows = [w for w in gw.getAllWindows() if "ESST0596" in w.title]

    if not windows:

        print("Não foi possivel abrir")

    window = windows[0]
    window.activate() # traz para frente
    time.sleep(0.5)

    pyautogui.click(window.left + 65, window.top + 49)
    time.sleep(0.5)

    pyautogui.click(window.left + 375, window.top + 236)
    time.sleep(0.5)

    pyautogui.hotkey("ctrl", "a")
    time.sleep(0.5)
    pyautogui.hotkey("ctrl", "c")
    time.sleep(0.5)

    pyautogui.click(window.left + 202, window.top + 239)

    pyautogui.hotkey("ctrl", "a")
    time.sleep(0.5)
    pyautogui.hotkey("ctrl", "v")
    time.sleep(0.5)

    pyautogui.click(window.left + 174, window.top + 53)

window = windows[0]
window.activate() # traz para frente
time.sleep(0.5)

pyautogui.click(window.left + 200, window.top + 157)
time.sleep(0.5)
pyautogui.hotkey("ctrl", "a")
time.sleep(0.5)

pyautogui.write("7454")
time.sleep(0.5)

pyautogui.press("tab")
time.sleep(0.5)

pyautogui.click(window.left + 292, window.top + 54)
time.sleep(0.5)

pyautogui.click(window.left + 407, window.top + 55)
time.sleep(0.5)

pyautogui.click(window.left + 206, window.top + 123)
time.sleep(0.5)

pyautogui.click(window.left + 518, window.top + 150)
time.sleep(0.5)

popUps = [w for w in gw.getAllWindows() if "UT-IMPR" in w.title]

popUp = popUps[0]
popUp.activate()

pyautogui.click(popUp.left + 96, popUp.top + 174)
time.sleep(0.5)

pyautogui.click(popUp.left + 45, popUp.top + 308)
time.sleep(0.5)

pyautogui.click(window.left + 56, window.top + 365)
time.sleep(2)

pyautogui.click(window.left + 194, window.top + 57)
time.sleep(0.5)