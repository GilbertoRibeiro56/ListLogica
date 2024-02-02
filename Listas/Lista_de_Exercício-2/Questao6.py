codigo = int(input('Digite o Código do Cargo: '))
if (codigo < 1 )or (codigo > 5):
  print('\nCÓDIGO INVÁLIDO!!','\nDIGITE UM CÓDIGO VALIDO DE 1 A 5!!')
  exit()
  
salary = float(input('Digite o Salário atual do funcionário: '))

if codigo == 1:
  new_salary = salary + (salary * 0.5)
  print('\nCARGO: Escrituário','\nSALÁRIO ATUAL:',salary,'\nVALOR DO AUMENTO: 50%','\nNOVO SALÁRIO:',new_salary)
  
if codigo == 2:
  new_salary = salary + (salary * 0.35)
  print('\nCARGO: Secretário','\nSALÁRIO ATUAL:',salary,'\nVALOR DO AUMENTO: 35%','\nNOVO SALÁRIO:',new_salary)
  
if codigo == 3:
  new_salary = salary + (salary * 0.2)
  print('\nCARGO: Caixa','\nSALÁRIO ATUAL:',salary,'\nVALOR DO AUMENTO: 20%','\nNOVO SALÁRIO:',new_salary)
  
if codigo == 4:
  new_salary = salary + (salary * 0.1)
  print('\nCARGO: Gerente','\nSALÁRIO ATUAL:',salary,'\nVALOR DO AUMENTO: 10%','\nNOVO SALÁRIO:',new_salary)
  
if codigo == 5:
  print('\nCARGO: Diretor','\nSALÁRIO ATUAL:',salary,'\nVALOR DO AUMENTO: SEM AUMENTO PARA ESTE CARGO')
