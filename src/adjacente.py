print("Verifica se o número tem dois digitos adjacentes iguais")
numero = int(input('Digite um número inteiro: '))
temp = str(numero)
tamanho = len(temp)
i = 1
n = numero
n = (numero // i) % 10
x = (numero // (10*i)) % 10
adjacente = False
if tamanho == 1:
    print('não')
else:
    while tamanho > 0 :
        if n == x:
            adjacente = True
        n = (numero // i) % 10 
        x = (numero // (10*i)) % 10
        i*= 10
        tamanho = tamanho - 1
    if adjacente == True:
        print('sim')
    else:
        print('não')