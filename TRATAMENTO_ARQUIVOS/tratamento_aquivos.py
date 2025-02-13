import os

#arquivo evento.txt     - armazenar informações sobre o evento.
#arquivo aluno.txt      - armazenar informações sobre o alunos.
#arquivo inscrições.txt - armazenar informações sobre as inscrições.
SOMAR               = "SOMAR"
SUBTRAIR            = "SUBTRAIR"
ARQUIVO_EVENTO      = "evento.txt"
ARQUIVO_ALUNO       = "alunos.txt"
ARQUIVO_INSCRICOES  = "inscrições.txt"


menu = """\nMenu de Opções:
            1- Cadastrar evento
            2- Cadastrar aluno
            3- Inscrever aluno
            4- Listar eventos cadastrados
            5- Listar alunos cadastrados
            6- Resumo participação
            7- Excluir eventos
            8- Sair\n"""""

#Dicionários
evento    = {} #keys: titulo, capacidade, vagas_restantes.
aluno     = {} #keys: nome, curso, instituição.
inscricao = {} #keys: evento_nome, aluno_nome.

#Listas de dicionários
eventos_cadastrados    = [] #manipula evento.
alunos_cadastrados     = [] #manipula aluno.
inscricoes_cadastradas = [] #manipula inscrição de alunos em eventos já cadastrados.


def arquivoExiste(nomeArquivo):
    try:
        #O parâmeto "nomeArquivo" deverá conter o caminho "absoluto ou relativo" do arquivo, seu nome e sua exetnção.
        if(os.path.exists(nomeArquivo)):
            return True
        else:
            return False
        
    except Exception as erroArquivo:
        print (f"Erro: {erroArquivo}")
        return False

def cadastrar_evento_arquivo():
    titulo     = input('\nDIGITE O NOME DO EVETO: ').title().strip()
    capacidade = input('\nDIGITE A CAPACIDADE MÁXIMA DO EVENTO: ').strip()
    
    try:
        #Paga o diretório atual e conecta o nome do arquivo a ser criado/aberto
        #se houver espações em branco no caminho absoluto, este deve ser passado
        #como string (entre aspas)
        diretorioAtual = "" + os.getcwd() + "/" + ARQUIVO_EVENTO + ""
        
        if arquivoExiste(diretorioAtual):
            #se o arquivo EXISTE, abre no modo APPEND, ou seja, um arquivo em branco, se conteúdo
            #ao final do arquivo.
            fEvento = open(ARQUIVO_EVENTO, "a")
        else:
            #o arquivo NÃO EXISTE, e será aberto no modo WRITE, ou seja, um arquivo
            #em branco sem conteúdo.
            fEvento = open(ARQUIVO_EVENTO, "w")
            #Escreve na primeira linha o nome das colunas que identifica as informações
            nomeColunas = "Nome do evento, Capacidade, Vagas restantes\n"
            fEvento.write(nomeColunas)
            
        #o conteúdo do arquivo será gravado como uma string
        linha = [titulo
        , ","
        , capacidade
        , ","
        , capacidade #parametro que representa as vagas restantes
        , "\n"]
            
        #Grava as informações no arquivo 
        informacoes = "".join(linha)
        #fEvento.write((f'{informações}'))
        fEvento.write((f'{informacoes}'))
        
        #OBRIGARIAMENTE , depois de finalizados as operações de gravação, o
        #arquivo de ser FECHADO
        fEvento.close()

    except Exception as erroArquivo:
        print(f'Erro: {erroArquivo}')

def exibir_eventos_cadastrados():
    if not eventos_cadastrados:
        if arquivoExiste(ARQUIVO_EVENTO):
            with open(ARQUIVO_EVENTO, "r") as f_evento:
                print("\nEventos Cadastrados:")
                for linha in f_evento:
                    print(linha.strip())
        else:
            print("Nenhum evento cadastrado.")
    else:
        print("\nEventos Cadastrados:")
        for evento in eventos_cadastrados:
            print(f'''Nome: {evento['titulo_evento']}, Capacidade: {evento['capacidade']}, 
                Vagas Restantes: {evento['vagas_restantes']}''')
        
def excluir_evento_arquivo(nome_do_evento):
    if not arquivoExiste(ARQUIVO_EVENTO):
        print("Não há eventos para serem excluídos.")
        return

    registro_arquivo = []
    evento_encontrado = False

    with open(ARQUIVO_EVENTO, "r") as arquivo_de_eventos:
        registro_arquivo = arquivo_de_eventos.readlines()

    with open(ARQUIVO_EVENTO, "w") as arquivo_de_eventos_alterado:
        for linha in registro_arquivo:
            if nome_do_evento.lower() in linha.lower():
                evento_encontrado = True
                print(f"Evento '{nome_do_evento}' excluído com sucesso.")
                continue  # Pula a linha do evento que será excluído
            arquivo_de_eventos_alterado.write(linha)

    if not evento_encontrado:
        print(f"Evento '{nome_do_evento}' não encontrado.")
        
        
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
    capacidade      = input('DIGITE A CAPACIDADE MÁXIMA DO EVENTO: ').strip()

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
        opcaoDigitada = input("DIGITE UMA OPÇÃO VÁLIDA DO MENU: ")
    
        if opcaoDigitada == "1":
            cadastrar_evento_arquivo()
        
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
            exibir_eventos_cadastrados()
            nomeDoEvento = input("Digite o nome do evento: ")
            excluir_evento_arquivo(nomeDoEvento)
        
        elif opcaoDigitada == "8":
            break
                
        else:
            print(f"{opcaoDigitada} - OPÇÃO INVÁLIDA DE MENU.")


executar_menu()
