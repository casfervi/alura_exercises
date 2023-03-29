import random

def jogar():

    imprime_abertura()
    palavra_secreta = carrega_palavra_secreta()
    letras_acertadas = ["_"]*len(palavra_secreta) # letras_acertadas = ["_" for letra in palavra_secreta]

    print("A palavra secreta possui {} letras.".format(len(palavra_secreta)))

    #numero_tentativas = int(input("Voce quer quantas tentativas pra  tentar acertar a palavra secreta? "))
    numero_tentativas = 7
    letras_chutadas = []

    enforcou = False
    erros = 0

    while(not enforcou):
        chute = input("Qual a letra? ").upper().strip()

        if(chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if(chute == letra):
                    letras_acertadas[index] = letra
                    print("Encontrei a letra {} na posicao {}.".format(letra,index+1))
                index += 1
            print(letras_acertadas)
            if(letras_acertadas.count("_") != 0):
                print("Ainda faltam {} letras.".format(letras_acertadas.count("_")))
            else:
                imprime_mensagem_vencedor()
                break
        elif(chute in letras_chutadas):
            print("Voce ja' tentou a letra {}. Tente outra letra.".format(chute))
        else:
            erros += 1
            desenha_forca(erros)
            enforcou = erros == numero_tentativas
            letras_chutadas.append(chute)
            if(enforcou):
                imprime_mensagem_perdedor(palavra_secreta)
            elif(erros == numero_tentativas-1):
                print("Nao tem a letra {} na palavra secreta.".format(chute))
                print("Voce ainda tem {} tentativa.".format(numero_tentativas - erros))
                print(letras_acertadas)
            else:
                print("Nao tem a letra {} na palavra secreta.".format(chute))
                print("Voce ainda tem {} tentativas.".format(numero_tentativas - erros))
                print(letras_acertadas)

def imprime_abertura():
    print("**************************************")
    print("** Ola. Bem vindo ao jogo de Forca! **")
    print("**************************************")

def carrega_palavra_secreta():
    with open("palavras.txt", "r") as arquivo:
        palavras = []
        for linha in arquivo:
            linha = linha.strip()
            palavras.append(linha)
    palavra_secreta = palavras[random.randrange(0, len(palavras))].upper()
    return palavra_secreta

def imprime_mensagem_perdedor(palavra_secreta):
    print("Voce nao conseguiu acertar a palavra secreta.")
    print("A palavra secreta era {}.".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

def imprime_mensagem_vencedor():
    print("Voce acertou todas as letras. Parabens!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")
    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

if(__name__ == "__main__"):
    jogar()
