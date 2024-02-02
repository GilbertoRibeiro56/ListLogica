from utils import Registro, ler_arquivo, grava_arquivo

def novo_numero(nome_arquivo: str) -> int:
  alunos = ler_arquivo(nome_arquivo)
  if len(alunos) != 0:
    maior_numero = alunos[0].numero
  else:
    return 1
  tamanho = len(alunos)
  for i in range(tamanho):
    if alunos[i].numero > maior_numero:
      maior_numero = alunos[i].numero
  return maior_numero + 1


def novo_aluno(nome_arquivo: str) -> None:
  while True:
    escolha = int(input('Digite 1 para cadastrar ou outro número para sair: '))
    if escolha == 1:
      print('Cadastro de novo aluno: ')
      aluno = Registro()
      aluno.numero = novo_numero(nome_arquivo)
      aluno.nome = input('Digite o nome: ')
      aluno.curso = input('Digite o curso: ')
      aluno.nota1 = float(input('Digite a nota 1: '))
      aluno.nota2 = float(input('Digite a nota 2: '))
      
      alunos = ler_arquivo(nome_arquivo)
      alunos.append(aluno)
      grava_arquivo(nome_arquivo, alunos)
    else:
      print('Saindo')
      break
    


#principal
novo_aluno('alunos.txt')
