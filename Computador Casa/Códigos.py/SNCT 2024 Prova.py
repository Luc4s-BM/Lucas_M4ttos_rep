import random

def avaliar_entrada_de_dadosINT(valor):
    try:
        return int(valor)
    except ValueError:
        return None

def cadastrar_evento():
    while True:
        nome_do_evento = input("Qual o nome do evento que você quer cadastrar?: ").strip()
        if any(char.isdigit() for char in nome_do_evento):
            print("O nome do evento não pode conter números. Tente novamente.")
        elif nome_do_evento == "":
            print("O nome do evento não pode estar vazio. Tente novamente.")
        else:
            break
    
    while True:
        capacidade_maxima_do_evento = input("Qual a quantidade máxima de pessoas desse evento?: ").strip()
        capacidade_valida = avaliar_entrada_de_dadosINT(capacidade_maxima_do_evento)
        
        if capacidade_valida is not None:
            participantes_aleatorios = random.randint(0, capacidade_valida)
            vagas_restantes = capacidade_valida - participantes_aleatorios
            print(f"Evento '{nome_do_evento}' cadastrado com capacidade para {capacidade_valida} pessoas.")
            print(f"Já temos {participantes_aleatorios} participantes cadastrados. Vagas restantes: {vagas_restantes}.")
            return nome_do_evento, vagas_restantes
        else:
            print("Digite uma quantidade válida! Apenas números inteiros são permitidos.")

def se_auto_cadastrar_nos_eventos(eventos):
    print("\n--- Escolha um evento para se cadastrar ---\n")
    for i, evento in enumerate(eventos, start=1):
        print(f"{i}. {evento[0]} (Vagas restantes: {evento[1]} pessoas)")
    
    while True:
        escolha = input("Digite o número do evento em que deseja se cadastrar: ").strip()
        escolha_valida = avaliar_entrada_de_dadosINT(escolha)
        
        if escolha_valida is not None and 1 <= escolha_valida <= len(eventos):
            evento_escolhido = eventos[escolha_valida - 1]
            if evento_escolhido[1] > 0:
                eventos[escolha_valida - 1] = (evento_escolhido[0], evento_escolhido[1] - 1)
                print(f"Você se cadastrou no evento: {evento_escolhido[0]}!")
                print(f"Vagas restantes no evento: {eventos[escolha_valida - 1][1]}")
            else:
                print("Este evento não possui vagas disponíveis.")
            break
        else:
            print("Opção inválida. Por favor, escolha um número válido.")
        
"""def excluir_alunos_do_evento(alunos1):
    while True:    
        escolha_do_evento_pra_excluir = input("Qual evento você deseja excluir os alunos dela?: ").strip().lower()
        if escolha_do_evento_pra_excluir in eventos:
            escolha_excluir_aluno = input(f"Você realmente deseja excluir os alunos do evento {evento}?: ").strip().lower()
            if escolha_excluir_aluno == "sim":
                print(f"{participantes_aleatorios} alunos removidos do evento {evento}")
                break
            elif escolha_excluir_aluno == "não" or escolha_excluir_aluno == "nao":
                print("")
        else:
            print(f"O evento {evento} não está cadastrado.")

def menu():
    print("Qual opção você deseja executar?\n1 - Cadastrar algum evento.\n2 - Se auto-cadastrar em algum evento.\n3 - Excluir alunos de algum evento.\n4 - Excluir um evento da lista de eventos.")
    escolha = int(input("Digite sua escolha: "))
    if escolha == 1:
        cadastrar_evento()
    elif escolha == 2:
        se_auto_cadastrar_nos_eventos()   
    elif escolha == 3:
        excluir_alunos_do_evento()
    elif escolha == 4:"""
