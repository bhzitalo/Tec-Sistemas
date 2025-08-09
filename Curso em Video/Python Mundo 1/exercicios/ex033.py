# Exercício Python 33: Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

# Pede os números ao usuário
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))

# Assume que o primeiro número é o maior e o menor
menor = num1
maior = num1

# Verifica o menor
if num2 < menor:
    menor = num2
if num3 < menor:
    menor = num3

# Verifica o maior
if num2 > maior:
    maior = num2
if num3 > maior:
    maior = num3

# Exibe os resultados
print(f"O menor número é {menor}")
print(f"O maior número é {maior}")