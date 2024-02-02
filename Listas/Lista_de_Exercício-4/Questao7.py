quantidade = int(input('Quantas pessoas serão entrevistadas: '))
c = 1
i = 0
altura_final = 0
mulher = 0
homem = 0
diferencial = 0
media = 0


while c <= quantidade:
  sexo = input('Qual o sexo dessa pessoa: Digite(m)ou(f): ')
  if sexo == 'f':
    altura = float(input('Qual a altura dessa pessoa: '))
    altura_final += altura
    i += 1
    mulher +=1

    media = altura_final / i
    print(f'A média de altura entre as mulheres é: {media:.2f} m')

  if sexo == 'm':
    homem +=1

  c += 1


if homem < mulher:
  diferencial = (mulher - homem) / quantidade
  diferencial = abs(diferencial) * 100
  if diferencial == 100:
    print('Não tem homens nessa comparação')
  else:
    print(f'A diferença entre Mulheres e Homens é {diferencial:.1f}%')

elif homem > mulher:
  diferencial = (homem - mulher) / quantidade
  diferencial = abs(diferencial) * 100
  if diferencial == 100:
    print('Não tem mulheres nessa comparação')
  else:
    print(f'A diferença entre Homens e Mulheres é {diferencial:.1f}%')


else:
  print('Não existe diferença de percentual')



  


          
          
      
      
    
