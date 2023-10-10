# Faça um código para ler um vetor de 30
# números. Após isto, ler mais um número
# qualquer, calcular e escrever quantas
# vezes esse número aparece no vetor.

vetor = ['']*30

for a in range(30):
    vetor[a] = int(input(f'Informe o {a + 1} Valor: '))

valorAleatorio = int(input('Qual valor deseja procurar: '))
contador = 0
for b in range(30):
    if vetor[b] == valorAleatorio:
        contador += 1
if contador == 0:
    print('Não existe valores iguais!')
else:
    print(f'O número {valorAleatorio} apareceu {contador} vezes na lista.')