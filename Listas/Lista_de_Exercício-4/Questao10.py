n = float(input('Digite um número para descobrir a raiz quadrada: '))
b = 2

while abs(n - (b * b)) > 0.00001:
    p = (b + (n / b)) / 2
    b = p
print(f'A raiz quadrada do número {n} é aproximadamente {p:.4f}')
