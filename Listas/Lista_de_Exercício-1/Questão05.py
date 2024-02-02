mercadoria = float(input('Digite o valor da mercadoria: '))
desconto = int(input('Digite o percentual do desconto: '))
print('O valor do desconto é: ', mercadoria * (desconto / 100))
print('Com isso o preço final é :', mercadoria - (mercadoria * (desconto / 100)))
