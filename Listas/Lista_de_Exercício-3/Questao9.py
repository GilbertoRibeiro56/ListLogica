x = int(input('Digite um número: '))
centena = 0
dezena = 0
unidade = 0
n_unidade = 0
n_dezena = 0
n_centena = 0

if (x < 0) or (x >= 500):
  print('Número Invalido')

else:
  x = x * 2
  centena = x // 100
  x = x - centena * 100

  dezena = x // 10
  x = x - dezena * 10

  unidade = x // 1

  n_centena = unidade
  n_dezena = dezena
  n_unidade = centena

  print(f'{n_centena}{n_dezena}{n_unidade}')
