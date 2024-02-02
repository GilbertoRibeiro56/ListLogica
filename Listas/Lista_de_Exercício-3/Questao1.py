nivel = int(input('Informe o nível do professor (1 a 3): '))
quantidade_hora = int(input('Quantas horas esse professor trabalhou: '))

salario = 0.00

if (nivel < 1) and (nivel > 3):
  print('Selecione um nível válido!!')
  exit()

elif nivel == 1:
  salario = quantidade_hora * 12.00

elif nivel == 2:
  salario = quantidade_hora * 17.00

elif nivel == 3:
  salario = quantidade_hora * 25.00

print(f'O Salário desse professor é: {salario:.2f}')
