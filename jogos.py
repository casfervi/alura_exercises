import forca
import adivinhacao

def escolhe_jogo():
    print("*****************************************")
    print("***********Escolha o seu jogo!***********")
    print("*****************************************")

    print("(1) Para o jogo da Forca \n(2) Para o jogo da adivinhacao")

    jogo = int(input("Qual jogo voce quer jogar? "))

    if(jogo==1):
        print("Jogando forca")
        forca.jogar()
    elif(jogo==2):
        print("Jogando adivinhacao")
        adivinhacao.jogar()

if(__name__ == "__main__"):
    escolhe_jogo()