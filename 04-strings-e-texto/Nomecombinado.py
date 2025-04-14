nome1 = input("Digite o primeiro nome: ")
nome2 = input("Digite o segundo nome: ")

meio1 = len(nome1) // 2
meio2 = len(nome2) // 2
novo_nome = nome1[:meio1] + nome2[meio2:]

print(f"O novo nome criado é: {novo_nome}")
