from lib import ler_arquivo, localizar, grava_arquivo, Registro

def altera_nota(nome_arquivo):
  while True:
    escolha = int(input('Digite 1 para editar notas ou outro número para sair: '))
    if escolha == 1:
      nome = input('Alterar a nota de quem? ')
      indice = localizar(nome_arquivo, nome)
      if indice == -1:
        print('Aluno não encontrado')
      else:
        alunos = ler_arquivo(nome_arquivo)
        alunos[indice].nota1 = float(input('Digite a nota 1: '))
        alunos[indice].nota2 = float(input('Digite a nota 2: '))
        grava_arquivo(nome_arquivo, alunos)

    else:
      print('Salvando e Saindo')
      break
  

#principal
altera_nota('alunos.txt')
