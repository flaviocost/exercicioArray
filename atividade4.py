# 4 - Escreva um código que permita a leitura das notas de uma turma de 5 alunos e
# guarde num vetor, Calcular a média da turma e contar quantos alunos obtiveram
# nota acima desta média calculada Escrever a média da turma e o resultado da contagem


notas = [0]*5
notaAluno = 0
acima = 0
for x in range(5):
    pergunta = float(input(f"Nota do {x + 1}º aluno: "))
    notas[x] = pergunta

for y in range(5):
    notaAluno += notas[y]
media = notaAluno / 5

for z in range(5):
    if media <= notas[y]:
        acima += 1

print(f"{media} Foi a média da turma! \n" f"{acima} alunos ficaram acima da média.")