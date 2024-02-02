n = int(input('Digite quantos numeros primos vc quer: '))
c = 0
numero = 2

while c <= n:
  primo = True

  
  if numero > 1:
    if numero % 2 == 0:
      if numero != 2:
        primo = False
    else:
      divisor = 3    
      while (divisor < numero):
        if numero % divisor == 0:
          primo = False
          break
        divisor += 2
  else:
    primo = False

    if primo == True:
      print(numero)    
      c+=1

  numero += 1
