from utils import config

import time
import pandas as pd
import pyautogui

pyautogui.FAILSAFE = True

def loading_transfer(sheet):

    df = pd.read_excel(
        "database/DataPy.xlsx",
        sheet_name=sheet,
        dtype={
            "quantidade": str
        }
    )

    return df.to_dict(orient="records")


def cooldown():

    time.sleep(config.delay)

def fill(value, tabs=1):

    pyautogui.write(str(value))
    cooldown()
    pyautogui.press("tab", presses=tabs)
    cooldown()


def amount(value):

    quantity = str(value).replace(".", ",")
    pyautogui.write(quantity)
    cooldown()


def transfer_parts(request):

    print(f"Transferindo peça: {request['item']}")

    fill(request['item'], tabs=2)
    fill(request['dep_origem'], tabs=2)
    fill(request['dep_destino'], tabs=1)
    fill(request['loc_destino'], tabs=2)
    amount(request["quantidade"])

    # Finaliza a transferência
    pyautogui.press("enter")
    cooldown()
    pyautogui.press("enter")


def transfer_truck(request):

    print(f"Transferindo peça: {request['item']}")

    fill(request['item'], tabs=1)
    fill(request['dep_origem'], tabs=1)
    fill(request['loc_origem'], tabs=1)
    fill(request['dep_destino'], tabs=1)
    fill(request['loc_destino'], tabs=1)
    amount(request["quantidade"])

    # Finaliza a transferência
    pyautogui.press("enter")
    cooldown()
    pyautogui.press("enter")