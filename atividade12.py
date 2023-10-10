# Escreva um algoritmo que solicite ao
# usuário a entrada de 5 nomes, e que exiba
# a lista desses nomes na tela.
# Após exibir essa lista, o programa deve
# mostrar também os nomes na ordem
# inversa em que o usuário os digitou, um
# por linha.

nomes = ['']*2

for a in range(2):
    nomes[a] = input(f'Informe o {a + 1} Nome: ')
nomes.sort(reverse=True)  #Vai de Z a A
print(nomes)