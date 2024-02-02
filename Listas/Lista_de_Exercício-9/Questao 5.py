from lib import ler_arquivo, localizar, grava_arquivo, Registro

def excluir_aluno(nome_arquivo):
  while True:
    escolha = int(input('Digite 1 para excluir um aluno ou outro número para sair: '))
    if escolha == 1:
      nome = input('Excluir qual aluno? ')
      indice = localizar(nome_arquivo, nome)
      if indice == -1:
        print('Aluno não encontrado')
      else:
        alunos = ler_arquivo(nome_arquivo)
        del alunos[indice]
        grava_arquivo(nome_arquivo, alunos)

    else:
      print('Salvando e Saindo')
      break
      

#principal
excluir_aluno('alunos.txt')
