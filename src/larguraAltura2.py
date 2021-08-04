largura = int(input("digite a largura: "))
altura = int(input("digite a altura: "))

for j in range (0,altura):
    if j == 0 or j == altura-1:
        for i in range (0,largura):
            print("#", end="")
    else:
        print("#", end="")
        for i in range (1,largura-1):
            print(" ", end="")
        print("#", end="")
    print()