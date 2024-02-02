v1 = []
v2 = []

for c in range (0,5):
  numero = int(input('Digite um Numero: '))
  v1.append(numero)

c = 4
while c >= 0:
  v2.append(v1[c])
  c -= 1

print(f'Vetor 1 = {v1}')
print(f'Vetor 2 = {v2}')
