from utils.transfer_parts import loading_sheet, loading_transfer, transfer_parts, transfer_truck
from windows              import open_window
from utils                import config

import time
import pyautogui
import pandas      as pd
import pygetwindow as gw


def focus_ce0206(delay):

    print("Focando na ce0206...")

    windows = [w for w in gw.getAllWindows() if "CE0206" in w.title]

    if not windows:

        system = gw.getWindowsWithTitle("DATASUL Interactive")

        datasul = system[0]
        datasul.activate()
        time.sleep(0.5)

        pyautogui.hotkey("ctrl", "alt", "x")
        time.sleep(0.5)

        pyautogui.write("CE0206")
        time.sleep(0.5)

        pyautogui.press("enter")
        time.sleep(3)
    
    window = windows[0]
    window.activate()
    time.sleep(delay)  # traz para frente

    x = window.left + 174
    y = window.top  + 198

    pyautogui.moveTo(x, y)
    color = pyautogui.pixel(x, y)
    time.sleep(delay)

    if color == (226, 229, 236):

        pyautogui.click(window.left + 201, window.top + 69)
        time.sleep(delay)
        pyautogui.press("tab", presses=4)
    
    return window


def start_ce0206(question):

    if question == "1":

        transfer = loading_sheet("Transferência de Peças")

    elif question == "2":

        transfer = loading_sheet("Transferência Caminhão Oficina")

    # Verificar se a planilha está vazia
    if not transfer:

        raise RuntimeError("A planilha está vazia.")
    
    # Verificar se todas as colunas necessárias estão presentes

    if  question == "1":

        columns = [
            "item", 
            "dep_origem", 
            "dep_destino", 
            "loc_destino", 
            "quantidade"
        ]

    elif question == "2":

        columns = [
            "item", 
            "dep_origem", 
            "loc_origem", 
            "dep_destino",
            'loc_destino',
            "quantidade"
        ]

    if not set(columns).issubset(transfer[0].keys()):

        raise RuntimeError("A planilha não possui todas as colunas necessárias.")

    total = len(transfer)

    for index, request in enumerate(transfer, start=1):

        print(f"[{index}/{total}] Processando item {request['item']}")

        try:

            if any(pd.isna(request[column]) for column in columns):

                print(f"Item {request['item']} ignorado por conter campos vazios na planilha.")
                continue
            
            if   question == "1":

                transfer_parts(request)

            elif question == "2":

                transfer_truck(request)

            loading_transfer()  # espera a transferência ser processada

            print(f"Item {request['item']} transferido com sucesso.")

        except Exception as e:

            part = request.get("item", "DESCONHECIDO")
            print(f"Erro ao transferir {part}: {e}")

    print("Automação finalizada.")