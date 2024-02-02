troco = int(input('Digite o valor do troco'))

troco50 = troco // 50
troco = troco - troco50 * 50

troco10 = troco // 10
troco = troco - troco10 * 10

troco1 = troco // 1

  
print(troco50,'moedas de 50')
print(troco10,'moedas de 10')
print(troco1,'moedas de 1')

