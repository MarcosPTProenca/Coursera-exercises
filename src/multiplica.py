def fazfatorial(x):
    fatorial = 1
    if x == 0:
        return 1
    else: 
        while x >0:
            fatorial *= x
            x = x-1
        return fatorial
n = int(input("Escreva o número n: "))
k = int(input("Escreva o número k: "))

binomial = fazfatorial(n)//(fazfatorial(k)*fazfatorial(n-k))

print(binomial)