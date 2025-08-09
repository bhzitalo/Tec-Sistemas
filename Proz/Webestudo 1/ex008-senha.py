 # 8 - Verificador de senha: Peça uma senha e só permita continuar se for igual a "1234", usando while. 

# A variável senha começa vazia.
senha = ""

# O while roda enquanto a senha digitada for diferente de 'coxinha'
while senha != 'coxinha':
    senha = input('Digite sua senha: ')

# exibe na tela a mensagem de senha correta
print("Senha correta! Acesso permitido.")