from lib import total

x = float(input('Digite o valor antigo do produto: '))
y = float(input('Digite o valor atual do produto: '))

resultado = total(x,y)

if resultado == 0:
  print('Esse produto não teve aumento no seu preço!!')
else:
  print(f'Esse produto teve {resultado:.1f}% de aumento')
