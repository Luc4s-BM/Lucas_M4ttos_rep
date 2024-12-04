import random
def iniciar_jogo():
    numero_aleatorio = random.randint(1, 10)
    chute = 0
    print("Tente adivinhar o número gerado!")
    print("Você tem 5 chances para acertar o número de 1 à 10.")
    chances = 5
    def adivinhar_numero(numero):
        nonlocal chances
        if numero == numero_aleatorio:
            print(f"Parábens, você acertou! Era o número {numero_aleatorio}")
            jogar_de_novo()
        elif numero > 10 or numero < 1:
            print("Digite um número dentro do que foi solicitado! Dentro de 1 à 10!")
        else:
            chances -= 1
            print("Errou, tente novamente!") 
        if chances == 0:
            print(f"Que pena! Acabou suas chances! Era o número {numero_aleatorio}")
            jogar_de_novo()
    while numero_aleatorio != chute:
        chute = int(input("Sua tentativa: "))
        adivinhar_numero(chute)
def jogar_de_novo():
    escolha = input("Você deseja jogar de novo?: ").strip().lower()
    if escolha == "sim":
        iniciar_jogo()
iniciar_jogo()
jogar_de_novo()