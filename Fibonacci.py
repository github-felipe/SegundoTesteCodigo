print("Bem Vindo(a) ao verificador de sequência de fibonacci!")
NumVerificar = int(input("Digite o número que você quer verificar se pertence a sequência(Precisa ser inteiro): "))

NumFibonacci = 0
NumAnterior = 1

while True:
    if NumFibonacci == NumVerificar:
        print(f"O número {NumVerificar} Pertence a sequência de fibonacci!")
        break
    elif NumFibonacci < NumVerificar:
        NumAtual = int(NumFibonacci)
        NumFibonacci = NumFibonacci + NumAnterior
        NumAnterior = int(NumAtual)
    else:
        print(f"O número {NumVerificar} não pertence a sequência de fibonacci!")
        break
