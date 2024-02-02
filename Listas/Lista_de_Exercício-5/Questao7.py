from time import sleep

objeto = []
for c in range(1,11):
  objeto.append(c)

valor = []
for c in range(0,10):
  produto = float(input(f'Digite o valor do Produto {c + 1}:'))
  valor.append(produto)

quantidade = []
for c in range(0,10):
  qtde = int(input(f'Digite a Quantidade de produtos vendidos com o Código {c + 1}: '))
  quantidade.append(qtde)

print(end='~'*70)
print()

c = 0
total = 0
while c < len(quantidade):
  total += quantidade[c]
  c += 1
sleep(1)
print(f'{total} objetos vendidos\n')

c = 0
while c < len(valor):
  sleep(0.5)
  print(f'Produto {c+1}: Valor Unitário: R$ {valor[c]:.2f} ')
  c += 1
print('~'*70)

c = 0
total = 0
while c < 10:
  total = (quantidade[c] * valor[c])
  sleep(0.5)
  print(f'Valor Total do produto {c+1} é: {total}')
  c += 1
print('~'*70)

c = 0
total = 0
while c < 10:
  total += quantidade[c] * valor[c]
  c += 1
print(f'Valor Total das Vendas = {total}')
print(f'O valor da comissão do vendedor é R$ {(total * 0.05):.2f}')

c = 0
total = 0
valor_final = 0
posicao_final = 0
while c < 10:
  if quantidade[c] > total:
    total = quantidade[c]
    valor_final = valor[c]
    posicao_final = objeto[c]
    c += 1
print(f'O valor do objeto mais vendido foi R$ {valor_final:.2f}, e sua posição no vetor é {posicao_final}')
