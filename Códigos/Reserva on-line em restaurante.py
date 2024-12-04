import time
import random
class all:
    def iniciar_reserva():

        resposta_sim = {"sim", "s", "claro", "com certeza", "afirmativo", "positivo", "exatamente", "certamente", "ok", "okay", "óbvio", "pode ser", "concordo", "isso mesmo", "isso aí", "combinado", "está certo", "beleza", "verdade", "pois é", "sem dúvida", "lógicom", "si", "sm", "im", "yes", "sure", "mis"}

        custo_fixo = 200
        custo_variavel_por_pessoa = 20
        margem_lucro = 10 / 100
        buffet_livre = 40

        print("Bem vindo, ao site do restaurante Formaggio!")
        reserva_online = input("Você gostaria de fazer uma reserva on-line?: ").strip().lower()
        mensagens = ["Aguarde", "Aguarde.", "Aguarde..", "Aguarde..."]
        for i in range(2):  
            for mensagem in mensagens:
                print(mensagem, end='\r')  
                time.sleep(0.5)
        if reserva_online in resposta_sim:
            print("Ótimo! Continue com sua reserva: ")
            print("Aqui está a nossa tabela de preços:")
            time.sleep(0.5)
            print(f"-> Custo fixo inicial: R${custo_fixo:.2f}.")
            time.sleep(0.5)
            print(f"-> Custo fixo por pessoa (Crianças abaixo de 10 anos não são cobradas): R${custo_variavel_por_pessoa:.2f}.")
            time.sleep(0.5)
            print(f"-> Buffet livre (Por pessoa): R${buffet_livre:.2f}.")
            time.sleep(0.5)
            print(f"-> 10% de taxas.")
            quantidade_de_pessoas = 0
            time.sleep(1.0)
            while True:
                quantidade_de_pessoas = input("Quantas pessoas participaram da reserva? (MÁX.30): ")
                quantidade_de_criancas = input("Quantas crianças menores de 10 anos de idade participaram da reserva?: ")
                for i in range(2):  
                    for mensagem in mensagens:
                        print(mensagem, end='\r')  
                        time.sleep(0.5)
                if quantidade_de_pessoas.isnumeric() and quantidade_de_criancas.isnumeric():
                    quantidade_de_pessoas = int(quantidade_de_pessoas)
                    quantidade_de_criancas = int(quantidade_de_criancas)
                    if quantidade_de_pessoas > 0 and quantidade_de_pessoas <= 30:
                        if quantidade_de_pessoas == 1:
                            print(f"OK, apenas {quantidade_de_pessoas} pessoa participará da reserva!")
                        elif quantidade_de_pessoas % 2 != 0 and quantidade_de_pessoas > 4:
                            print("Parece que o número de pessoas não se encaixa exatamente nas nossas mesas, não se preocupe, iremos adicionar uma mesa extra para você!")
                        else:
                            print(f"Perfeito, as {quantidade_de_pessoas} pessoas se encaixará em nossas mesas.")
                        break
                    elif quantidade_de_pessoas == 0:
                        for i in range(2):  
                            for mensagem in mensagens:
                                print(mensagem, end='\r')  
                                time.sleep(0.5)
                        print("Por favor, digite um número de pessoas válido!")
                    else:
                        for i in range(2):  
                            for mensagem in mensagens:
                                print(mensagem, end='\r')  
                                time.sleep(0.5)
                        print("Desculpe, mas nosso limite de pessoas por reserva é apenas 30!")
                        print(f"Não poderemos acolher {quantidade_de_pessoas} pessoas!")
                        print("Se ainda deseja fazer a reserva, digite um valor válido!")
                else: 
                    for i in range(2):  
                        for mensagem in mensagens:
                            print(mensagem, end='\r')  
                            time.sleep(0.5)
                    print("Digite um valor válido!")
            quantidade_de_pessoas = quantidade_de_pessoas - quantidade_de_criancas
            preco_total = (custo_fixo + (buffet_livre * quantidade_de_pessoas) + (custo_variavel_por_pessoa * quantidade_de_pessoas)) * (1 + margem_lucro)
            print(f"OK, o preço final vai ficar R${preco_total:.2f}, com {quantidade_de_pessoas + quantidade_de_criancas} pessoas.")
            while True:
                confirmacao = str(input(f"Confirme suas informações:\n-> Quantidade de pessoas: {quantidade_de_pessoas + quantidade_de_criancas}.\n-> Quantidade de crianças com menos de 10 anos de idade: {quantidade_de_criancas}.\n-> Valor final: R${preco_total:.2f}.\nAs informações estão corretas?: ")).strip().lower()
                break

            if confirmacao in resposta_sim:
                for i in range(5):  
                    for mensagem in mensagens:
                        print(mensagem, end='\r')  
                        time.sleep(0.5)
                nome_cliente = ""
                while True:
                    nome_cliente = input("Digite seu nome: ").strip()
                    if nome_cliente.isalpha():
                        confirmar_nome_cliente = input("Confirme seu nome: ").strip()
                        if nome_cliente == confirmar_nome_cliente:
                            break
                        else:
                            print("Parece que os nomes estão diferentes!")
                    else:
                        print("Digite um nome válido!")

                pin = random.randint(1000, 9999)
                print("Pronto, apenas lembre do seu PIN: ", pin)
                print(f"Suas informações: Nome: {nome_cliente} - PIN: {pin}")
            else:
                print("Ok, voltaremos ao começo para que você corrija as suas informações.")
        else:
            print("Ok, tenha um bom dia!")
    iniciar_reserva() 