lista = []
numero = int(input('Digite um número: '))
while numero != 0:
    lista.append(numero)
    numero = int(input('Digite um número: '))
for i in range(len(lista)-1,-1,-1):
    print(lista[i])