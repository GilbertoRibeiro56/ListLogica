tamanho = 10
vetor = []
repete = []
for i in range(tamanho):
    numero = int(input('Digite um valor: '))
    vetor.append(numero)
    repete.append(False)

for i in range(tamanho):
    print(f'Número escrito: {vetor[i]} ', end='')
    print()

for i in range(tamanho):
    if repete[i] == False:
          quantidade = 1
          repete[i] = True
          for j in range(i+1, tamanho):
            if repete[j] == False:
              if vetor[i] == vetor[j]:
                quantidade += 1
                repete[j] = True
          print(f'O número {vetor[i]} aparece {quantidade} vez(es)!!')
