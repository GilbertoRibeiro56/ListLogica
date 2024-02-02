matriz = []
linha = 20
coluna = 3

for l in range(linha):
  lin = []
  for c in range(coluna):
    x = float(input(f'Informe a {c+1}ª nota do {l+1}º aluno: '))
    lin.append(x)
  matriz.append(lin)


print('*'*70)
cont = 0
print('MATRIZ DE NOTAS')
for c in range(linha):
  print(f'O aluno {cont+1} NOTAS: {matriz[c]} ', end='')
  print()
  if c > 20:
    c = 0
  cont += 1
  if cont > linha:
    break

print('*'*70)
print('MÉDIA DOS ALUNOS')
nota = 0.0
for l in range(linha):
  soma = 0
  for c in range(coluna):
    soma = soma + matriz[l][c]
    nota += soma
  print(f'O aluno {l+1} ficou com média: {soma/coluna:.1f} ', end='')
  print()

media_turma = nota / linha
print(f'A média da Turma é: {media_turma:.1f}')
