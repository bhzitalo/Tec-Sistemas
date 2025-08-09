#. Média de três notas: Leia três notas de um aluno, calcule a média e informe se ele foi aprovado (média ≥ 7). 
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
nota3 = float(input('Digite a terceira nota: '))
soma = nota1 + nota2 + nota3
media = soma / 3
print(f'A média é igual a: {media:.1f}')
if media >= 7:
    print('APROVADO')
else:
    print('REPROVADO')