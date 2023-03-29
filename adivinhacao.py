# print("**************************************")
# print('Ola. Bem vindo ao jogo de advinhacao!')
# print("**************************************")
#
# numero_secreto = 42
#
# tentativa = input("Digite um numero: ")
# tentativa = int(tentativa)
#
# print("Voce digitou o numero ",tentativa)
#
# if(tentativa == numero_secreto):
#     print("Voce acertou o numero secreto!")
# else:
#     if(tentativa < numero_secreto):
#         print("Voce errou. O numero secreto e' maior que o numero sugerido por voce. Tente novamente.")
#     else:
#         print("Voce errou. O numero secreto e' menor que o numero sugerido por voce. Tente novamente.")



#
# print("**************************************")
# print('Ola. Bem vindo ao jogo de advinhacao!')
# print("**************************************")
#
# numero_secreto = 42
# total_de_tentativas = 3
# rodada = 1
#
# while(rodada <= total_de_tentativas):
#     print("Tentativa {} de {}".format(rodada, total_de_tentativas))
#     tentativa = input("Digite um numero: ")
#     tentativa = int(tentativa)
#     print("Voce digitou o numero ",tentativa)
#
#     acertou = tentativa == numero_secreto
#     maior = tentativa < numero_secreto
#     menor = tentativa > numero_secreto
#
#     if(acertou):
#         print("Voce acertou o numero secreto!")
#     else:
#         if(maior):
#             print("Voce errou. O numero secreto e' maior que o numero sugerido por voce. Tente novamente.")
#         elif(menor):
#             print("Voce errou. O numero secreto e' menor que o numero sugerido por voce. Tente novamente.")
#
#     rodada = rodada + 1
#
#
#
# print("**************************************")
# print("Fim do jogo.")
# print("**************************************")

#
# print("**************************************")
# print('Ola. Bem vindo ao jogo de advinhacao!')
# print("**************************************")
#
# numero_secreto = 42
# total_de_tentativas = 3
#
# for rodada in range(1,total_de_tentativas+1):
#     print("Tentativa {} de {}".format(rodada, total_de_tentativas))
#     tentativa = input("Digite um numero entre 1 e 100: ")
#     tentativa = int(tentativa)
#     print("Voce digitou o numero ",tentativa)
#
#     if(tentativa < 1 or tentativa > 100):
#         print("Voce deve digitar um numero entre 1 e 100!")
#         continue
#
#     acertou = tentativa == numero_secreto
#     maior = tentativa < numero_secreto
#     menor = tentativa > numero_secreto
#
#     if(acertou):
#         print("Voce acertou o numero secreto!")
#         break
#     else:
#         if(maior):
#             print("Voce errou. O numero secreto e' maior que o numero sugerido por voce. Tente novamente.")
#         elif(menor):
#             print("Voce errou. O numero secreto e' menor que o numero sugerido por voce. Tente novamente.")
#
#
#
# print("**************************************")
# print("Fim do jogo.")
# print("**************************************")

import random

def jogar():

    print("*******************************************")
    print('** Ola. Bem vindo ao jogo de advinhacao! **')
    print("*******************************************")

    print("Qual o nivel de dificuldade?")
    print("(0) Muito facil \n(1) Facil \n(2) Medio \n(3) Dificil ")
    nivel = int(input("Defide o nivel: "))

    if(nivel==0):
        total_de_tentativas = 20
    elif(nivel==1):
        total_de_tentativas = 15
    elif(nivel==2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    numero_secreto = random.randrange(1,101)
    pontos = 1000

    for rodada in range(1,total_de_tentativas+1):
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))
        tentativa = input("Digite um numero entre 1 e 100: ")
        tentativa = int(tentativa)
        print("Voce digitou o numero ",tentativa)

        if(tentativa < 1 or tentativa > 100):
            print("Voce deve digitar um numero entre 1 e 100!")
            continue

        acertou = tentativa == numero_secreto
        maior = tentativa < numero_secreto
        menor = tentativa > numero_secreto

        if(acertou):
            print("Voce acertou o numero secreto!")
            print("Sua pontuacao final foi de {} pontos".format(pontos))
            break
        else:
            pontos_perdidos = abs(numero_secreto - tentativa)
            pontos = pontos - pontos_perdidos
            if(maior):
                print("Voce errou. O numero secreto e' maior que o numero sugerido por voce. Tente novamente.")
            elif(menor):
                print("Voce errou. O numero secreto e' menor que o numero sugerido por voce. Tente novamente.")
            print("Sua pontuacao atual e' {} pontos".format(pontos))

    #print("Precione C para uma nova tentantiva ou Q para parar o jogo.")

    print("**************************************")
    print("***********  Fim do jogo.  ***********")
    print("**************************************")

if(__name__ == "__main__"):
    jogar()