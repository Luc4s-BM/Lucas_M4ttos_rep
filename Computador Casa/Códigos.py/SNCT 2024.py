eventos = []
inserir_eventos = input("Digite o nome do evento: ")
capacidade_de_pessoas = input("Digite a quantidade máxima de pessoas: ")
def cadastrar_eventos(evento_cadastro):
    evento_cadastro.append(eventos)
def excluir_evento_cadastrado():
def alunos_interessados_no_evento():
def excluir_alunos_cadastrados_e_atualizar():
def exibir_eventos_e_participantes():
    print()



escolha_do_menu = input("Digite sua opção: ").strip().lower()
def menu_de_opcoes(escolha):    
    if escolha == "1":
        cadastrar_eventos()
    elif escolha == "2":
        excluir_evento_cadastrado()
    elif escolha == "3":
        alunos_interessados_no_evento()
    elif escolha == "4":
        excluir_alunos_cadastrados_e_atualizar()
    elif escolha == "5":
        exibir_eventos_e_participantes()
    elif escolha == "6":
        print("OK, encerrando.")
        break
    else: 
        print(f"Não há opção {escolha} no menu.")
    print("""
    1 - Cadastrar evento.
    2 - Excluir evento cadastrado.
    3 - Cadastrar alunos no evento existentente.
    4 - Excluir alunos cadastrados no evento
    5 - Exibir lista de eventos e alunos cadastrados.
    6 - Digite "Sair" ou "6" para encerrar.
    """)
    
    menu_de_opcoes(escolha_do_menu)






















