# Altere o sistema anterior e faça um sistema
# de login, pedindo a senha do usuário e
# mostrando seu nome e a mensagem, login
# efetuado com sucesso.

nomesUsuarios = ['']*5
senhasUsuarios = ['']*5

for x in range(1):
    print('Realize seu cadastro e em seguida logue em sua conta usando a senha.')
    nomesUsuarios[x] = input('Digite seu nome: ')
    senhasUsuarios[x] = input('Digite sua senha: ')

print('Digite sua senha para efetuar o login!')
senha = input('Digite sua senha: ')

while senha != senhasUsuarios[x]:
    senha = input('Senha inválida! Digite novamente: ')
else:
    print('Login efetuado com sucesso!')
