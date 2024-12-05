def decisao_fazer_lista_de_compras():
    while True:
        fazer_lista = input("Gostaria de fazer uma lista de compras? (SIM / NÃO): ").strip().lower()
        
        if fazer_lista == "sim":
            print("OK, comece a sua lista!\n")
            lista = lista_de_compras()
            itens_pegos(lista)
            break
        elif fazer_lista in ["não", "nao"]:
            print("OK, talvez outra hora...")
            break
        else:
            print("Digite uma resposta válida! (SIM ou NÃO)")
            
def lista_de_compras():
    lista = []
    numero_do_item = 1
    while True:
        item = input(f'-> Digite o {numero_do_item}º item da sua lista de compras (ou "PRONTO" para encerrar): ').strip().upper()
        if item == "PRONTO":
            print("\n===================================================================================")
            break
        lista.append(item)
        numero_do_item += 1
    
    print("\nSua lista de compras:\n")
    for i, item in enumerate(lista, start=1):
        print(f"{i} - {item.capitalize()}")
    print("\n===================================================================================\n")
    return lista

def itens_pegos(lista):
    itens_coletados = []
    while len(itens_coletados) < len(lista): 
        listar_itens = input('Digite o item que você já coletou (ou "PRONTO" para encerrar): ').strip().upper()
        if listar_itens == "PRONTO":
            print("Você decidiu sair antes de coletar todos os itens.")
            break
        if listar_itens in lista and listar_itens not in itens_coletados:
            itens_coletados.append(listar_itens)
            print(f"Item '{listar_itens.capitalize()}' marcado como coletado!")
        elif listar_itens in itens_coletados:
            print(f"Você já marcou o item '{listar_itens.capitalize()}' como coletado.")
        else:
            print(f"O item '{listar_itens.capitalize()}' não está na lista de compras.")

        if len(itens_coletados) == len(lista):
            print("\nTodos os itens foram coletados! Sua lista de compras está completa.")
            break

            
    for item in itens_coletados:
        print(f"- {item.capitalize()}")

decisao_fazer_lista_de_compras()
