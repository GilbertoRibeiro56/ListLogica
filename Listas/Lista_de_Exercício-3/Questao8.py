h = float(input('Informe a Altura: '))
p = float(input('Informe o Peso: '))
s = input('Informe o Sexo: ')

peso_ideal = 0.0
peso_final = 0.0
     
if s == 'm':
  peso_ideal = (72.7 * h) - 58
  peso_ideal = round(peso_ideal, 2)
  if p > peso_ideal:
    peso_final = p - peso_ideal
    print(f'Você precisa perder {peso_final:.2f}kg')
     
  if p < peso_ideal:
    peso_final = peso_ideal - p
    print(f'Você precisa ganhar {peso_final:.2f}kg')

  if p == peso_ideal:
    print('Você está no peso ideal')

elif s == 'f':
  peso_ideal = (62.1 * h) - 44.7
  peso_ideal = round(peso_ideal, 2)
  if p > peso_ideal:
    peso_final = p - peso_ideal
    print(f'Você precisa perder {peso_final:.2f}kg')
     
  if p < peso_ideal:
    peso_final = peso_ideal - p
    print(f'Você precisa ganhar {peso_final:.2f}kg')

  if p == peso_ideal:
    print('Você está no peso ideal')

else:
  print('Digite um Sexo válido!!')

