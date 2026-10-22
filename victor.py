import os
import json

def gravacao_json(arquivo: str, pessoas : list) -> None:
    with open(arquivo, 'w', encoding = 'utf-8') as f:
        json.dump(pessoas, f, indent = 4, ensure_ascii = False)
        print("Pessoa gravada com sucesso")

def carregar_arquivo(arquivo: str, pessoa: list) -> list:
    with open(arquivo, 'r', encoding = 'utf-8') as f:
        return json.load(f) 

def verificar_id(id_jogador: str, pessoas: list) -> bool:
    for pessoa in pessoas:
        if pessoa["id_jogador"] == id_jogador:
            return True
    return False

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
            arquivo = "jogadores.json"
            jogadores = []
            if os.path.exists(arquivo):
                jogadores = carregar_arquivo(arquivo, jogadores)
            
                id_jogador = input("id: ")
                nickname = input("Nickname: ")
                horas_jogadas = int(input("Horas jogadas: "))
                dinheiro_gasto = float(input("Dinheiro gasto: "))


                if verificar_id(id_jogador, pessoas):
                    print("Jogador já existente")
                else:
                    jogador = {
                        "id_jogador": id_jogador,
                        "nickname": nickname,
                        "horas_jogadas": horas_jogadas,
                        "dinheiro_gasto" : dinheiro_gasto
                    }

                    jogadores.append(jogador)
                    gravacao_json(arquivo, jogadores)

        case 2:
            if os.path.exists(arquivo):
                # abrir o arquivo json para leitura
                with open(arquivo, 'r', encoding='utf-8') as f:
                    pessoas = json.load(f) # load carrega o arquivo json
                    
                if len(pessoas) == 0:
                    print("Nenhuma pessoa cadastrada!")
                else:
                    print("====== PESSOAS CADASTRADAS ======")
                    print(f"{'CPF':12} | {'NOME':25} | {'IDADE':6} | {'SALÁRIO':9}")
                    print(60 * '-')
                    for pessoa in pessoas:
                        print(f"{pessoa['cpf']:12} | {pessoa['nome']:25} | {pessoa['idade']:6d} | {pessoa['salario']:9.2f}")
            else:
                print("Arquivo não existe!")            
        case 3:
            break
        case 4:
            break
        case 5:
            break
