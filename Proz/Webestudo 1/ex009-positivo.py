# 9. Número positivo, negativo ou zero: Leia um número e diga se ele é positivo, negativo ou igual a zero.

# Recebe um número
num = int(input('Digite um número: '))

# Verifica o número
if num > 0:
    print(f'O número {num} é maior que 0, ou seja, ele é positivo!')
elif num < 0:
    print(f'O número {num} é menor que 0, ou seja, ele é negativo')
else:
    print('O número é igual a 0')