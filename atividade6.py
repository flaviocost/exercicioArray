# Faça um código para ler 5 números e
# armazenar em um vetor. Após a leitura
# total dos 5 números, o código deve
# escrever esses 5 números lidos na ordem
# inversa

lista = [0]*5
for x in range(5):
    valor = int(input(f'Informe o {x + 1}ª Valor: '))
    lista[x] = valor
    lista.sort(reverse=True)
print(lista)
