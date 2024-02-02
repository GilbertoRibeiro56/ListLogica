import random
matriz1 = []
linha1 = 10
coluna1 = 10

for l in range(linha1):
  linha = []
  for c in range(coluna1):
    x = random.randint(10,99)
    linha.append(x)
  matriz1.append(linha)

print('MATRIZ ORIGINAL')
for l in range(linha1):
  for c in range(coluna1):
    print(f'[{matriz1[l][c]:02d}] ', end='')
  print()

matriz2 = []
linha2 = 10
coluna2 = 10
div = 0

for l in range(linha2):
  linha = []
  for c in range(coluna2):
      div = (matriz1[l][c]) / matriz1[l][l]
      linha.append(div)
  matriz2.append(linha)

print('*'*70)
print('MATRIZ RESULTADO')
for l in range(linha2):
  for c in range(coluna2):
    print(f'[{matriz2[l][c]:.1f}] ', end='')
  print()
