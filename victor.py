import os
import json

os.system("cls")
def gravacao_json(arquivo: str, jogadores: list) -> None:
    with open(arquivo, "w", encoding="utf-8") as f:
        json.dump(jogadores, f, indent=4, ensure_ascii=False)


def carregar_arquivo(arquivo: str) -> list:
    with open(arquivo, "r", encoding="utf-8") as f:
        return json.load(f)


def verificar_id(id_jogador: str, jogadores: list) -> bool:
    for jogador in jogadores:
        if jogador["id_jogador"] == id_jogador:
            return True
    return False


def buscar_jogador(id_jogador: str, jogadores: list) -> dict:
    for jogador in jogadores:
        if jogador["id_jogador"] == id_jogador:
            return jogador
    return None


def cadastrar_jogador(id_jogador: int, nickname: str, horas_jogadas: int, dinheiro_gasto: float) -> dict:
    jogador = {
        "id_jogador": id_jogador,
        "nickname": nickname,
        "horas_jogadas": horas_jogadas,
        "dinheiro_gasto": dinheiro_gasto
    }

    return jogador


arquivo = "jogadores.json"
jogadores = []

if os.path.exists(arquivo):
    jogadores = carregar_arquivo(arquivo)


while True:
    print("""
    0 - Sair
    1 - Cadastrar
    2 - Listar
    3 - Buscar
    4 - Editar
    5 - Excluir
    """)
    escolha = int(input("Escolha: "))

    match escolha:
        case 0:
            print("Saindo...")
            break

        case 1:
            id_jogador = input("ID: ")

            if id_jogador == "":
                print("O ID não pode ficar vazio!")

            elif verificar_id(id_jogador, jogadores):
                print("Jogador já existente!")

            else:
                nickname = input("Nickname: ")
                horas_jogadas = int(input("Horas jogadas: "))
                dinheiro_gasto = float(input("Dinheiro gasto: "))

                jogador = cadastrar_jogador(id_jogador, nickname, horas_jogadas, dinheiro_gasto)
                jogadores.append(jogador)
                gravacao_json(arquivo, jogadores)

                print("Jogador cadastrado com sucesso!")
        case 2:
            if len(jogadores) == 0:
                print("Nenhum jogador cadastrado!")

            else:
                print("========== JOGADORES CADASTRADOS ==========")
                print(
                    f"{'ID':12} | {'NICKNAME':20} | "
                    f"{'HORAS':10} | {'DINHEIRO':12}"
                )
                print(65 * "-")

                for jogador in jogadores:
                    print(
                        f"{jogador['id_jogador']:12} | "
                        f"{jogador['nickname']:20} | "
                        f"{jogador['horas_jogadas']:10d} | "
                        f"{jogador['dinheiro_gasto']:12.2f}"
                    )
        case 3:
            id_jogador = input("Digite o ID: ")

            jogador = buscar_jogador(id_jogador, jogadores)

            if jogador is not None:
                print("JOGADOR ENCONTRADO!")
                print(f"""
                        ID: {jogador['id_jogador']}
                        Nickname: {jogador['nickname']}
                        Horas jogadas: {jogador['horas_jogadas']}
                        Dinheiro gasto: R$ {jogador['dinheiro_gasto']:.2f}
                    """)
            else:
                print("ID não encontrado!")

        case 4:
            id_jogador = input("Digite o ID do jogador: ")
            jogador = buscar_jogador(id_jogador, jogadores)

            if jogador is not None:

                print("JOGADOR ENCONTRADO!")
                print(f"""
                        ID: {jogador['id_jogador']}
                        Nickname: {jogador['nickname']}
                        Horas jogadas: {jogador['horas_jogadas']}
                        Dinheiro gasto: R$ {jogador['dinheiro_gasto']:.2f}
                    """)

                print("Digite os novos dados:")

                jogador["nickname"] = input("Novo nickname: ")
                jogador["horas_jogadas"] = int(input("Novas horas jogadas: "))
                jogador["dinheiro_gasto"] = float(input("Novo dinheiro gasto: "))
                gravacao_json(arquivo, jogadores)
                print("Jogador editado com sucesso!")

            else:
                print("ID não encontrado!")

        case 5:
            id_jogador = input("Digite o ID do jogador: ")
            jogador = buscar_jogador(id_jogador, jogadores)

            if jogador is not None:
                print("JOGADOR ENCONTRADO!")
                print(f"""
                        ID: {jogador['id_jogador']}
                        Nickname: {jogador['nickname']}
                        Horas jogadas: {jogador['horas_jogadas']}
                        Dinheiro gasto: R$ {jogador['dinheiro_gasto']:.2f}
                    """)
                confirmacao = input("Deseja realmente excluir? (S/N): ")

                if confirmacao == "S" or confirmacao == "s":
                    jogadores.remove(jogador)
                    gravacao_json(arquivo, jogadores)
                    print("Jogador excluído com sucesso!")
                else:
                    print("Exclusão cancelada!")
            else:
                print("ID não encontrado!")
                
        case _:
            print("Opção inválida!")
