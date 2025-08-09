# Crie um programa que simule uma prova com 5 questões e mostre ao final se o aluno foi aprovado ou não
# Nota > 7 = aprovado
# Nota > 5 e <= 7 recuperação
# Nota < 5 reprovado

# Questões sobre conceitos de Python e suas respostas corretas
questoes = {
    "1) Qual comando utilizamos para exibir uma mensagem ao usuário?\n(a) input()\n(b) float()\n(c) while()\n(d) print()\nResposta: ": "d",
    "2) Qual comando utilizamos para receber dados do usuário?\n(a) leia\n(b) input\n(c) print()\n(d) escreval()\n Resposta: ": "b",
    "3) Como se chama a estrutura usada para repetir blocos de código?\n(a) condicional\n(b) loop\n(c) variável\n(d) função\nResposta: ": "b",
    "4) O que o operador '==' verifica?\n(a) Atribuição\n(b) Diferença\n(c) Igualdade\n(d) Soma\nResposta: ": "c",
    "5) Qual símbolo é usado para fazer comentários em Python?\n(a) //\n(b) <!-- -->\n(c) #\n(d) /* */\nResposta: ": "c"
}

acertos = 0
print("📝 Simulado de Python - Responda com a letra correta (a, b, c ou d)\n")

# Loop para aplicar a prova
for pergunta, resposta_correta in questoes.items():
    resposta = input(pergunta).strip().lower() # remove espaços extras e transforma a resposta em letra minúscula, para evitar erro se o usuário digitar
    if resposta == resposta_correta: # verifica se o aluno acertou e, se sim, adiciona 1 ao contador de acertos.
        acertos += 1

# Calcula a nota adicionando 2 pontos por questão
nota = acertos * 2
print(f"\n📊 Você acertou {acertos} de 5 questões. Nota final: {nota}")

# Exibe a nota final
if nota > 7:
    print("Aprovado!")
elif nota > 5:
    print("Recuperação.")
else:
    print("Reprovado.")
