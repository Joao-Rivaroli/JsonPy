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

    # verifica se existem registro
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