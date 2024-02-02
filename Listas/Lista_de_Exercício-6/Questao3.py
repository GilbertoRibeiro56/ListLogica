import random
matriz1 = []
linha1 = 10
coluna1 = 10

for l in range(linha1):
  lin = []
  for c in range(coluna1):
    valor = random.randint(0,99)
    lin.append(valor)
  matriz1.append(lin)
  
print('MATRIZ 1')
for l in range(linha1):
  for c in range(coluna1):
    print(f'[{matriz1[l][c]:02d}] ', end='')
  print()

matriz2 = []
linha2 = 10
coluna2 = 10

for l in range(linha2):
  lin = []
  for c in range(coluna2):
    valor = random.randint(0,99)
    lin.append(valor)
  matriz2.append(lin)

print('MATRIZ 2')
for l in range(linha2):
  for c in range(coluna2):
    print(f'[{matriz2[l][c]:02d}] ', end='')
  print()

matriz3 = []
linha3 = 10
coluna3 = 10
soma = 0

for l in range(linha3):
  lin = []
  for c in range(linha3):
    soma = (matriz1[l][c]) + (matriz2[l][c])
    lin.append(soma)
  matriz3.append(lin)

print('MATRIZ 3')
for l in range(linha3):
  for c in range(linha3):
    print(f'[{matriz3[l][c]:03d}] ', end='')
  print()
