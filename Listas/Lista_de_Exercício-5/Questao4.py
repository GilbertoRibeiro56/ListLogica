v1 = []
n = 0
for c in range (0,10):
  nome = input('Digite um nome(USE LETRAS MAIÚSCULAS E ACENTUAÇÃO): ')
  if nome == 'JOSÉ':
    n += 1
  v1.append(nome)


print(f'O nome JOSÉ aparece {n} vezes!')
