# Exercício Python 31: Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

print("=-"*15)
print("CALCULADORA DE PASSAGEM")
print("=-"*15)

distancia = float(input("Digite a distância percorrida: "))
if distancia <= 200:
    valor_passagem = distancia * 0.50
    print(f"O valor da viagem será de R$ {valor_passagem}")
else:
    valor_passagem = distancia * 0.45
    print(f"O valor da viagem será de R$ {valor_passagem}")