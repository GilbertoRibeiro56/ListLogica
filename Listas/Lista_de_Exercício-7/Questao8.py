dados_gerais = []
def coleta_de_dados():
    for habitantes in range(1, 6):
        dados = []
        sexo = input('Digite M para masculino ou F para feminino: ')
        cor_dos_olhos = input('Digite A para azul ou C para castanho: ')
        cor_dos_cabelos = input('Digite L para loiro, P para pretos ou C para castanhos: ')
        idade = int(input('Digite a idade deste habitante: '))
        dados = [sexo, cor_dos_olhos, cor_dos_cabelos, idade]
        dados_gerais.append(dados)
def media_de_idade():
    soma = quantidade = 0
    for habitantes in range(5):
        if dados_gerais[habitantes][1] == 'C' and dados_gerais[habitantes][2] == 'P':
            soma += dados_gerais[habitantes][3]
            quantidade += 1
    if quantidade == 0:
        return 'Não há habitantes com olhos castanhos e cabelos pretos!'
    else:
        return soma / quantidade
def maior_idade():
    maior_idade = dados_gerais[0][3]
    for habitantes in range(5):
        if dados_gerais[habitantes][3] >= maior_idade:
            maior_idade = dados_gerais[habitantes][3]
    return maior_idade
def fenotipo():
    quantidade = 0
    for habitantes in range(5):
        if dados_gerais[habitantes][0] == 'F' and 18 <= dados_gerais[habitantes][3] <= 35 and dados_gerais[habitantes][1] == 'A' and dados_gerais[habitantes][2] == 'L':
            quantidade += 1
    return quantidade
coleta_de_dados()
if type(media_de_idade()) == str:
    print(f'{media_de_idade()}')
else:
    print(f'A a média de idade das pessoas com olhos castanhos e cabelos pretos é {media_de_idade():.1f}')
print(f'A maior idade entre os habitantes é {maior_idade()} anos')
print(f'A quantidade de indivíduos do sexo feminino com idade entre 18 e 35 anos e que tenham olhos azuis e cabelos loiros é {fenotipo()}')
