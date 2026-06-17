import pygetwindow as gw
import pyautogui
import time

print("Selecione a janela, posicione o mouse sobre o local desejado e aguarde 10 segundos...")

time.sleep(10)

window = gw.getActiveWindow()

x, y = pyautogui.position()

color = pyautogui.pixel(x, y)

print(f"Janela ativa: {window.title}")
print(f"Coordenadas capturadas: ({x}, {y})")
print(f"Coordenadas relativas à janela: ({x - window.left}, {y - window.top})")
print(f"Coloração: {color}")