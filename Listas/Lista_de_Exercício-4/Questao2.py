while True:
  print('SIMBOLOS DE OPERAÇÃO POSSÍVEIS','\n','\n1 = SOMA','\n2 = SUBTRAÇÃO','\n3 = MULTIPLICAÇÃO','\n4 = DIVISÃO','\n5 = ENCERRAR O PROGRAMA','\n')

  operacao = int(input('Digite a Operação: '))

  if operacao == 5:
    print('Saindo do Programa!!')
    break

  elif (operacao >= 1) and (operacao < 5):
    numero = int(input('Digite o Número para saber a tabuada dele: '))
    c = 1
    while c <= 10:
      if operacao == 1:
        resultado = numero + c
        print(f'{numero} + {c} = {resultado}')


      if operacao == 2:
        resultado = numero - c
        if resultado >=0:
          print(f'{numero} - {c} = {resultado}')


      if operacao == 3:
        resultado = numero * c
        print(f'{numero} x {c} = {resultado}')
		

      if operacao == 4:
        resultado = numero / c
        print(f'{numero} / {c} = {resultado:.2f}')
			
      c += 1
	
	
  else:
    print('Operação Inválida')
