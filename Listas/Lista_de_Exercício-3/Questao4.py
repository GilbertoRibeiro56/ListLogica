ano_carro = int(input('Informe o ano do veículo: '))
valor_carro = float(input('Informe o valor do veículo em R$: '))

taxa = 0.00
imposto = 0.00

if ano_carro < 1990:
  imposto = (valor_carro * 0.01)

else:
  imposto = (valor_carro * 0.015)

print(f'O valor do imposto desse carro é: R$ {imposto:.2f}')
