import random

def jogo_adivinhar_numero():
    # Define o número a ser adivinhado
    numero_escolhido = random.randint(1, 100)
    
    tentativas = 0
    adivinhou = False

    print("Bem-vindo ao jogo de adivinhar o número!")
    print("Estou pensando em um número entre 1 e 100.")

    # Loop do jogo
    while not adivinhou:
        # Solicita ao usuário que adivinhe o número
        tentativa = int(input("Tente adivinhar o número: "))
        tentativas += 1

        # Verifica se a tentativa está correta
        if tentativa < numero_escolhido:
            print("O número é maior do que isso. Tente novamente!")
        elif tentativa > numero_escolhido:
            print("O número é menor do que isso. Tente novamente!")
        else:
            adivinhou = True
            print(f"Parabéns! Você adivinhou o número em {tentativas} tentativas.")
            print("Obrigado por jogar!")

# Executa o jogo
jogo_adivinhar_numero()
