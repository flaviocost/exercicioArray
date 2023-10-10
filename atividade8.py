# Faça um código para ler 5 nomes de
# usuários e suas respectivas senhas, e
# armazenar cada lista em um array
# diferente, após completar a digitação,
# imprimir , nome, senha e posição dos
# dados no array

nomesUsuarios = ['']*5
senhasUsuarios = ['']*5

for x in range(5):
    nomesUsuarios[x] = input('Digite seu nome: ')
    senhasUsuarios[x] = input('Digite sua senha: ')

for y in range(5):
    print(f'O usuário  {y}ª {nomesUsuarios[y]} tem como senha: {senhasUsuarios[y]}')

