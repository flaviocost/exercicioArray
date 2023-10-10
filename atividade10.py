# Faça um código para ler um valor N qualquer (que
# será o tamanho dos vetores). Após, ler dois
# vetores A e B (de tamanho N cada um) e depois
# armazenar em um terceiro vetor Soma a soma dos
# elementos do vetor A com os do vetor B
# (respeitando as mesmas posições) e escrever o
# vetor Soma.

valorN = int(input('Informe o tamanho da lista: '))

a = [''] * valorN
b = [''] * valorN

for x in range(valorN):
    a[x] = int(input(f'Informe o {x + 1}valor da lista "A": '))
for y in range(valorN):
    b[y] = int(input(f'Informe o {y + 1}valor da lista "B": '))
soma = [''] * valorN
for z in range(valorN):
    soma[z] = a[z] + b[z]
print(f'A soma entre as litas A e B: {soma}')