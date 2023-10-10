# Perguntar ao usuário quantos alunos tem
# na sala e criar um array, unidimensional
# (Vetor) com o nome de todos os alunos da
# sala

pergunta = int(input('Informe quantos alunos tem na sala: '))
alunos = [0]*pergunta

for x in range(pergunta):
    nomesAlunos = input('Informe os nomes dos alunos: ')
    alunos.append(nomesAlunos)