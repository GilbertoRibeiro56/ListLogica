x = float(input('Digite o valor de um lado: '))
y = float(input('Digite o valor de um outro lado: '))
z = float(input('Digite o valor de mais um lado: '))

if (x <= 0) or (y <= 0) or (z <= 0):
  print('Digite valores válidos!!')
  exit()

if (x >= y+z) or (y >= x+z) or (z >= x+y):
  print('Não é possível formar um triângulo com esses valores!!')
  
else:  
  if (x != y ) and (y != z) and (z != x):
    print('Esses lados formam um triângulo escaleno!!')
  
  elif x == y == z:
    print('Esses lados formam um triângulo equilátero!!')

  elif (x != y) or (y != z) or (z != x):
    print('Esses lados formam um triângulo isóceles!!')


