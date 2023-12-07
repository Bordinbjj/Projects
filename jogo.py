import random

def jogo_adivinhacao():
    numero_secreto = random.randint(1, 100)  
    tentativas = 0
    tentativas_maximas = 5  

    print("Bem-vindo ao jogo de adivinhação!")
    print("Tente adivinhar o número entre 1 e 100. Você tem 5 tentativas.")

    while tentativas < tentativas_maximas:
        tentativa = int(input("Digite o seu palpite: "))

        if tentativa < numero_secreto:
            print("Tente um número maior.")
        elif tentativa > numero_secreto:
            print("Tente um número menor.")
        else:
            print("Parabéns! Você acertou o número!")
            break

        tentativas += 1

    if tentativa != numero_secreto:
        print(f"Suas tentativas acabaram. O número secreto era {numero_secreto}.")

jogo_adivinhacao()
