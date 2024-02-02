import random
matriz = []
linha = 20
coluna = 20

for l in range(linha):
  lin = []
  for c in range(coluna):
    x = random.randint(1,99)
    lin.append(x)
  matriz.append(lin)

print('MATRIZ PRINCIPAL')
for l in range(linha):
  for c in range(coluna):
    print(f'[{matriz[l][c]:02d}] ', end='')
  print()

print('*'*100)
print('VALORES ABAIXO DA DIAGONAL PRINCIPAL')
print()

contador = 0
for l in range(1,20):
  for c in range(0,1 + contador):
    print(f'[{matriz[l][c]:02d}] ', end='')
  print()
  contador += 1
