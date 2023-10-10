# Faça um algoritmo que leia 30 valores do
# tipo inteiro e armazene-os em um vetor.
# A seguir, o algoritmo deverá informar
# (1) todos os números pares que existem no
# vetor;
# (2) o menor e o maior valor existente no
# vetor;
# (3) quantos dos valores do vetor são
# maiores que a média desses valores:

A = ['']*30
Par = ['']*30
maior = 0
soma = 0

for a in range(30):
    A[a] = int(input(f'Digite o {a + 1}º valor: '))
    if a == 0:
        menor = A[a]
    soma += A[a]
    if A[a] > maior:
        maior = A[a]
    if A[a] < menor:
        menor = A[a]

media = soma / 30
maiorMedia = 0
for b in range(30):
    if A[b] > media :
        maiorMedia += 1

for y in range(30):
    if A[y] % 2 == 0:
        Par[y] = A[y]

print(f'\n(1) Os numeros pares são: ')
for z in range(30):
    if Par[z] != '':
        print(Par[z], end='')

print(f'\n(2) O menor de todos é o {menor}. \n (2) O maior de todos é  o {maior}. \n No total, existem {maiorMedia}, numeros maiores que a média dos valores ({media}). ')