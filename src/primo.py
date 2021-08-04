numero = int(input('Digite um numero inteiro: '))
cont = 1
primo = 0
while cont <= numero:
    if numero % cont == 0:
        primo = primo + 1
    cont = cont + 1
if primo == 2:
    print ('primo')
else:
    print('não primo')
