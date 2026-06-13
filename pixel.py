import pygetwindow as gw
import pyautogui
import time

from utils.transfer_parts import focus_ce0206

print("Selecione a janela, posicione o mouse sobre o local desejado e aguarde 5 segundos...")

time.sleep(5)

window = gw.getActiveWindow()

x, y = pyautogui.position()

print(f"Janela ativa: {window.title}")
print(f"Coordenadas capturadas: ({x}, {y})")
print(f"Coordenadas relativas à janela: ({x - window.left}, {y - window.top})")