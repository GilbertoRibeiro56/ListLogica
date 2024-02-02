numero = int(input('Digite um número que represente a fatorial: '))

e = 1

i = 1
while i <= numero:
  num = i
  i += 1
  
  fat = 1
  if num > 1:
    c = 1
    while c <= num:
      fat *= c
      c += 1

e = e + (1/fat)
  
print(e)



