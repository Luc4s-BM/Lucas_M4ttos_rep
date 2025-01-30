SOMAR               = "SOMAR"
SUBTRAIR            = "SUBTRAIR"

menu = """\nMenu de Opções:
            1- Cadastrar evento
            2- Cadastrar aluno
            3- Inscrever aluno
            4- Listar eventos cadastrados
            5- Listar alunos cadastrados
            6- Resumo participação
            7 - Sair\n"""""

def validar_dadosint(entrada):
    while True:
        try:
            return int(entrada)
        except ValueError:
            entrada = input("Digite um valor válido: ")

#Dicionários
evento    = {} #keys: titulo, capacidade, vagas_restantes
aluno     = {} #keys: nome, curso, instituição
inscricao = {} #keys: evento_nome, aluno_nome

#Listas de dicionários
eventos_cadastrados    = [] #manipula evento
alunos_cadastrados     = [] #manipula aluno
inscricoes_cadastradas = [] #manipula inscrição de alunos em eventos já cadastrados


def exibir_menu():
    print(menu)

def exibir_eventos_cadastrados():
    for evento in eventos_cadastrados:
        print(evento)

def exibir_alunos_cadastrados():
    for aluno in alunos_cadastrados:
        print(aluno)

def exibir_inscricoes_efetuadas():
    for inscricao in inscricoes_cadastradas:
        print(inscricao)        

#Fazer validação dos dados e tratamento de erro
def cadastrar_evento():
    titulo          = input('\nDIGITE O NOME DO EVENTO: ').title().strip()
    capacidade      = validar_dadosint(input('DIGITE A CAPACIDADE MÁXIMA DO EVENTO: ').strip())

    #Cria um evento novo que é armazenado em uma variável do tipo "dicionário"
    evento = {'titulo_evento': titulo,
                 'capacidade': capacidade,
            'vagas_restantes': capacidade
    }      

    #Armazena, na lista de dicionários, o evento novo criado
    eventos_cadastrados.append(evento)
    
#Fazer validação dos dados e tratamento de erro
def cadastrar_aluno():
    nome        = input('\nDIGITE O NOME DO ALUNO: ').strip()
    curso       = input('DIGITE O CURSO DO ALUNO: ').strip()
    instituicao = input('DIGITE A INSTITUIÇÃO EM QUE O ALUNO ESTUDA: ').strip()

    #Cria um aluno novo que é armazenado em uma variável do tipo "dicionário"
    aluno = {'nome_aluno': nome,
                 'curso' : curso,
            'instituicao': instituicao
            }      

    #Armazena, na lista de dicionários, o aluno novo criado
    alunos_cadastrados.append(aluno)    
    
#Fazer validação dos dados e tratamento de erro
def inscrever_aluno_curso():
    nomeEvento  = input('\nDIGITE O NOME DO EVENTO EM QUE O ALUNO QUER SE INSCREVER: ').strip()
    nomeAluno   = input('DIGITE O NOME DO ALUNO: ').strip()

    #Cria uma inscrição nova que é armazenada em uma variável do tipo "dicionário"
    inscricao = {'evento_nome': nomeEvento,
                 'aluno_nome' : nomeAluno
                }
    
    #Armazena, na lista de dicionários, a inscrição nova criada
    #PRECISA validar se o aluno informado já não está inscrito nesse curso
    #PRECISA validar se o curso existe e se o aluno existe
    inscricoes_cadastradas.append(inscricao)
    
    #Atualizar o número de vagas restantes no curso em que o aluno foi inscrito
    atualizar_vagas(nomeEvento, SUBTRAIR)


#Fazer validação dos dados e tratamento de erro
def atualizar_vagas(nomeEvento, tipoAtualizacao):
    msg = ''

    if len(eventos_cadastrados) > 0:
        for indice in range(len(eventos_cadastrados)):
            if eventos_cadastrados[indice].get('titulo_evento').upper() == nomeEvento.upper():
                if tipoAtualizacao == SOMAR:
                    atualizar = int(eventos_cadastrados[indice].get('vagas_restantes')) + 1
                else:
                    atualizar = int(eventos_cadastrados[indice].get('vagas_restantes')) - 1
                
                #validar o numero máximo de vagas definida na criação do evento novo
                if atualizar >= 0:
                    eventos_cadastrados[indice].update({'vagas_restantes': atualizar})
                    msg = 'O evento ' + eventos_cadastrados[indice].get('titulo_evento') + ' foi atualizado com sucesso!'
                else:
                    msg = 'Não há mais vagas disponíveis neste curso'
    else:
        msg = 'Não existem eventos cadastrados.'

    return msg

def executar_menu():
    while True:
        exibir_menu()
        
        #Fazer validação dos dados e tratamento de erro
        opcaoDigitada = validar_dadosint(input("DIGITE UMA OPÇÃO VÁLIDA DO MENU: ")) 
    
        if opcaoDigitada == "1":
            cadastrar_evento()
        
        elif opcaoDigitada == "2":
            cadastrar_aluno()
        
        elif opcaoDigitada == "3":
            inscrever_aluno_curso()
        
        elif opcaoDigitada == "4":
            exibir_eventos_cadastrados()
        
        elif opcaoDigitada == "5":
            exibir_alunos_cadastrados()
        
        elif opcaoDigitada == "6":
            exibir_inscricoes_efetuadas()
        
        elif opcaoDigitada == "7":
            break
                
        else:
            print(f"{opcaoDigitada} - OPÇÃO INVÁLIDA DE MENU.")


executar_menu()
