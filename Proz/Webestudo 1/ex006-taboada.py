# 6 -  Tabuada: Peça um número e mostre a tabuada dele de 1 a 10.

# Declaração de variáveis: (num) pede pro usuário digitar um número
# Contador é 1 e sempre recebe + 1 até ser igual a 10
num = int(input('Digite um número: ')) 
contador = 1

# Enquanto o contador for < 10, exibe o resultador e adiciona +1 ao contador
while contador <= 10:
    print(f' {num} x {contador} = {contador}')
    contador = contador + 1

