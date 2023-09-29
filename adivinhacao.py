import random

def jogar_adivinhacao():
        print("************************************")
        print("* Bem vindo ao jogo de Adivinhação *")
        print("************************************")

        numero_secreto  =  round(random.randrange(1,101))
        total_tentativas = 3
        print(numero_secreto)

        for rodada in range(1, total_tentativas +1):
            print("tentativa {} de {}".format(rodada,total_tentativas))
            chute_str = input("digite um  número entre 1 e 100: ")
            print("vc digitou o ",chute_str)
            chute = int(chute_str)
            if chute < 1 or chute > 100:
                print("número entre 1 e 100")
                continue

            acertou = chute == numero_secreto
            maior   = chute  > numero_secreto
            menor   = chute  < numero_secreto

            if(acertou):
                print("acertou")
                break
            else:
                if(maior):
                    print("o seu chute foi maior que o numero secreto")
                elif (menor):
                    print("o seu chute foi menor que o numero secreto")

        print("Fim do jogo")

if(__name__=="__main__"):
    jogar_adivinhacao()
