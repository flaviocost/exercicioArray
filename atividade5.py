# Ler um vetor A de 10 números. logo em
# seguida, ler mais um número e guardar em
# uma variável X.
# Armazenar em um vetor M o resultado de
# cada elemento de A multiplicado pelo
# valor X. Logo após, imprimir o vetor M.

fator = int(input('Informe o valor que deseja multiplicar:  '))
a = ['']*10

for x in range(10):
    a[x] = int(input(f'Informe o {x + 1}ª valor: '))

m = ['']*10
for y in range(10):
    m[y] = a[y] * fator
    print(f'O valor {a[y]} x {fator} = {m[y]}')