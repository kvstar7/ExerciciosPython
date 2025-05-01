def calcular_fatorial(n):
    fatorial = 1
    for i in range(1, n + 1):
        fatorial *= i  
    return fatorial

print("Digite números inteiros positivos para calcular o fatorial.")
print("Digite 0 para encerrar.")

while True:
    numero = int(input("Digite um número: "))
    if numero == 0:
        print("Desligando o programa...")
        break
    if numero < 0:
        print("Digite apenas números positivos.")
        continue
    fatorial = calcular_fatorial(numero)
    print(f"O fatorial de {numero} é: {fatorial}")
