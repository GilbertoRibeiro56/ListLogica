from lib import ordem_maior, ordem_menor

a = int(input('Digite um número: '))
b = int(input('Digite um número: '))
c = int(input('Digite um número: '))
d = int(input('Digite um número: '))
e = int(input('Digite um número: '))

maior = ordem_maior(a,b,c,d,e)
menor = ordem_menor(a,b,c,d,e)

print(f'O maior valor digitado é: {maior} \nO menor valor digitado foi: {menor}')
