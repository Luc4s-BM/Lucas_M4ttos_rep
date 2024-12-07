import time
import random

def mostrar_mensagens():
    mensagens = ["Aguarde", "Aguarde.", "Aguarde..", "Aguarde..."]
    for mensagem in mensagens:
        print(mensagem, end='\r')
        time.sleep(0.5)

def validar_entrada_numerica(mensagem, limite_max):
    while True:
        valor = input(mensagem).strip()
        if valor.isnumeric():
            valor = int(valor)
            if 0 <= valor <= limite_max:
                return valor
            else:
                print(f"Por favor, digite um número entre 0 e {limite_max}.")
        else:
            print("Entrada inválida! Digite apenas números.")

def calcular_preco(quantidade_de_pessoas, custo_fixo, custo_variavel_por_pessoa, buffet_livre, margem_lucro):
    preco = (custo_fixo + 
             (quantidade_de_pessoas * custo_variavel_por_pessoa) + 
             (quantidade_de_pessoas * buffet_livre)) * (1 + margem_lucro)
    return preco

def iniciar_reserva():
    resposta_sim = {"sim", "s", "claro", "com certeza", "afirmativo", "positivo", "ok", "yes"}
    custo_fixo = 200
    custo_variavel_por_pessoa = 20
    margem_lucro = 0.1
    buffet_livre = 40

    print("Bem-vindo ao site do restaurante Formaggio!")
    reserva_online = input("Você gostaria de fazer uma reserva online? (Sim/Não): ").strip().lower()

    mostrar_mensagens()

    if reserva_online in resposta_sim:
        print("\nÓtimo! Continue com sua reserva:")
        print(f"-> Custo fixo inicial: R${custo_fixo:.2f}")
        print(f"-> Custo variável por pessoa (Crianças abaixo de 10 anos não são cobradas): R${custo_variavel_por_pessoa:.2f}")
        print(f"-> Buffet livre por pessoa: R${buffet_livre:.2f}")
        print(f"-> Taxa de 10% inclusa no valor final.")
        
        quantidade_de_pessoas = validar_entrada_numerica("Quantas pessoas participarão da reserva? (MÁX. 30): ", 30)
        quantidade_de_criancas = validar_entrada_numerica("Quantas crianças menores de 10 anos estarão na reserva?: ", quantidade_de_pessoas)

        mostrar_mensagens()

        adultos_pagantes = quantidade_de_pessoas - quantidade_de_criancas
        preco_total = calcular_preco(adultos_pagantes, custo_fixo, custo_variavel_por_pessoa, buffet_livre, margem_lucro)

        print(f"\nO preço final será R${preco_total:.2f} para {quantidade_de_pessoas} pessoas.")
        confirmacao = input("As informações estão corretas? (Sim/Não): ").strip().lower()

        if confirmacao in resposta_sim:
            nome_cliente = input("Digite seu nome: ").strip().capitalize()
            pin = random.randint(1000, 9999)
            print(f"\nReserva confirmada! Nome: {nome_cliente}, PIN: {pin}.")
        else:
            print("Ok, reinicie o processo para corrigir as informações.")
    else:
        print("Ok, tenha um bom dia!")

iniciar_reserva()
