from lib import ler_arquivo, Registro, grava_arquivo

def Listar(nome_arquivo: str) -> int:
  print('\tALUNOS EM EXAME')
  print()
  alunos = ler_arquivo(nome_arquivo)
  tamanho = len(alunos)
  indice = -1
  for i in range(tamanho):
    media = (alunos[i].nota1+alunos[i].nota2)/2
    if media >= 3 and media < 7:
      print(f'Numero: {alunos[i].numero} Nome: {alunos[i].nome} Media:{media}')
Listar('alunos.txt')
