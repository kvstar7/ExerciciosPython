palavra = input("Digite uma palavra: ")
if len(palavra) < 5:
    classificacao = "curta"
else:
    classificacao = "longa"
    
print(f"A palavra '{palavra}' é {classificacao}.")
