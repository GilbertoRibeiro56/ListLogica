from lib import ler_arquivo, Registro, grava_arquivo

def Listar(nome_arquivo: str) -> int:
  curso = input('Digite o Curso: ')
  print(f'\tALUNOS DO CURSO DE {curso}')
  print()
  alunos = ler_arquivo(nome_arquivo)
  tamanho = len(alunos)
  indice = -1
  for i in range(tamanho):
    if curso == alunos[i].curso:
      print(f'Numero: {alunos[i].numero} Nome: {alunos[i].nome}')
Listar('alunos.txt')
