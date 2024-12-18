#1
def main(tupla):
    print("Dias da Semana: ", tupla[0])
    print("Meses do Ano: ", tupla[1])
    print("Estações do Ano: ", tupla[2])
#2 
def main2(lista2):
    print("Dias da Semana: ", lista2[0])
    print("Meses do Ano: ", lista2[1])
    print("Estações do Ano: ", lista2[2])

#3
def imprimir(lista3):
    print(f"Quantos elementos: Há {len(lista3)} elementos nessa lista.")
    print(f"Dados: 1º - {lista3[0]}, 3º - {lista3[2]}, {len(lista3)}º - {lista3[-1]}")

#4
def questao4():
    lista4 = [ "Arroz", "Feijão", "Macarrão", "Frango", "Pão", "Leite", "Ovos", "Queijo", "Manteiga", "Açúcar", "Café", "Sal", "Óleo", "Alface", "Tomate"]

    def incluir_item():
        while True:
            novo_item = input("Digite o item que deseja incluir (ou digite 'PRONTO' para finalizar): ").strip().title()
            if novo_item.lower() == "pronto":
                break
            lista4.append(novo_item)
        exibir_lista(lista4)

    def remover_item():
        exibir_lista(lista4)
        item_para_remover = input("Digite o nome do item que deseja remover: ").strip().title()
        if item_para_remover in lista4:
            lista4.remove(item_para_remover)
            print(f"O item '{item_para_remover}' foi removido com sucesso!")
        else:
            print("Este item não está na lista.")
        exibir_lista(lista4)

    def atualizar_item():
        exibir_lista(lista4)
        item_para_atualizar = input("Digite o nome do item que deseja atualizar: ").strip().title()
        if item_para_atualizar in lista4:
            novo_valor = input(f"Digite o novo valor para o item '{item_para_atualizar}': ").strip().title()
            indice = lista4.index(item_para_atualizar)
            lista4[indice] = novo_valor
            print(f"O item '{item_para_atualizar}' foi atualizado para '{novo_valor}'.")
        else:
            print("Este item não está na lista.")
        exibir_lista(lista4)

    def menu():
        while True:
            print("\nEscolha uma das opções:")
            print("1 - Incluir um novo item")
            print("2 - Remover um item")
            print("3 - Atualizar um item existente")
            print("4 - Exibir lista")
            print("5 - Encerrar o programa")
            opcao = input("Digite o número da opção desejada: ").strip()
            if opcao == "1":
                incluir_item()
            elif opcao == "2":
                remover_item()
            elif opcao == "3":
                atualizar_item()
            elif opcao == "4":
                exibir_lista(lista4)
            elif opcao == "5":
                print("Programa encerrado. Até logo!")
                break
            else:
                print("Opção inválida. Tente novamente.")
    menu()

#6
def adivinhar_linguagem_oculta():
    print('Adivinhe as linguagens que constam na lista oculta! (Quando quiser encerrar digite "SAIR").')
    while True:
        tentativa = input("Sua tentativa: ").strip().title()
        if tentativa in linguagens_ocultas:
            print(f"A linguagem {tentativa} consta na lista!")
        elif tentativa.lower() == "sair":
            print("--- Programa encerrado ---")
            break
        else:
            print(f"A linguagem {tentativa} não consta na lista!")





















