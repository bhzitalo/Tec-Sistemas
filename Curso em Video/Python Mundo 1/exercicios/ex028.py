# Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

from time import sleep # Adiciona uma pausa na execução do código
from random import randint # Para sortear um número
numero_secreto = randint(0, 5)

print("Jogo da advinhação! Que número estou pensando?")
numero = int(input("Digite um número entre 0 e 5: "))
print("Verificando...")
sleep(2) # Faz uma pausa de 2 segundos
if numero == numero_secreto:
    print("CERTA RESPOSTA!")
else:
    print("RESPOSTA ERRADA!")
    print(f"Eu pensei no número {numero_secreto}")