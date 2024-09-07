texto = str(input('Qual texto você deseja inverter? '))
textoinvertido = str()
for letra in texto:
    textoinvertido = letra + textoinvertido
print('O texto inserido foi:')
print(texto)
print('O texto invertido é:')
print(textoinvertido)
