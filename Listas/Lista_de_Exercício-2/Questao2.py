a = int(input('Digite um número: '))
b = int(input('Digite um número maior: '))
c = int(input('Digite um outro número maior: '))

if (a > b) or  (a > c):
  print('Valor inválido, Digite os três valores em ordem crescente!!')
  exit()
  
elif (b < a) or (b > c):
  print('Valor inválido, Digite os três valores em ordem crescente!!')
  exit()
  
d = int(input('Digite um número qualquer: '))

if d >= c:
  print(d,c,b,a)
elif (d >= b) and (d < c):
  print(c,d,b,a)
elif (d >= a) and (d < b) and (d < c):
  print(c,b,d,a)
elif d < a:
  print(c,b,a,d)
