from lib import tempo

print('Que horas o jogo começou?')
h1 = int(input('Hora: '))
m1 = int(input('Minutos: '))

print('Que horas o jogo terminou?')
h2 = int(input('Hora: '))
m2 = int(input('Minutos: '))

final = tempo(h1,m1,h2,m2)
print(f'O jogo teve duração de {final}min!')
