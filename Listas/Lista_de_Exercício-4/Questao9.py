n = int(input('Digite o numero de termos que você quer descobrir da sequência Fibonacci: '))
n1 = 0
n2 = 1
c = 3
print(n1, end=' ')
print(n2, end=' ')
while c <= n:
  n3 = n1 + n2
  print(n3, end=' ')
  n1 = n2
  n2 = n3
  c += 1



