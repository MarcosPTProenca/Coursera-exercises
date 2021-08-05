def soma_elementos(lista):
    soma = 0
    for i in lista:
        soma += i
    return soma

lista = [2, 4, 2, 2, 3, 3, 1]
print(soma_elementos(lista))