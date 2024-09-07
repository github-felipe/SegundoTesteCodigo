import json

with open('dados.json', 'r') as arquivo:
        dados = json.load(arquivo)

contador = 0
contadormedia = 0
valoresmedia = 0
for dia in dados:
    dicionario = dados[contador]
    if contador == 0:
        maiorvalor = dicionario['valor']
        menorvalor = dicionario['valor']
        primeiraexecucao = False
    if dicionario['valor'] > 0:
        contadormedia = contadormedia + 1
        valoresmedia = valoresmedia + dicionario['valor']
        media = valoresmedia / contadormedia
    if dicionario['valor'] > maiorvalor:
        maiorvalor = dicionario['valor']
    if dicionario['valor'] < menorvalor:
        menorvalor = dicionario['valor']
    contador = contador + 1
print(f'O Menor valor registrado foi de: {menorvalor}')
print(f'O Maior valor registrado foi de: {maiorvalor}')
print(f'A média dos valores é de: {media}')
