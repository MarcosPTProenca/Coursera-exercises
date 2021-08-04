n = int(input('Digite o valor de n: '))
fatorial = 1
if n == 0:
    print(1)
else: 
    while n >0:
        fatorial *= n
        n = n-1
    print(fatorial)