numero = int(input('Digite um número: '))
temp = str(numero)
tamanho = len(temp)
i = 1
n = numero % 10
soma = n
while tamanho >= 0 :
    n = (numero // (10*i)) % 10 
    soma += n
    i*= 10
    tamanho = tamanho - 1
print(soma)