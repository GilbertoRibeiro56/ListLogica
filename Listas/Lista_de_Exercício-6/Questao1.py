import random as aleatorio
matriz = []
linha = 10
coluna = 10
for l in range(linha):
  lin = []
  for c in range(coluna):
    x = aleatorio.random()
    lin.append(x)
  matriz.append(lin)

for l in range(linha):
  for c in range(coluna):
    print(f'[{matriz [l][c]:.2f}]', end='')
  print()

diagonal = []
for l in range(linha):
  for c in range(coluna):
    if l == c:
      valor = matriz[l][c]
      diagonal.append(valor)
      print(diagonal)
      
print()
print('A diagonal principal dessa matriz é:')
for j in range(len(diagonal)):
  print(f'[{diagonal[j]:.2f}] ', end='')
  
