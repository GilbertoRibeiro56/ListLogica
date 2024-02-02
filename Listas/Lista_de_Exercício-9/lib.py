class Registro:
  numero: int
  nome: str
  curso: str
  nota1: float
  nota2: float


def ler_arquivo(nome_arquivo: str) -> list:
  arquivo = open(nome_arquivo, 'r')
  alunos = []
  for linha in arquivo.readlines():
    linha = linha.replace('\n','')
    campos = linha.split('#')
    aluno = Registro()
    aluno.numero = int(campos[0])
    aluno.nome = campos[1]
    aluno.curso = campos[2]
    aluno.nota1 = float(campos[3])
    aluno.nota2 = float(campos[4])
    alunos.append(aluno)
  arquivo.close()
  return alunos


def grava_arquivo(nome_arquivo: str, alunos: list) -> None:
  arquivo = open(nome_arquivo, 'w')
  tamanho = len(alunos)
  for i in range(tamanho):
    linha = f'{alunos[i].numero}#{alunos[i].nome}#{alunos[i].curso}#{alunos[i].nota1}#{alunos[i].nota2}\n'
    arquivo.write(linha)
  arquivo.close()


def localizar(nome_arquivo: str, nome: str) -> int:
  alunos = ler_arquivo(nome_arquivo)
  tamanho = len(alunos)
  indice = -1
  for i in range(tamanho):
    if alunos[i].nome == nome:
      indice = i
      break
  return indice
  
  
