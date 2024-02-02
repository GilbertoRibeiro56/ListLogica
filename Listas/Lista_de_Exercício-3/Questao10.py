qtd_xicara = int(input('Informe a quantidade de xícaras de café'))
litro_agua = 0.05
n_colher = 0.25

qtd_litro = qtd_xicara * litro_agua
qtd_colher = qtd_xicara * n_colher

print(f'Para fazer {qtd_xicara:.0f} xícara de café será preciso {qtd_litro:.2f}L de água e {qtd_colher:.1f} colheres de pó de café')
