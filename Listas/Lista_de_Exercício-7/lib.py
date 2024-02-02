#QUESTÃO 1
def soma(a,b,c):
  sum_int = 0
  if b < c:
    while b <= c:
      if b % a == 0:
        sum_int += b
      b += 1

  else:    
    if c < b:
      while c <= b:
        if c % a == 0:
          sum_int += c
        c += 1  
    else:
      sum_int = b + c
  return sum_int    


#QUESTÃO 2
def hora(s):
  h = 0
  m = 0
  
  h = s // 3600
  s -= h*3600

  m = s // 60
  s -= m*60

  total = f'TEMPO TOTAL DIGITADO: {h}:{m}:{s}'
  return total


#QUESTÃO 3
def total(a,b):
  fim = 0.0
  if (a > b):
    fim += ((a - b)* 100)/ b
    return fim

  if (b > a):
    fim += ((b - a)* 100)/a
    return fim

  if a == b:
    return 0


#QUESTÃO 4
def media(b,c,d):
  while True:
    a = input('Digite o tipo da média: Aritimética(A)ou Ponderada(P): ')
    if(a == 'A') or (a == 'P'):
      break
    
  media = 0.0
  if a == 'A':
    media = (b+c+d)/3
    return media

  if a == 'P':
    media = ((b*5) + (c*3) + (d*2))/10
    return media
  

#QUESTÃO 5
def tempo(a,b,c,d):
  if(d < b):
    d += 60
    c -= 1

  if(c < a):
    c += 24

  final = d - b + (c - a)*60
  return final


#QUESTÃO 6
def ordem_maior(a,b,c,d,e):
  big = a  
  #maiores
  if (b > big):
    big = b
  if (c > big):
    big = c
  if (d > big):
    big = d
  if (e > big):
    big = e
    
  return big

def ordem_menor(a,b,c,d,e):
  small = a
  #menores
  if (b < small):
    small = b
  if (c < small):
    small = c
  if (d < small):
    small = d
  if (e < small):
    small = e
    
  return small
  


#QUESTÃO 7
def fatorial(n):
  e = 1
  i = 1
  while i <= n:
    num = i
    i += 1
    fat = 1
    if num > 1:
      c = 1
      while c <= num:
        fat *= c
        c += 1

    e = e + (1/fat)
    
  return e

    
#QUESTÃO 9
def divisor(a:int) -> int:   
    v = []
    for i in range(1, a):
      if a % i == 0:
        v.append(i)
    if sum(v) == a:
      x = 'Número perfeito'
      return x
    else:
      x = 'número não perfeito'
      return x

      
#QUESTÃO 10
def fatorial(A):
    B = []
    for x in range(len(A)):
        PRODUTO = 1
        for y in range(1, A[x] + 1):
            PRODUTO *= y
        B.append(PRODUTO)
    return B


