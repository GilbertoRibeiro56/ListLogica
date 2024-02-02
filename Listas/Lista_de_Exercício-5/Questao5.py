import random as ale
tamanho = 50
v1 = []
for c in range(tamanho):
  valor = ale.randint(0,999)
  v1.append(valor)

x = 0
while x < 10:   
  numero = int(input('Digite um número: '))
  c = 0
  found = False

  while c < len(v1):
    if v1[c] == numero:
      found = True
      break
    c += 1
  
  if found:
    print(end='~'*30)
    print()
    print('Existe no Vetor!')
    print(end='~'*30)
    print()
    
  else:
    print(end='~'*30)
    print()
    print('Não Existe no Vetor!')
    print(end='~'*30)
    print()
  x += 1

print(v1)
  
    
