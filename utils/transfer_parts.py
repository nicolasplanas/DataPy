from utils import config

import time
import pandas as pd
import pyautogui

pyautogui.FAILSAFE = True

def loading_sheet(sheet):

    df = pd.read_excel(
        "database/DataPy.xlsx",
        sheet_name=sheet,
        dtype={
            "quantidade": str
        }
    )

    return df.to_dict(orient="records")


def loading_transfer():

    window = config.ce0206

    x = window.left + 174
    y = window.top  + 198

    pyautogui.moveTo(x, y)
    color = pyautogui.pixel(x, y)
    time.sleep(config.delay)

    if color == (0, 120, 215):

        ...
        
    else:

        loading_transfer()


def cooldown():

    time.sleep(config.delay)


def fill_transfer(value, tabs=1):

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

    fill_transfer(request['dep_origem'], tabs=2)
    fill_transfer(request['item'], tabs=2)
    fill_transfer(request['dep_destino'], tabs=1)
    fill_transfer(request['loc_destino'], tabs=2)
    amount(request["quantidade"])

    # Finaliza a transferência
    pyautogui.press("enter")
    cooldown()
    pyautogui.press("enter")


def transfer_truck(request):

    print(f"Transferindo peça: {request['item']}")

    fill_transfer(request['item'], tabs=2)
    fill_transfer(request['dep_origem'], tabs=1)
    fill_transfer(request['loc_origem'], tabs=1)
    fill_transfer(request['dep_destino'], tabs=1)
    fill_transfer(request['loc_destino'], tabs=2)
    amount(request["quantidade"])

    # Finaliza a transferência
    pyautogui.press("enter")
    cooldown()
    pyautogui.press("enter")