from utils.excel       import read_excel
from utils.logger      import register_log

from utils.transferência_peças import (

    focus_ce0206,
    fill_request,
    carregar_transferencias
)

def execute():

    register_log("Iniciando a automação...")

    request = read_excel()

    transferencias = carregar_transferencias()

    focus_ce0206()

    for request in transferencias:
        
        try:
            fill_request(request)
            register_log(f"Item {request['item']} transferido com sucesso.")

        except Exception as e:
            register_log(
                f"Erro ao transferir {request['item']}: {e}"
            )
        continue

    register_log("Automação finalizada.")

if __name__ == "__main__":

    execute()