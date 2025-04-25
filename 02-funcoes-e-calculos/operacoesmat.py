
def adicao(a, b):
 return a + b
def subtracao(a, b):
 return a - b
def multiplicacao(a, b):
 return a * b
def divisao(a, b):
 if b == 0:
   return "Erro: Divisão por zero!"
 return a / b

print("Escolha uma operação:")
print("1. Adição")
print("2. Subtração")
print("3. Multiplicação")
print("4. Divisão")

operacao = input("Digite o número da operação desejada: ")

try:
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    if operacao == "1":
        resultado = adicao(num1, num2)
        print(f"O resultado da adição é: {resultado}")
    elif operacao == "2":
        resultado = subtracao(num1, num2)
        print(f"O resultado da subtração é: {resultado}")
    elif operacao == "3":
        resultado = multiplicacao(num1, num2)
        print(f"O resultado da multiplicação é: {resultado}")
    elif operacao == "4":
        resultado = divisao(num1, num2)
        print(f"O resultado da divisão é: {resultado}")
    else:
        print("Operação inválida!")
except ValueError:
    print("Erro: Por favor, insira números válidos.")
