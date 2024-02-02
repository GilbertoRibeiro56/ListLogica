from lib import fatorial
A = []
for elementos in range(1, 11):
    A.append(int(input(f'Digite o {elementos}º número para adicionar ao vetor A: ')))
fatorial(A)
print(f'{fatorial(A)}')
