numero = int(input('Digite um número a ser verificado: '))
c = 1
divisivel = 0


while c <= numero:
  if numero % c == 0:
    divisivel += 1      
    
  c += 1
if divisivel >= 2:
  print('É um número Primo!!')

else:
  print(f'Não é um número primo!!')

