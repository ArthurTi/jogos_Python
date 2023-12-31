import random

def jogar_forca():
        print("************************************")
        print("* Bem vindo ao jogo de forca *")
        print("************************************")

        arquivo =  open("palavra.txt", "r")
        palavras = []
        for linha in arquivo:
                linha =  linha.strip()
                palavras.append(linha)

        arquivo.close()

        numero =  random.randrange(0,len(palavras))
        palavra_secreta = palavras[numero].upper()  #colocando a palara em maiusculo


        letras_acertadas = ["_" for letra in palavra_secreta]


        enforcou = False
        acertou =  False
        erros = 0


        while(not enforcou and not acertou):
                chute = input("qual a letra? ")
                chute = chute.strip().upper()

                if(chute in palavra_secreta):
                        index = 0
                        for letra in palavra_secreta:
                                if(chute == letra):
                                        letras_acertadas[index] = letra

                                index += 1

                else :
                     erros += 1

                enforcou  =  erros == 6
                acertou =  "_"  not in letras_acertadas

                print(letras_acertadas)


        if(acertou):
                print("parabens, vc ganhou!!!")

        else:
                print("vc é burrão")

        print("Fim do jogo")

if(__name__=="__main__"):
        jogar_forca()