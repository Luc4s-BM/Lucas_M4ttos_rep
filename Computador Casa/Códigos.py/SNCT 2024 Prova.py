import random

def avaliar_entrada_de_dadosINT(valor):
    try:
        return int(valor)
    except ValueError:
        return None

def cadastrar_evento(nome_do_evento, capacidade_maxima, eventos):
    if any(char.isdigit() for char in nome_do_evento) or not nome_do_evento.strip():
        return None, "O nome do evento é inválido. Ele não pode conter números ou estar vazio."
    
    capacidade_valida = avaliar_entrada_de_dadosINT(capacidade_maxima)
    if capacidade_valida is None or capacidade_valida <= 0:
        return None, "A capacidade máxima deve ser um número inteiro positivo."
    
    participantes_aleatorios = random.randint(0, capacidade_valida)
    vagas_restantes = capacidade_valida - participantes_aleatorios
    eventos.append((nome_do_evento, vagas_restantes))
    return (nome_do_evento, vagas_restantes), f"Evento '{nome_do_evento}' cadastrado com sucesso."

def se_auto_cadastrar_nos_eventos(eventos, escolha):
    escolha_valida = avaliar_entrada_de_dadosINT(escolha)
    if escolha_valida is None or not (1 <= escolha_valida <= len(eventos)):
        return eventos, "Opção inválida. Por favor, escolha um número válido."
    
    evento_escolhido = eventos[escolha_valida - 1]
    if evento_escolhido[1] > 0:
        eventos[escolha_valida - 1] = (evento_escolhido[0], evento_escolhido[1] - 1)
        return eventos, f"Você se cadastrou no evento: {evento_escolhido[0]}! Vagas restantes: {eventos[escolha_valida - 1][1]}"
    else:
        return eventos, "Este evento não possui vagas disponíveis."

def excluir_alunos_do_evento(nome_evento, eventos):
    for i, evento in enumerate(eventos):
        if evento[0].lower() == nome_evento.lower():
            eventos[i] = (evento[0], evento[1])
            return eventos, f"Todos os participantes foram removidos do evento '{evento[0]}'."
    return eventos, f"O evento '{nome_evento}' não foi encontrado."

def excluir_eventos_da_lista(nome_evento, eventos):
    for evento in eventos:
        if evento[0].lower() == nome_evento.lower():
            eventos.remove(evento)
            return eventos, f"O evento '{nome_evento}' foi excluído com sucesso."
    return eventos, f"O evento '{nome_evento}' não foi encontrado."

def exibir_lista():
    for i,scnt_eventos in enumerate(eventos, start=1):
        print(f"Nome do evento: {i} - Capacidade máxima: {scnt_eventos}")

eventos = []

while True:
    print("Qual opção você deseja executar?")
    print("1 - Cadastrar algum evento.")
    print("2 - Se auto-cadastrar em algum evento.")
    print("3 - Excluir alunos de algum evento.")
    print("4 - Excluir um evento da lista de eventos.")
    print("5 - Exibir lista de eventos.")
    print("6 - Sair")

    opcao = input("Digite sua escolha: ").strip()
    if opcao == "1":
        nome_do_evento = input("Qual o nome do evento que você quer cadastrar?: ").strip()
        capacidade_maxima = input("Qual a quantidade máxima de pessoas desse evento?: ").strip()
        _, mensagem = cadastrar_evento(nome_do_evento, capacidade_maxima, eventos)
        print(mensagem)
    elif opcao == "2":
        if not eventos:
            print("Nenhum evento disponível para se cadastrar.")
            continue
        print("\n--- Escolha um evento para se cadastrar ---")
        for i, evento in enumerate(eventos, start=1):
            print(f"{i}. {evento[0]} (Vagas restantes: {evento[1]})")
        escolha = input("Digite o número do evento em que deseja se cadastrar: ").strip()
        eventos, mensagem = se_auto_cadastrar_nos_eventos(eventos, escolha)
        print(mensagem)
    elif opcao == "3":
        nome_evento = input("Digite o nome do evento para excluir os alunos: ").strip()
        eventos, mensagem = excluir_alunos_do_evento(nome_evento, eventos)
        print(mensagem)
    elif opcao == "4":
        nome_evento = input("Digite o nome do evento para excluir da lista: ").strip()
        eventos, mensagem = excluir_eventos_da_lista(nome_evento, eventos)
        print(mensagem)
    elif opcao == "5":
        exibir_lista()
    elif opcao == "6":
        print("Encerrando o programa.")
        break
    else:
        print("Opção inválida. Tente novamente.")
