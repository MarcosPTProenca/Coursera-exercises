def remove_repetidos(lista):
    lista.sort()
    count = 0
    for i in lista:
        for j in lista:
            if i == j:
                count += 1
                if count > 1:
                    for k in range(count-1):
                        del lista[lista.index(i)]
        count = 0
    return sorted(lista)
lista = [1,2,1,3,4,7,10]
print(remove_repetidos(lista))