import os
from unittest import case
import pandas as pd
import time

from utils.logger import register_log
from utils.transfer_parts import (

    focus_ce0206,
    fill_request,
    loading_transfer
)

def clean():

    os.system("cls" if os.name == "nt" else "clear")

def starting_automation():

    clean()
    print("Iniciando a automação em 3 segundos...")
    time.sleep(1)

    clean()
    print("Iniciando a automação em 2 segundos...")
    time.sleep(1)

    clean()
    print("Iniciando a automação em 1 segundo...")
    time.sleep(1)

    clean()

question = input("----- Bem vindo ao DataPy! -----\n\n" \
                 "Escolha uma tarefa:\n" \
                 "1 - Transferência de Peças Guardadas\n" \
                 "2 - Transferência de Materiais\n" \
                 "3 - Relatório de EPI\n" \
                 "4 - RM de EPI\n")

match question:

    case "1":

        clean()
        delay = input("Escolha o tempo entre as ações (padrão: 0.5s): ")

        clean()
        print("Abrindo arquivo do excel para adicionar os dados...")
        time.sleep(1)

        os.startfile("database/DataPy.xlsx")

        clean()
        input("Pressione ENTER quando terminar de editar a planilha...")

        clean()
        input("Ao pressionar ENTER novamente, a automação irá iniciar. Certifique-se de que a janela CE0206 esteja aberta e visível.")

        starting_automation()

        focus_ce0206()
        execute()

    case "2":

        clean()
        delay = input("Escolha o tempo entre as ações (padrão: 0.5s): ")

    case "3":

        clean()
        delay = input("Escolha o tempo entre as ações (padrão: 0.5s): ")

    case "4":

        clean()
        delay = input("Escolha o tempo entre as ações (padrão: 0.5s): ")

def execute():

    register_log("Iniciando a automação em 3 seg...")

    time.sleep(3)

    transfer = loading_transfer()

    # Verificar se a planilha está vazia
    if not transfer:
        raise RuntimeError("A planilha está vazia.")
    
    # Verificar se todas as colunas necessárias estão presentes
    columns = [
        "item", 
        "dep_origem", 
        "dep_destino", 
        "localizacao", 
        "quantidade"
    ]

    if not set(columns).issubset(transfer[0].keys()):
        raise RuntimeError("A planilha não possui todas as colunas necessárias.")

    focus_ce0206()

    total = len(transfer)

    for indice, request in enumerate(transfer, start=1):

        register_log(f"[{indice}/{total}] Processando item {request['item']}")

        try:

            if any(pd.isna(request[column]) for column in columns):
                register_log(f"Item {request['item']} ignorado por conter campos vazios na planilha.")
                continue
            
            fill_request(request)

            time.sleep(1)  # espera a transferência ser processada

            register_log(f"Item {request['item']} transferido com sucesso.")

        except Exception as e:
            part = request.get("item", "DESCONHECIDO")
            register_log(
                f"Erro ao transferir {part}: {e}"
            )

    # Limpa espaços em branco de todas as colunas
    df = df.apply(lambda col: col.str.strip())

    register_log("Automação finalizada.")