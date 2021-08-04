def maximo(x,y,z):
    if x > y and x > z:
        return x
    elif y > x and y > z:
        return y
    elif z > x and z > y:
        return z
    else:
        return x
def testes():
    if maximo(30,14,10) == 30:
        print ('Funcionou')
    else: 
        print ('Não funcionou')
    if maximo(0,-1, 1) == 1:
        print ('Funcionou')
    else: 
        print ('Não funcionou')
testes()