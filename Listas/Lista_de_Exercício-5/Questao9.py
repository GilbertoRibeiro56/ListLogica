v1 = []
v2 = []
v3 = []

for c in range(1,11):
  numero = int(input('Digite um valor para o vetor 1: '))
  v1.append(numero)

for c in range(1,11):
  numero = int(input('Digite um valor para o vetor 2: '))
  v2.append(numero)

c = 0

while c < len(v1):
  v3.append(v1[c])
  v3.append(v2[c])

  c += 1

print(f'Valores intercalados = {v3}')
