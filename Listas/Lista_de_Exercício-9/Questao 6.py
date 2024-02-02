from lib import ler_arquivo, Registro, grava_arquivo

def Listar(nome_arquivo: str) -> int:
  print('\tALUNOS')
  print()
  alunos = ler_arquivo(nome_arquivo)
  tamanho = len(alunos)
  indice = -1
  for i in range(tamanho):
    media = (alunos[i].nota1+alunos[i].nota2)/2
    print(f'Numero:{alunos[i].numero} Nome:{alunos[i].nome},Media:{media}')
Listar('alunos.txt')
