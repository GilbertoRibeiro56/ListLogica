import random
matriz1 = []
linha1 = 3
coluna1 = 2

print('MATRIZ 1')
for l in range(linha1):
  lin1 = []
  for c in range(coluna1):
    x = random.randint(1,9)
    lin1.append(x)
  matriz1.append(lin1)
  
for l in range(linha1):
  for c in range(coluna1):
    print(f'[{matriz1[l][c]}] ', end='')
  print()



print('MATRIZ 2')
matriz2 = []
linha2 = 2
coluna2 = 4

for l in range(linha2):
  lin2 = []
  for c in range(coluna2):
    x = random.randint(1,9)
    lin2.append(x)
  matriz2.append(lin2)

for l in range(linha2):
  for c in range(coluna2):
    print(f'[{matriz2[l][c]}] ', end='')
  print()



print('MATRIZ FINAL')
matriz3 = []
linha3 = 3
coluna3 = 4

for l in range(linha3):
  lin3 = []
  for c in range(coluna3):
    x = 0
    lin3.append(x)
  matriz3.append(lin3)


for l in range(linha3):
  for c in range(coluna3):
    for q in range(2):
      matriz3[l][c] += matriz1[l][q] * matriz2[q][c]


for l in range(linha3):
  for c in range(coluna3):
    print(f'[{matriz3[l][c]:02d}] ', end='')
  print()
