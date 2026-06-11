import pygetwindow as gw
import pandas      as pd
import pyautogui
import time

from utils.logger import register_log

pyautogui.FAILSAFE = True

delay = 0.5

def cooldown():

    time.sleep(delay)

def carregar_transferencias():

    df = pd.read_excel(
        "database/DataPy.xlsx",
        sheet_name="Transferência de Peças",
        dtype={
            "quantidade": str
        }
    )

    return df.to_dict(orient="records")

def focus_ce0206():

    register_log("Focando na ce0206...")

    janelas = gw.getWindowsWithTitle("06.9.5631 - CE0206 - 2.00.00.023 - Transferência  Depósitos (Modo Clássico) - 15 - UMOE BIOENERGY")

    if not janelas:

        register_log("Janela não encontrada!")
        raise RuntimeError("Janela ce0206 não encontrada.")
    
    janela = janelas[0]
    janela.activate()
    time.sleep(0.5)  # traz para frente

    return janela

def fill_request(request):

    register_log(

        f"Transferindo peça: {request['item']}"
    )

    def preencher(valor, tabs=1):
        pyautogui.write(str(valor))
        pyautogui.press("tab", presses=tabs)
        cooldown()

    preencher(request['item'], tabs=2)

    preencher(request['dep_origem'], tabs=2)

    preencher(request['dep_destino'], tabs=1)

    preencher(request['localizacao'], tabs=2)

    # Finaliza a transferência
    quantidade = str(request["quantidade"]).replace(".", ",")
    pyautogui.write(quantidade)
    pyautogui.press("enter", presses=2)
    
    time.sleep(2)