import random as ran
matriz = []
linha = 10
coluna = 30

for l in range(linha):
  linha_a = []
  for c in range(coluna):
    x = ran.randint(1,99)
    linha_a.append(x)
  matriz.append(linha_a)

print('MATRIZ PRINCIPAL:')
for l in range(linha):
  for c in range(coluna):
    print(f'[{matriz[l][c]:02d}] ', end='')
  print()
print('**'*75)
print('MATRIZ ADULTERADA')
for c in range(coluna):
  for l in range(5):
    aux = matriz[l][c]
    aux2 = matriz[9-l][c]
    matriz[l][c] = aux2
    matriz[9-l][c] = aux

for l in range(linha):
  for c in range(coluna):
    print(f'[{matriz[l][c]:02d}] ', end='')
  print()
    
    
