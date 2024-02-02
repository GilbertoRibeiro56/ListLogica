valor_casa = float(input('Informe o valor da casa a ser comprada: '))
salario_comp = float(input('Informe o salário do comprador: '))
anos_pag = int(input('Informe o tempo em anos para a quitação do imóvel: '))
mes_pag = (anos_pag * 12)

valor_limite = salario_comp * 0.3
valor_mes = (valor_casa / mes_pag)

if valor_mes > valor_limite:
  print(f'\nO valor da prestação é superior a 30% do salário!')
  print('EMPRESTIMO RECUSADO!!')
else:
  print(f'\nO valor da prestação é R${valor_mes:.2f} e está abaixo dos 30% exigidos!')
  print('EMPRESTIMO APROVADO!!')
