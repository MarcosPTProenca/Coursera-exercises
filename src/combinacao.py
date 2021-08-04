def fatorial (x):
    n = 1
    if x == 0:
        return 1
    else:
        while x > 0:
            n *= x
            x = x-1
        return n
def combinacao (x,y):
    return fatorial(x)/(fatorial(y)*fatorial(x-y))
def fdb (n,defe,p):
    return combinacao(n,defe)*(p**defe)*(1-p)**(n-defe)
n = 67
p = 0.31
i = 17
pt = 0
while i <= 67:
    pt += fdb(n,i,p)
    i=i+1
pt = pt*100
print (f'{pt}%')