import pandas as pd
import time

from utils.logger import register_log
from utils.transfer_parts import (

    focus_ce0206,
    fill_request,
    loading_transfer
)

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

if __name__ == "__main__":

    execute()