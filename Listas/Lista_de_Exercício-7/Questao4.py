from lib import media
n1 = float(input('Digite uma nota: '))
n2 = float(input('Digite uma outra nota: '))
n3 = float(input('Digite mais uma nota: '))

resultado = media(n1,n2,n3)
print(f'Média Final {resultado:.1f}')
