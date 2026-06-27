from windows.ce0206 import focus_ce0206, start_ce0206
from utils.excel    import open_spreadsheet
from utils          import config

import os
import time


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

clean()
question = input("\n----- Bem vindo ao DataPy! -----\n\n" \
                 "Escolha uma tarefa:\n" \
                 "1 - Transferência de Peças Guardadas\n" \
                 "2 - Transferência de Caminhão Oficina\n" \
                 "3 - Relatório de EPI\n" \
                 "4 - Baixar RM de EPI\n" \
                 "R:")

match question:

    case "1":

        clean()
        config.delay = float(input("Escolha o tempo entre as ações (padrão: 0.5s): ") or 0.5)

        clean()
        print("Abrindo arquivo do excel para adicionar os dados...")
        time.sleep(1)

        open_spreadsheet("Transferência Caminhão Oficina")

        clean()
        input("Pressione ENTER quando terminar de editar a planilha...")

        clean()
        input("Ao pressionar ENTER novamente, a automação irá iniciar. Certifique-se de que a janela CE0206 esteja aberta e visível.")

        starting_automation()

        focus_ce0206(config.delay)
        # start_ce0206(question)

    case "2":

        clean()
        config.delay = float(input("Escolha o tempo entre as ações (padrão: 0.5s): ") or 0.5)

        clean()
        print("Abrindo arquivo do excel para adicionar os dados...")
        time.sleep(1)

        open_spreadsheet("Transferência de Peças")

        clean()
        input("Pressione ENTER quando terminar de editar a planilha...")

        clean()
        input("Ao pressionar ENTER novamente, a automação irá iniciar. Certifique-se de que a janela CE0206 esteja aberta e visível.")

        starting_automation()

        focus_ce0206(config.delay, config.ce0206)
        start_ce0206(question)

    case "3":

        clean()
        config.delay = float(input("Escolha o tempo entre as ações (padrão: 0.5s): ") or 0.5)

    case "4":

        clean()
        config.delay = float(input("Escolha o tempo entre as ações (padrão: 0.5s): ") or 0.5)