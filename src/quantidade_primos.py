def primo (numero):
    cont = 1
    primo = 0
    while cont <= numero:
        if numero % cont == 0:
            primo = primo + 1
        cont = cont + 1
    if primo == 2:
        return True
    else:
        return False
    
def n_primos(x):
    quantidade = 0
    for i in range(0,x):
        if primo(i) == True:
            quantidade+=1
    if x == 2:
        quantidade = 1
    return quantidade

