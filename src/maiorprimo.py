def primo (x):
    cont = 1
    primo = 0
    while cont <= x:
        if x % cont == 0:
            primo = primo + 1
        cont = cont + 1
    if primo == 2:
        return x
    else:
        return False

def maior_primo(x):
    primos = []
    while x > 0:
        if primo(x) != False:
            primos.append(primo(x))
        x = x -1
    primos.sort
    return primos[0]
