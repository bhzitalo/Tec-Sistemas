# Exercício Python 29: Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

from random import randint
velocidade = randint(70, 100)

if velocidade > 80:
    multa = velocidade - 80
    print("Você excedeu o limite de velocidade!")
    print("Limite: 80 km/h")
    print(f"Sua velocidade: {velocidade} km/h")
    print(f"Você foi multado em {multa*7.00:.2f} reais")
else:
    print("Velocidade Permitida!")
    print(f"Velocidade: {velocidade} km/h")