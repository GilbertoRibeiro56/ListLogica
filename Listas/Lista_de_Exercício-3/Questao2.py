x = int(input('Digite um número: '))

if x % 2 == 0:
  print('Número Par!!')
  if x < 0:
    print('Número negativo!!')
  else:
    print('Número positivo!!')

if x % 2 == 1:
  print('Número impar!!')
  if x < 0:
    print('Número negativo!!')
  else:
    print('Número positivo!!')
