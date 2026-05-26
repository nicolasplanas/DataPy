from utils.excel       import read_excel
from utils.logger      import register_log

from utils.datasul     import (

    focus_datasul, 
    open_cd1409, 
    fill_request, 
    confirm
)

from utils.validations import (

    popup_erro_exists,
    save_screenshot
)

def execute():

    register_log("Iniciando a automação...")

    requests = read_excel()

    focus_datasul()

    open_cd1409()

    for request in requests:

        try:

            fill_request(request)

            if popup_erro_exists():

                register_log(f"Erro encontrado na requisição: {request['requisicao']}")
                save_screenshot(f"erro_{request['requisicao']}")
                continue

            confirm()

            register_log(

                f"Requisição processada com sucesso: {request['requisicao']}"
            )

        except Exception as error:

            register_log(f"Erro ao processar a requisição {request['requisicao']}: {error}")
            save_screenshot(f"erro_{request['requisicao']}")

    register_log("Automação finalizada.")

if __name__ == "__main__":

    execute()