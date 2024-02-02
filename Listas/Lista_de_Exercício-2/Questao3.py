a = int(input('Digite um Número: '))
b = int(input('Digite um outro Número: '))
c = int(input('Digite mais um Número: '))

bigger = a
smaller = a

if (b > bigger):
  bigger = b
if (c > bigger):
  bigger = c
if (b < smaller):
  smaller = b
if (c < smaller):
  smaller = c
print('O maior número é:',bigger,'\nO menor número é:',smaller)
