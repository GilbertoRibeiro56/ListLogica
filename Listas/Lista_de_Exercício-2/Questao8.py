print('VALORES DE TIPOS DE INSTALAÇÃO POSSÍVEIS','\n','\nR = RESIDÊNCIA','\nI = INDUSTRIA','\nC = COMÉRCIO','\n','\n****ATENÇÃO QUE A LETRA DO TIPO DA INSTALAÇÃO TEM QUE SER DIGITADA MAIÚSCULA****','\n')

kwh = int(input('Digite a quantidade de kW/h consumida: '))
instalacao = input('Digite o tipo da instalação: ')
total = 0.00


if instalacao == 'R':
  if kwh <= 500:
    total = kwh * 0.4
    print(f'O valor da conta de Energia Elétrica é: R${total:.2f}')
  else:
    total = kwh * 0.65
    print(f'O valor da conta de Energia Elétrica é: R${total:.2f}')

if instalacao == 'C':
  if kwh <= 1000:
    total = kwh * 0.55
    print(f'O valor da conta de Energia Elétrica é: R${total:.2f}')
  else:
    total = kwh * 0.60
    print(f'O valor da conta de Energia Elétrica é: R${total:.2f}')
    
if instalacao == 'I':
  if kwh <= 5000:
    total = kwh * 0.55
    print(f'O valor da conta de Energia Elétrica é: R${total:.2f}')
  else:
    total = kwh * 0.6
    print(f'O valor da conta de Energia Elétrica é: R${total:.2f}')

else:
  print('\nTIPO DE INSTALAÇÃO INVÁLIDA!!')
  print('\nDIGITE UM VALOR VÁLIDO!!')
