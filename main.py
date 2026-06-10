from utils.excel       import read_excel
from utils.logger      import register_log

from utils.transferência_peças import (

    focus_ce0206,
    fill_request,
)

from utils.validations import (

    popup_erro_exists,
    save_screenshot
)

def execute():

    register_log("Iniciando a automação...")

    requests = read_excel()

    transferencias = carregar_transferencias()

    focus_ce0206()

    for request in requests:

        try:

            fill_request(request)

            if popup_erro_exists():

                register_log(f"Erro encontrado na requisição: {request['requisicao']}")
                save_screenshot(f"erro_{request['requisicao']}")
                continue


            register_log(

                f"Requisição processada com sucesso: {request['requisicao']}"
            )

        except Exception as error:

            register_log(f"Erro ao processar a requisição {request['requisicao']}: {error}")
            save_screenshot(f"erro_{request['requisicao']}")

    register_log("Automação finalizada.")

if __name__ == "__main__":

    execute()