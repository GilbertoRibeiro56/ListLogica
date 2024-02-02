class Estatistica:
  estado: str
  veiculo :int
  acidente : int


def Menu() -> None:
  menu = '''
*********************************************************
REGISTRO DE TRÂNSITO DO NORDESTE(2014)

1. Número de veículos no Nordeste(Detalhado)
2. Percentual de veículos de cada estado.
3. Percentual de acidentes no Nordeste(em Porcento(%)).
4. Maior e Menor índice de acidentes em 2014.
0. Sair.
*********************************************************'''
  print(menu)

#Cadastro de estados
def Cadastro(lista: list) -> None:
  registro = Estatistica()
  if len(lista) == 0:
    registro.numero = 1

  else:
    last = len(lista) -1
    valor = lista[last].numero + 1
    registro.numero = valor
  registro.estado = input('Informe a Unidade Federativa: ')
  registro.veiculo = int(input('Informe o tamanho da frota de veículos desse estado: '))
  registro.acidente = int(input('Informe o número de acidentes: '))

  lista.append(registro)


#Tabela de veículos
def Tabela() -> None:
  for c in range(len(lista)):
    print(f'UF: {lista[c].estado} - {lista[c].veiculo} Veiculos - {lista[c].acidente} Acidentes')
  nordeste = 0
  for i in range(len(lista)):
    nordeste += lista[i].veiculo
    
#Maior e Menor
def MaiorMenor(dados:list)->None:
  maior = -1
  menor = 1000000000000

  for c in range(len(lista)):
    if lista[c].acidente > maior:
      maior = lista[c].acidente
      x = lista[c].estado

    if lista[c].acidente < menor:
      menor = lista[c].acidente
      y = lista[c].estado
  print(f'o maior indice é {maior}  do {x}')
  print(f'o menor indice é {menor} do {y}')
    
#Total de veículos
def Veiculos(lista: list) -> None:
  veiculos = 0
  for c in range(len(lista)):
    veiculos += lista[c].veiculo
  for i in range(len(lista)):
    percentual = lista[i].veiculo * 100 / veiculos
    print(f'percentual de veiculos do {lista[i].estado} é = {percentual:.2f}%.')

#Media de acidentes
def Acidente(lista: list) -> None:
  for c in range(len(lista)):
    media =  lista[c].acidente / 12
    print(f'media de acidentes no estado do {lista[c].estado} é = {media:.2f} acidentes por mês.')


#Principal
lista = []
for c in range(9):
  Cadastro(lista)

while True:
  Menu()
  escolha = int(input('Escolha uma Opção: '))
  if escolha == 1:
    Tabela()
  if escolha == 2:
    Veiculos(lista)
  if escolha == 3:
    Acidente(lista)
  if escolha == 4:
    MaiorMenor(lista)
  if escolha == 0:
    print('PROGRAMA ENCERRANDO!!')
    break
  else:
    print('Digite uma opção válida.')
    print()

