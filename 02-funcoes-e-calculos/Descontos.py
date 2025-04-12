valor_compra = float(input("Digite o valor total da compra (em R$): "))

if valor_compra > 500:
    desconto = 0.25  # 25%
elif valor_compra > 200:
    desconto = 0.15  # 15%
elif valor_compra > 100:
    desconto = 0.10  # 10%
else:
    desconto = 0.00
    
valor_desconto = valor_compra * desconto
valor_final = valor_compra - valor_desconto

print(f"Valor original: R${valor_compra:.2f}")
print(f"Desconto aplicado: {desconto * 100:.0f}%")
print(f"Valor do desconto: R${valor_desconto:.2f}")
print(f"Valor final a pagar: R${valor_final:.2f}")