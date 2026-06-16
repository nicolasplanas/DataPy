from utils.transfer_parts import loading_transfer, transfer_parts, transfer_truck

import time
import pyautogui
import pandas      as pd
import pygetwindow as gw

def focus_ce0206(delay):

    print("Focando na ce0206...")

    windows = gw.getWindowsWithTitle("06.9.5631 - CE0206 - 2.00.00.023 - Transferência  Depósitos (Modo Clássico) - 15 - UMOE BIOENERGY")

    if not windows:

        print("Janela não encontrada!")
        raise RuntimeError("Janela ce0206 não encontrada.")
    
    window = windows[0]
    window.activate()
    time.sleep(0.5)  # traz para frente

    x = window.left + 174
    y = window.top  + 198

    pyautogui.moveTo(x, y)
    time.sleep(delay)
    color = pyautogui.pixel(x, y)

    if color == (226, 229, 236):

        pyautogui.click(197, 69)
        time.sleep(delay)
        pyautogui.press("tab", presses=4)
    
    return window


def start_ce0206(question):

    if question == "1":

        transfer = loading_transfer("Transferência de Peças")

    elif question == "2":

        transfer = loading_transfer("Transferência Caminhão Oficina")

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

    for indice, request in enumerate(transfer, start=1):

        print(f"[{indice}/{total}] Processando item {request['item']}")

        try:

            if any(pd.isna(request[column]) for column in columns):

                print(f"Item {request['item']} ignorado por conter campos vazios na planilha.")
                continue
            
            if   question == "1":

                transfer_parts(request)

            elif question == "2":

                transfer_truck(request)

            time.sleep(1)  # espera a transferência ser processada

            print(f"Item {request['item']} transferido com sucesso.")

        except Exception as e:

            part = request.get("item", "DESCONHECIDO")
            print(f"Erro ao transferir {part}: {e}")

    print("Automação finalizada.")