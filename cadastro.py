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

# ler os dados da pessoa
cpf = input("CPF: ")
nome = input("Nome: ")
idade = int(input("Idade: "))
salario = float(input("Salario: "))

existe = False

for pessoa in pessoas:
    # verifica se o cpf existe
    if pessoa["cpf"] == cpf:
        existe = True
        break

if existe:
    print("Cpf já cadastrado!")
else:
    # cria um dicionario com os dados
    pessoa = {
        "cpf": cpf,
        "nome": nome,
        "idade": idade,
        "salario": salario
    }

    # adiciona o dicionario á lista
    pessoas.append(pessoa)

    # abrir o arquivo json para gravação
    with open(arquivo, 'w', encoding='utf-8') as f:
        json.dump(pessoas, f, indent=4, ensure_ascii=False)

    print("Pessoa gravada com sucesso")
