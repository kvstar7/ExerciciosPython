opcao1 = 0
opcao2 = 0
opcao3 = 0

def votar():
    global opcao1, opcao2, opcao3
    print("Escolha uma das opções abaixo para votar:")
    print("1. Opção A")
    print("2. Opção B")
    print("3. Opção C")
    
    try:
        voto = int(input("Digite o número da sua opção (1, 2 ou 3): "))
        
        if voto == 1:
            opcao1 += 1
        elif voto == 2:
            opcao2 += 1
        elif voto == 3:
            opcao3 += 1
        else:
            print("Opção inválida! Tente novamente.")
            return False
        return True
    except ValueError:
        print("Entrada inválida! Por favor, insira um número inteiro.")
        return False

num_votos = int(input("Quantos votos você quer registrar? "))

for i in range(num_votos):
    print(f"\nVoto {i + 1}:")
    while not votar():
        pass
    
    print("\nResultado final dos votos:")
print(f"Opção A: {opcao1} votos")
print(f"Opção B: {opcao2} votos")
print(f"Opção C: {opcao3} votos")