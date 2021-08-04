def soma_hipotenusas(n):
    soma = 0
    hipotenusa = []
    while n >= 1:
        for i in range (0,n):
            for j in range(0,n):
                if (i*i + j*j) == (n*n):
                    if n not in hipotenusa:
                        hipotenusa.append(n)
        n = n-1
    for k in hipotenusa:
        soma = soma + k
    return soma
