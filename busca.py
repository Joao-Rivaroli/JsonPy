import json
import os
os.system("cls")

arquivo = "pessoas.json"

# cliar uma lista 'pessoas' vazia
pessoas = []

# Verificar se o arquivo json existe
if os.path.exists(arquivo):
    # abrir o arquivo json para leitura
    with open(arquivo, 'r', encoding='utf-8') as f:
        pessoas = json.load(f) # load carrega o arquivo json

    cpf = input("CPF: ")

    encontrado = None

    for pessoa in pessoas:
        if pessoa['cpf'] == cpf:
            encontrado = pessoa
            break

    # Ferifica se encontrou o registro
    if encontrado is not None:
        print("PESSOA ENCONTRADA!")
        print(f'''
        CPF: {pessoa['cpf']}
        Nome: {pessoa['nome']}
        Idade: {pessoa['idade']}
        Salario: {pessoa['salario']}
        ''')
    else:
        print("CPF não encontrado!")
else:
    print("Arquivo não encontrado")
