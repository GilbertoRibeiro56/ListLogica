from lib import soma

while True:
    x = int(input('Digite um número maior que 1(um): '))
    if x > 1:
      break

y = int(input('Digite um valor: '))
z = int(input('Digite um outro valor: '))

resultado = soma(x,y,z)

print(f'Resultado da soma = {resultado}')
