# 7 - Soma de 1 até N: Peça um número N e calcule a soma de todos os números de 1 

# Solicita ao usuário um número 
num = int(input("Digite um número: "))

# Calcula a soma de 1 até num
soma = 0
for contador in range(1, num + 1):
    soma = soma + contador

# Exibe o resultado
print(f"A soma de 1 até {num} é {soma}")