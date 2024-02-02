v1 = []
for c in range(0,9):
  numero = int(input('Digite um número: '))
  v1.append(numero)

total = 0

for i in range (0,9):
  primo = True
  numero = v1[i]
  for j in range(2, numero):
    if numero % j == 0:
      primo = False
      break

  if (primo == True) and (numero > 1):
    print(f'O número primo {v1[i]} está na {i+1}ª posição.')
