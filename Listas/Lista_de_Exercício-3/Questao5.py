graus = float(input('Informe a medida do ângulo: '))
volta = 0
sobra = 0

if graus > 0:
  if graus > 360:
    volta = graus // 360
    sobra = graus % 360
  
  if (graus > 0) and (graus < 90):
    print('Primeiro Quadrante!!')

  if (graus > 90) and (graus < 180):
    print('Segundo Quadrante!!')

  if (graus > 180) and (graus < 270):
    print('Terceiro Quadrante!!')

  if (graus > 270) and (graus < 360):
    print('Quarto Quadrante!!')

  if volta >= 1:
    print(f'Foram dadas {volta:.0f} voltas no sentido antihorario')





if graus < 0:
  if graus < -360:
    volta = graus // 360

  if (graus < 0) and (graus > -90):
    print('Quarto Quadrante!!')

  if (graus < -90) and (graus > -180):
    print('Terceiro Quadrante!!')

  if (graus < -180) and (graus > -270):
    print('Segundo Quadrante!!')

  if (graus < -270) and (graus > -360):
    print('Primeiro Quadrante!!')

  if volta <= -1:
    volta = volta * (-1)
    print(f'Foram dadas {volta:.0f} voltas no sentido horario')
    









