entrada = input("Digite uma palavra ou frase: ")
entrada = entrada.replace(" ", "").lower()

if entrada == entrada[::-1]:
    print("A entrada é um palíndromo!")
else:
    print("A entrada não é um palíndromo.")