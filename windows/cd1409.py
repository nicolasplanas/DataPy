import time
import pyautogui
import pygetwindow as gw

print("Focando na cd1409...")

windows = [w for w in gw.getAllWindows() if "CD1409" in w.title]

window = windows[0]
window.activate() # traz para frente
time.sleep(0.5)

pyautogui.click(window.left + 458, window.top + 184)
time.sleep(0.5)

pyautogui.press("tab", presses=2)
time.sleep(0.5)

pyautogui.write("1") # quantidade
time.sleep(0.5)

#fornecedor
pyautogui.click(window.left + 594, window.top + 400, clicks=2)
time.sleep(0.5)

pyautogui.click(window.left + 571, window.top + 322, clicks=2)
time.sleep(0.5)

pyautogui.press("enter", presses=2)
time.sleep(0.5)

pyautogui.click(window.left + 570, window.top + 431)
time.sleep(0.5)

popUps = [w for w in gw.getAllWindows() if "UMCC0003" in w.title]

popUp = popUps[0]
popUp.activate()
time.sleep(0.5)

pyautogui.write("6317")
time.sleep(0.5)

pyautogui.press("tab")
time.sleep(0.5)

pyautogui.press("space")
time.sleep(0.5)