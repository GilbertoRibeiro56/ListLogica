from time import sleep

class Municipio:
  salario: float
  sexo: str
  idade: int
  filho: int
  
#Menu
def Menu() -> None:
  menu = '''*********************************************************
PORTAL DA TRANSPARÊNCIA(BETA)

1. Média dos salários
2. Média dos filhos.
3. Maior Salário.
4. Mulheres com salário maior que R$ 1000,00
0. Sair.
*********************************************************'''
  print(menu)

#Titulo
def Titulo(mensagem: str) -> None:
  tamanho = len(mensagem)
  print('*' * (tamanho+4))
  print('* ' + mensagem + ' *')
  print('*' * (tamanho+4))
  
#Cadastro de Servidores
def Cadastro(lista: list) -> None:
  registro = Municipio()
  if len(lista) == 0:
    registro.numero = 1

  else:
    last = len(lista) -1
    valor = lista[last].numero + 1
    registro.numero = valor
  registro.sexo = input('Informe o Sexo do servidor: (m) ou (f): ')
  registro.salario = float(input('Digite o salário desse servidor: '))
  registro.idade = int(input('Informe a idade desse servidor: '))
  registro.filho = int(input('Informe quantos filhos esse servidor tem: '))

  lista.append(registro)

#Maior Salario
def Estribado(lista: list) -> None:
  Titulo('MAIOR SALÁRIO')
  maior = 0
  for c in range(len(lista)):
    if (lista[c].salario > maior):
      maior = lista[c].salario
  print()
  print(f'O maior salário é: R$ {maior:.2f}.')

#Média de Filhos
def MediaMenino(lista: list) -> None:
  Titulo('Média de filhos dos servidores')
  filho = 0
  cont = 0
  for c in range(len(lista)):
    filho += lista[c].filho
    cont += 1
    media = filho/cont
  print()
  print(f' A media de filho é {media:.2f}')

#Média de Salário
def MediaDinheiro(dados: list) -> None:
  Titulo('Média dos salários dos servidores')
  salario = 0
  contador = 0
  for c in range(len(dados)):
      salario += dados[c].salario
      contador += 1
      media = salario/contador
  print(f' A media dos salários é {media:.2f}') 
    
#Mulheres w/ Salario > 1000
def Salario(variacao) -> None:
  cont_salario = 0
  cont_mulher = 0
  for c in range(len(lista)):
    if lista[c].sexo == 'f':
      for c in range(len(lista)):
        if lista[c].sexo == 'f':
          cont_mulher += 1
          if lista[c].salario > 1000:
            cont_salario += 1

      variacao = cont_salario * 100 / cont_mulher
      print('CALCULANDO!!')
      sleep(0.65)
      return(f'Foram cadastrada(s) {cont_mulher} mulher(es), desta(s) {variacao:.1f}% tem salário maior que R$ 1.000,00.')
    else:
      print()
      return('Nenhuma funcionária cadastrada!!')
      break

#Main
lista = []
for c in range(20):
  Cadastro(lista)
while True:
  Menu()
  escolha = int(input('Escolha a opção de consulta: '))
  if escolha == 1:
    MediaDinheiro(lista)
    
  elif escolha == 2:
    MediaMenino(lista)
    
  elif escolha == 3:
    Estribado(lista)
    
  elif escolha == 4:
    x = Salario(lista)
    print(x)
    
  elif escolha == 0:
    print('PROGRAMA FECHANDO')
    sleep(0.5)
    print('OBRIGADO PELA PREFERÊNCIA :)')
    sleep(0.5)
    break
  
  else:
    print()
    print('DIGITE UMA OPÇÃO VÁLIDA!!')
    print()
