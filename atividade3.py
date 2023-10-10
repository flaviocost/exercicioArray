# 3 - altere o exercício anterior para permitir
# achar o nome de um aluno na lista

pergunta = int(input('Informe quantos alunos tem na sala: '))
alunos = [0]*pergunta

for x in range(pergunta):
    nomesAlunos = input('Informe os nomes dos alunos: ')
    alunos[x] = nomesAlunos

achou = 0
procura = input('Qual aluno deseja procurar: ')
for j in range(pergunta):
    if procura == alunos[j]:
        achou += 1
        print(f'O Aluno {procura}, está na {j}º Posição')



