numero = input('Digite o número para verificar se é um palíndromo: ')

ini = 0
end = len(numero) - 1


while ini < end:
  if numero[ini] != numero[end]:
    palindromo = False

  else:
    palindromo = True

  ini += 1
  end -= 1
  
      
if palindromo == True:
  print(f'{numero} é um palíndromo')

else:
  print(f'{numero} não é um palíndromo')
