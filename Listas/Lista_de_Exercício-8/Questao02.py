class Professores:
  numero: int
  sexo: str
  hora: float

def Titulo(mensagem: str) -> None:
  tamanho = len(mensagem)
  print('*' * (tamanho+4))
  print('* ' + mensagem + ' *')
  print('*' * (tamanho+4))

#Cadastra os Professores
def Cadastro(tabela: list) -> None:
  if len(tabela) == 10:
    print('Não é possível cadastar outro funcionário!')
  

  else:
    registro = Professores()
    if len(tabela) == 0:
      registro.numero = 1

    else:
      last = len(tabela) -1
      valor = tabela[last].numero +1
      registro.numero = valor
    registro.sexo = input('Informe o sexo do professor (m) ou (f): ')
    registro.hora = int(input('Quantas horas esse professor trabalhou: '))

    tabela.append(registro)
    
#Mostrar Geral
def Listar(tabela: list) -> None:
  Titulo('QUADRO DE FUNCIONÁRIOS')
  for c in range(len(tabela)):
    if tabela[c].sexo == 'm':
      if tabela[c].hora <= 70:
        desconto = 10
        desc = '10'
      else:
        desconto = 8
        desc = '8'
    if tabela[c].sexo == 'f':
      if tabela[c].hora <= 70:
        desconto = 7
        desc = '7'
      else:
        desconto = 5
        desc = '5'
    bruto = tabela[c].hora * 60.50
    salario_liquido = (bruto - (bruto * desconto / 100))
    print(f'Funcionário {c}. Salário Bruto R$ {bruto:.2f} - DESCONTO -> {desc}% = Salário Líquido R${salario_liquido:.2f}.')
  print('=-'*40)
  
#Principal
tabela = []
while True:
  Cadastro(tabela)
  if len(tabela) == 10:
    break


Listar(tabela)

#Media dos Professores
Titulo('MÉDIA DOS PROFESSORES')
contM = 0
totalM = 0.0
mediaM = 0.0

for i in range(len(tabela)):
  if (tabela[i].sexo == 'm') == '':
    break
  else:
    for c in range(len(tabela)):
      if tabela[c].sexo == 'm':
        totalM += tabela[c].hora * 60.50
        contM += 1
        mediaM = totalM / contM
print(f'A média dos salários dos professores é R${mediaM:.2f}.')
    
contF = 0
totalF = 0.0
mediaF = 0.0
for i in range(len(tabela)):
  if(tabela[i].sexo == 'f') == '':
    break
  else:
    for c in range(len(tabela)):
      if tabela[c].sexo == 'f':
        totalF += tabela[c].hora * 60.50
        contF += 1
        mediaF = totalF / contF
print(f'A média dos salários das professoras é R${mediaF:.2f}.')
