import adivinhacao
import Forca
def escolha_jogo():
    print("************************************")
    print("******* Escolha o seu jogo *********")
    print("************************************")
    print("1 forca, 2 advinhação")

    escolha = int(input("qual jogo? "))


    if(escolha == 1):
        Forca.jogar_forca()

    elif(escolha == 2):
        adivinhacao.jogar_adivinhacao()

if(__name__=="__main__"):
    escolha_jogo()