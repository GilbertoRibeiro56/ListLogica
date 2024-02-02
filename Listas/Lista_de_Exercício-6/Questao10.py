import random
matriz = []
print('MATRIZ')

for l in range (5):
  linha = []
  for c in range(5):
    x = random.randint(1,25)
    linha.append(x)
  matriz.append(linha)

for l in range (5):
  for c in range(5):
    print(f'[{matriz[l][c]:02d}] ', end='')
  print()

print('*' * 150)
print('MATRIZ INVERTIDA')
for l in range (5):
  for c in range(5):
    print(f'[{matriz[c][l]:02d}] ', end='')
  print()
