import math

print('Dada a equação do segundo grau: ax² + bx + c = 0')
a = float(input('Digite o valor do coeficiente a: '))
b = float(input('Digite o valor do coeficiente b: '))
c = float(input('Digite o valor do coeficiente c: '))

delta = (b**2)-4*a*c

if delta > 0:
    x1 = (-b+math.sqrt(delta))/(2*a)
    x2 = (-b-math.sqrt(delta))/(2*a)
    if x1 < x2:
        print(f'as raízes da equação são {x1} e {x2} ')
    else:
        print(f'as raízes da equação são {x2} e {x1} ')
elif delta == 0:
    x = (-b)/(2*a)
    print(f'a raiz desta equação é {x} ')
else:
    print('esta equação não possui raízes reais')
