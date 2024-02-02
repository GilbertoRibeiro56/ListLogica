salario = float(input('Digite o Valor do Salário em R$: '))
aumento = 0.00
                
if salario > 1250.00:
  aumento = salario + (salario * 0.10)
else:
  aumento = salario + (salario * 0.15)

print(f'O Salário com o aumento fica: R$ {aumento:.2f}')
