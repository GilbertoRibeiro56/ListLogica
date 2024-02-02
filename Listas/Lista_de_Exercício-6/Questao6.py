import random
matriz = []

for l in range(20):
  linha = []
  for c in range(20):
    valor = random.randint(0,80)
    linha.append(valor)
  matriz.append(linha)

print('MATRIZ')
for i in range(20):
  for j in range(20):
    print(f'[{matriz[i][j]:02d}] ', end= '')
  print()
print('*' * 170)

print('Acima da diagonal principal: ')
for i in range(20):
  for j in range(20):
    if i < j:
      print(f'[{matriz[i][j]:02d}] ', end = '')
print()
print()


print('*' * 170)
print('Acima da diagonal secundária: ')
c = 20
cont = 0
for i in range(20):
  c -=1
  for j in range(c):
    print(f'[{matriz[i][j]:02d}] ', end = '')
    cont += 1
