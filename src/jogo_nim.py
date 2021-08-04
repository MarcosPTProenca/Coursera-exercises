def computador_escolhe_jogada(n,m):
    if n <= m:
        print(f"O computador retirou {n} peças")
        print(f"Agora restam {n-n} peças no tabuleiro\n")
        return n
    else:
        jogada = n%(m+1)
        if jogada> 0:
            print(f"O computador retirou {jogada} peças")
            print(f"Agora restam {n-jogada} peças no tabuleiro\n")
            return jogada
        print(f"O computador retirou {m} peças")
        print(f"Agora restam {n-m} peças no tabuleiro\n")
        return m
def usuario_escolhe_jogada(n,m):
   jogada = int(input("Quantas peças você vai tirar? "))
   print("\n")
   while jogada == 0 or jogada>m or jogada > n or jogada<0:     
       print("Oops! Jogada inválida! Tente de novo.\n")
       jogada = int(input("Quantas peças você vai tirar? "))
   print(f"Você retirou {jogada} peças")
   print(f"Agora restam {n-jogada} peças no tabuleiro\n")
   return jogada
           
def partida():
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))
    print("\n")
    usuario_ganhou = 1
    computador_ganhou = 2
    if (n % (m+1)) == 0:
        print("Você começa!\n")
        n = n-usuario_escolhe_jogada(n,m)
        vez_usuario = False
    else:
        print("Computador começa!\n")
        n = n-computador_escolhe_jogada(n,m)
        vez_usuario = True
    while n > 0:
        if vez_usuario == True:
            n = n-usuario_escolhe_jogada(n,m)
            vez_usuario = False
            if n == 0:
                print("Fim do jogo! Voce ganhou!\n")
                return usuario_ganhou
        elif vez_usuario == False:
            n = n-computador_escolhe_jogada(n,m)
            vez_usuario = True
            if n == 0:
                print("Fim do jogo! O computador ganhou!\n")
                return computador_ganhou
def main():
    print("Bem-vindo ao jogo do NIM! Escolha: \n")
    computador = 0
    usuario = 0
    while True: 
        resposta = int(input("1 - para jogar uma partida isolada\n2 - para jogar um campeonato "))
        print("\n")
        if resposta == 1:
            print("Você escolheu uma partida isolada!\n")
            partida()
            break
        elif resposta == 2:
            print("Você escolheu um campeonato!\n")
            for i in range(0,3):
                print(f"**** Rodada {i+1} ****")
                x = partida()
                if x == 2:
                    computador +=1
                elif x == 1:
                    usuario +=1
            print("**** Final do campeonato! ****\n")
            print(f"Placar: Você {usuario} X {computador} Computador")
            break
        else:
            False
            
main()

            
            
            
            
            
            