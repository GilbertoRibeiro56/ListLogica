print('SIMBOLOS DE OPERAÇÃO POSSÍVEIS','\n','\n+ = SOMA','\n- = SUBTRAÇÃO','\n* = MULTIPLICAÇÃO','\n/ = DIVISÃO','\n** = POTENCIAÇÃO','\n? = RADICIAÇÃO','\n')

a = float(input('Digite um Número: '))

operacao = (input('Digite o simbolo da operação: '))
if operacao == '+':
  b = float(input('Digite outro Número: '))
  total = a + b
  
elif operacao == '-':
  b = float(input('Digite outro Número: '))
  total = a - b
  
elif operacao == '*':
  b = float(input('Digite outro Número: '))
  total = a * b
  
elif operacao == '/':
  b = float(input('Digite outro Número: '))
  total = a / b

elif operacao =='**':
  b = int(input('Digite o valor do Expoente: '))
  total = a**b

elif operacao == '?': #NÃO SOUBE QUE SÍMBOLO COLOCAR PARA REPRESENTAR A RAIZ, POR ISSO OPTEI POR ESSE
  total = (a ** 0.5)

else:
  print('\nOPERAÇÃO INVALIDA!!','\nDIGITE UMA OPERAÇÃO VÁLIDA!!')
  exit()
  
print(f'O Valor da Operação Solicitada é: {total:.1f}')

