valor = 0
valor_final = 0

while True:
  codigo = int(input('Digite o codigo de um produto: '))
  if codigo == 1:
    quantidade = int(input('Digite a Quantidade de Produtos: '))
    valor = (0.50 * quantidade)
    valor_final = valor_final + valor
    
  elif codigo == 2:
    quantidade = int(input('Digite a Quantidade de Produtos: '))
    valor = (1.00 * quantidade)
    valor_final = valor_final + valor
    
  elif codigo == 3:
    quantidade = int(input('Digite a Quantidade de Produtos: '))
    valor = (4.00 * quantidade)
    valor_final = valor_final + valor
    
  elif codigo == 5:
    quantidade = int(input('Digite a Quantidade de Produtos: '))
    valor =(7.00 * quantidade)
    valor_final = valor_final + valor
    
  elif codigo == 9:
    quantidade = int(input('Digite a Quantidade de Produtos: '))
    valor = (8.00 * quantidade)
    valor_final = valor_final + valor
    
  elif codigo == 0:
    break

  else:
    print('Valor inválido!!')

print(f'Valor Total a ser pago: R$ {valor_final:.2f}')
