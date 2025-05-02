def gerar_pa(primeiro_termo, razao, quantidade_termos):
    termos = [primeiro_termo]  
    
    for i in range(1, quantidade_termos):
        proximo_termo = termos[i - 1] + razao  
        termos.append(proximo_termo)  
    
    return termos

print("Digite dois números inteiros:")

primeiro_termo = int(input("Digite o primeiro número: "))
razao = int(input("Digite a razão da PA: "))
quantidade_termos = int(input("Quantoas casinhas você quer na PA? "))

pa = gerar_pa(primeiro_termo, razao, quantidade_termos)

print("\nA Progressão Aritmética gerada é:")
print(pa)
