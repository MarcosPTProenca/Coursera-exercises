def digital_root(n):
    temp = str(n)
    tamanho = len(temp)
    i=1
    j=1
    soma = 0
    soma1 = 0
    if tamanho <= 2:
        while tamanho > 0:
            x = (n//i) %10
            soma += x
            i*=10
            tamanho = tamanho - 1
        return soma
    else: 
        while tamanho > 0:
            x = (n//i) %10
            soma += x
            i*=10
            tamanho = tamanho - 1   
        temp = str(soma)
        tamanho2 = len(temp)
        while tamanho2 >0:
            x = (soma//j) %10
            soma1 += x
            j*=10 
            tamanho2 = tamanho2 - 1
        soma1 = digital_root(soma1)
        return soma1

print(digital_root(16))