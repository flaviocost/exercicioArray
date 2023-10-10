# 2 - altere o exercício anterior e mostre na tela,
# ao final, o nome de cada aluno e sua
# respectiva posição no array.

pergunta = int(input('Informe quantos alunos tem na sala: '))
alunos = []

for x in range(pergunta):
    nomesAlunos = input('Informe os nomes dos alunos: ')
    alunos.append(nomesAlunos)

for i in range(len(alunos)):
    print(f'Nome do Aluno: {alunos[i]}, númeração: {i + 1}')
