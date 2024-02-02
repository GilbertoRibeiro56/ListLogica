posicao = []
x = int(input('Digite o Tamanho do vetor: '))
for c in range(x):
  nome = input('Digite um nome: ')
  posicao.append(nome)

print(end='~'*30)
print()
print('Posição Par:')
for c in range(1,x,2):
  print(f'{posicao[c]} na posicao {c + 1}')
  
print(end='~'*30)
print()

print('Posição Impar:')
for c in range(0,x,2):
  print(f'{posicao[c]} na posicao {c + 1}')

