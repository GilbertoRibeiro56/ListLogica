import random
matriz = []
linha = 10
coluna = 20
soma = 0

for l in range(linha):
  lin = []
  for c in range(coluna):
    x = random.randint(0,99)
    lin.append(x)
  matriz.append(lin)

print('MATRIZ PRINCIPAL')
for l in range(linha):
  for c in range(coluna):
    print(f'[{matriz[l][c]:02d}] ', end='')
  print()


print('*'*100)
for l in range(linha):
  y = 0
  for c in range(coluna):
    y += matriz[l][c]
  print(f'A soma dos valores da linha {l} é: {y}')


    
