from time import sleep

class Agenda:
  numero: int
  nome: str
  telefone: int
  idade: int

def Titulo(mensagem: str) -> None:
  tamanho = len(mensagem)
  print('*' * (tamanho+4))
  print('* ' + mensagem + ' *')
  print('*' * (tamanho+4))

#Cadastra os Contatos
def Cadastro(registros: list) -> None:
  Titulo('CADASTRO')

  if len(registros) == 10:
    print('Sem espaço para armazenar mais contatos!')

  else:
    registro = Agenda()
    if len(registros) == 0:
      registro.numero = 1
      
    else:
      last = len(registros)-1
      valor = registros[last].numero + 1
      registro.numero = valor
    registro.nome = input('Digite o Nome: ')
    registro.idade = int(input('Digite a idade: '))
    registro.telefone = int(input('Digite o numero de telefone: '))

    registros.append(registro)
    
#Procura os Contatos
def Found(registros: list) -> None:
  nome = input('Qual a pessoa que deseja encontrar o contato: ')
  for c in range(len(registros)):
    if registros[c].nome == nome:
      Titulo('NOME ENCONTRADO')
      print(f'Posição {c}: Tel: {registros[c].telefone} \n           {registros[c].idade} anos ')

#Edita um contato
def Editar(registros: list) -> None:
  Titulo('TELA DE EDIÇÃO')
  y = input('Qual o nome do contato que deseja editar: ')
  for c in range(len(registros)):
    if registros[c].nome == y:
      x = input('Deseja editar esse contato? (s) ou (n): ')
      if x == 's':
        registros[c].nome = input('Digite o novo nome: ')
        registros[c].telefone = int(input('Digite o novo telefone: '))
        registros[c].idade = input('Digite a nova idade: ')
        print('CONTATO EDITADO COM SUCESSO')

#Apagar um contato
def Deletar(registos: list) -> None:
  Titulo('DELETAR CONTATO')
  y = input('Qual o nome do contato que deseja deletar: ')
  for c in range(len(registros)):
    if registros[c].nome == y:
      del registros[c]
      print('CONTATO APAGADO')

#Listar Todos os Contatos
def Listar(registros: list) -> None:
  Titulo('CONTATOS')
  print(f'Contatos Registrados: {len(registros)}')
  for c in range(len(registros)):
    print(f'{c}. {registros[c].nome} - Tel.{registros[c].telefone} - {registros[c].idade} anos.')

#Média
def Media(registros: list) -> None:
  Titulo('MÉDIA DAS IDADES')
  soma = 0
  contador = 0
  for c in range(len(registros)):
    soma += registros[c].idade
    contador += 1
  media = soma / contador
  print(f'A média de idades da agenda é: {media:.1f} anos')

#Menu
def Menu() -> None:
  mensagem = '''******************************************************
        Agenda:
1. Cadastro.
2. Localizar um Contato.
3. Edição de Contato.
4. Deletar um Contato.
5. Mostrar Contatos.
6. Médias de idades.
7. Sair.
******************************************************'''
  print(mensagem)
  
#Principal

registros = []
while True:
  Menu()
  escolha = input('ESCOLHA UMA OPÇÃO:')
  if escolha == '1':
    Cadastro(registros)
    
  elif escolha == '2':
    Found(registros)
    
  elif escolha == '3':
    Editar(registros)

  elif escolha == '4':
    Deletar(registros)

  elif escolha == '5':
    Listar(registros)

  elif escolha == '6':
    Media(registros)

  elif escolha == '7':
    print('Programa Encerrando')
    a = 3
    for c in range(6):
      sleep(0.75)
      print(f'{a}/100')
      a *= 2
    sleep(0.5)
    print('Programa Finalizado')
    break

  else:
    Titulo('Digite um valor válido')
