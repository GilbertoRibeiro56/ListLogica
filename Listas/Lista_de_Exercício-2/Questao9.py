altura = float(input('Digite o valor da sua altura: '))

if altura <= 0:
  print('ALTURA INVÁLIDA!!')

if (altura > 0) and (altura < 1.50):
  print('Pessoa Baixa!')

if (altura >= 1.50) and (altura <= 1.80):
  print('Pessoa de altura Normal!')

if altura > 1.80:
  print('Pessoa Alta!')
