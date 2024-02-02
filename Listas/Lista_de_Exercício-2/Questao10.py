salario_min = float(input('Digite o valor do salário mínimo: '))
horas = int(input('Digite o valor de horas trabalhadas: '))
depend = int(input('Digite o número de dependentes do funcionário: '))
hora_ex = int(input('Digite quantidade de horas extras trabalhadas: '))

valor_hora = salario_min * 0.20      #Valor da hora trabalhada
salario_mes = horas * valor_hora     #Valor do Salario do Mês
acres_dependente = depend * 32       #Acréscimo dos dependentes
acres_hora_ex = (valor_hora * 1.5 * hora_ex)    #Valor da Hora Extra
salario_bruto = salario_mes + acres_dependente + acres_hora_ex

if salario_bruto < 200:
  imposto = 0
  
if (salario_bruto >= 200) and (salario_bruto <= 500):
  imposto = 0.1
  
if salario_bruto > 500:
  imposto = 0.2

salario_liqui = salario_bruto - (salario_bruto * imposto)

if salario_liqui <= 350:
  grati = 100

if salario_liqui >350:
  grati = 50

salario_final = salario_liqui + grati

print(f'O valor do salário desse funcionário é: {salario_final:.2f}')
