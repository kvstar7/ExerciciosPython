n1 = float(input('Digite um numero: '))
n2 = float(input('Digite um numero: '))
print('Qual operação você deseja realizar entre esses números?')

operacao = input('\n (+) - Soma\n(-) - Subtração\n(*) - Multiplicação\n (/) - Divisão: ')
resultado = None

if operacao == '+':
  resultado = n1 + n2
elif operacao == '-':
  resultado = n1 - n2
elif operacao == '*':
  resultado = n1 * n2
elif operacao == '/':
  resultado = n1 / n2
 
if resultado is not None:
  print(f'{n1} {operacao} {n2} = {resultado}')
else:
  print('Operação não permitida')