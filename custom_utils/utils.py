from custom_utils import utils

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

    def exibir_lista(lista):
        print("Aqui está sua lista atual: ")
        for i, lista in enumerate(lista, start= 1):
            print("- ", lista)
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
linguagens_ocultas = ["C", "C++", "JavaScript", "Java", "Lua", "Python"]
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

#7 
lista_de_medicos = ["lucas", "joão", "ana", "júlia", "guilherme"]

def imprimir_lista_medicos():
    for i, medico in enumerate(lista_de_medicos, start=1):
        print(f"{i}. {medico.capitalize()}")

def escolher_medico():
    while True:
        imprimir_lista_medicos()
        escolha = input("Digite o número ou o nome do médico: ")
        if escolha.isdigit():
            escolha = int(escolha)
            if 1 <= escolha <= len(lista_de_medicos):
                print(f"Consulta com o(a) médico(a) {lista_de_medicos[escolha-1].capitalize()} marcada!")
                break
            else:
                print("Número inválido! Tente novamente.")
        elif escolha.lower() in [medico.lower() for medico in lista_de_medicos]:
            print(f"Consulta com o(a) médico(a) {escolha.capitalize()} marcada!")
            break
        else:
            print("Digite um número ou nome válido!")

#8
produtos_precos = {
    "Arroz": 5.50, "Feijão": 7.30, "Macarrão": 4.20, "Frango": 12.80,
    "Pão": 3.00, "Leite": 4.50, "Ovos": 10.00, "Queijo": 15.90,
    "Manteiga": 8.20, "Açúcar": 3.70, "Café": 9.50, "Sal": 2.30,
    "Óleo": 7.00, "Alface": 2.50, "Tomate": 5.80
}

#9
def verificar_produto():
    produto_digitado = input("Informe o nome de um produto: ").strip().title()
    
    if produto_digitado in produtos_precos:
        print(f"O item '{produto_digitado}' faz parte da lista de supermercado.")
    else:
        print(f"O item '{produto_digitado}' NÃO faz parte da lista de supermercado.")
verificar_produto()

#10
cadastro_cliente = {
    "Nome": "Maria Silva",
    "Idade": 28,
    "sexo": "Feminino",
    "EstAdo Civil": "Solteira",
    "Nacionalidade": "Brasileira",
    "Faixa de Renda": "R$ 2.000 - R$ 3.000",
    "Endereço": "Cracolândia, 123, São Paulo - SP",
    "Telefone": "(11) 98765-4321",
    "Email": "maria.silva@email.com"
}

def exibir_cadastro(cadastro):
    print("Cadastro do Cliente:")
    for chave, valor in cadastro.items():
        print(f"{chave}: {valor}")

exibir_cadastro(cadastro_cliente)

#11














