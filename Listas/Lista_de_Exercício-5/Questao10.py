v1 = []
for c in range(0,8):
  numero = int(input('Digite um número: '))
  v1.append(numero)

v2 = []
v3 = []

c = 0
while c < len(v1):
  if v1[c] > 0:
    v2.append(v1[c])

  if v1[c] < 0:
    v3.append(v1[c])
    
  c += 1
if v3 == []:
  print(f'Valores Positivos digitados: {v2}')
  print('Não houve valores negativos.')

if v2 == []:
  print(f'Valores Negativos digitados: {v3}')
  print('Não houve valores positivos')

if v2 != [] and v3 != []:
  print(f'Valores Positivos digitados: {v2}')
  print(f'Valores Negativos digitados: {v3}')
