import pandas as pd
import time

from utils.logger import register_log
from utils.transferência_peças import (

    focus_ce0206,
    fill_request,
    carregar_transferencias
)

def execute():

    register_log("Iniciando a automação em 3 seg...")

    time.sleep(3)

    transferencias = carregar_transferencias()

    # Verificar se a planilha está vazia
    if not transferencias:
        raise RuntimeError("A planilha está vazia.")
    
    # Verificar se todas as colunas necessárias estão presentes
    campos = [
        "item", 
        "dep_origem", 
        "dep_destino", 
        "localizacao", 
        "quantidade"
    ]

    if not set(campos).issubset(transferencias[0].keys()):
        raise RuntimeError("A planilha não possui todas as colunas necessárias.")

    focus_ce0206()

    total = len(transferencias)

    for indice, request in enumerate(transferencias, start=1):

        register_log(f"[{indice}/{total}] Processando item {request['item']}")

        try:

            if any(pd.isna(request[campo]) for campo in campos):
                register_log(f"Item {request['item']} ignorado por conter campos vazios na planilha.")
                continue
            
            fill_request(request)

            time.sleep(1)  # espera a transferência ser processada

            register_log(f"Item {request['item']} transferido com sucesso.")

        except Exception as e:
            item = request.get("item", "DESCONHECIDO")
            register_log(
                f"Erro ao transferir {item}: {e}"
            )

    register_log("Automação finalizada.")

if __name__ == "__main__":

    execute()