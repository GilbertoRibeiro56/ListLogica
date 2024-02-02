cigarro_dia = int(input('Quantos cigarros o fumante fuma em um dia: '))
anos_fumante = int(input('Quantos anos faz que a pessoa fuma: '))
dias_fumante = (anos_fumante * 365)
tempo_vida = (dias_fumante * cigarro_dia) / 6
dias_perdidos = tempo_vida / 24
print(f'O fumante perdeu {dias_perdidos:.2f} dias de vida')
print(f'O fumante perdeu {dias_perdidos / 365:.2f} anos de vida')
