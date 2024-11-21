#1

def calcular_tamanho_string(caracteres_da_string):
    if type(caracteres_da_string) == str:
        return len(caracteres_da_string)
    else:    
        return - 1 
    
letra_da_musica = ("Meu caminho é cada manhã Não procure saber onde vou Meu destino não é de ninguém Eu não deixo os meus passos no chão Se você não entende, não vê Se não me vê, não entende Não procure saber onde estou Se o meu jeito te surpreende Se o meu corpo virasse sol Minha mente virasse sol Mas só chove e chove Chove e chove Se um dia eu pudesse ver Meu passado inteiro E fizesse parar de chover Nos primeiros erros, oh O meu corpo viraria sol Minha mente viraria... Mas só chove e chove Chove e chove Se um dia e pudesse ver Meu passado inteiro E fizesse parar de chover Nos primeiros erros, oh O meu corpo viraria sol Minha mente viraria... Mas só chove e chove Chove e chove, oh O meu corpo viraria sol Minha mente viraria sol Mas só chove e chove Chove e chove, oh Chove e chove, oh Chove e chove, oh Chove e chove").strip()
tamanho_da_string_inserida = calcular_tamanho_string(letra_da_musica)

if tamanho_da_string_inserida <= 0: 
    print("Entrada inválida!")
else:
    print(f'A música "Primeiros Erros" tem {tamanho_da_string_inserida} caracteres.')

#2
StringFrase = str(input("Insira uma frase:  \n"))
PosicaoString = int(input("Informe a posição da letra que quer: \n"))
def  LocalizarCaracter(StringFrase, PosicaoString):
    try:
        print(f'A {PosicaoString}º letra da frase "{StringFrase}" é a letra "{StringFrase[PosicaoString - 1]}"')
    except IndexError():
        print("Indice fora do alcance!")
LocalizarCaracter(StringFrase, PosicaoString)

#3
def exibir_caracteres_e_posicoes(string):
    for indice, caracter in enumerate(string):
        print(f"{caracter} - {indice + 1}º caracter da String")
string_passada = input("Digite uma frase qualquer:\n")
exibir_caracteres_e_posicoes(string_passada)

#4 
FraseParaTerminar = str(input("Informe uma palavra ou frase para verificar se termina com alguma letra/palavra:\n "))
FraseOuPalavraParaVerificar = input("Insira uma palavra ou letra para ver se ela está presente no final da palavra:\n")
def FuncaoVerdadeiroFalso(FraseParaTerminar,FraseOuPalavraParaVerificar):
    if (FraseParaTerminar.endswith(FraseOuPalavraParaVerificar)):
        print(f"{FraseParaTerminar} Termina com {FraseOuPalavraParaVerificar}!")
    else:
        print(f'"{FraseParaTerminar}" não Termina com {FraseOuPalavraParaVerificar}!')
(FuncaoVerdadeiroFalso(FraseParaTerminar, FraseOuPalavraParaVerificar))

#5
def conceitoVariavel():
    print('''Em Python, uma variável é um nome que se refere a um valor específico. Pense nela como uma caixinha onde você pode guardar um número, um texto, uma lista ou qualquer outro tipo de dado. Você dá um nome a essa caixinha para que possa encontrar o valor armazenado mais tarde.
    Existem algumas regras e convenções que você deve seguir ao nomear suas variáveis em Python:
    Os nomes das variáveis devem começar com uma letra ou um underscore (_).
    Os nomes das variáveis podem conter letras, números e underscores.
    Os nomes das variáveis não podem conter espaços ou caracteres especiais, e não podem ser palavras reservadas do Python (como if, for, print, etc.).
    Python diferencia maiúsculas de minúsculas, portanto variavel e Variavel seriam consideradas variáveis diferentes.''')
def conceitoLacoInfinito():
    print('''O loop infinito é um conceito importante na programação, e em Python não é diferente. Em termos simples, um loop infinito é um trecho de código que se repete continuamente, sem uma condição de parada definida. Isso significa que o código dentro do loop será executado repetidamente, até que uma condição específica seja atendida para interromper a execução. Em Python, podemos criar um loop infinito usando a estrutura de controle “while True”.''')
def conceitoSemantica():
    print('''O Que é Semântica? Aqui, a semântica é clara: o código soma x e y e imprime o resultado, que será 15 . Se você trocasse o + por - , o resultado seria -5 . A semântica ajuda você a entender o que cada linha do código está realmente fazendo. É a parte abstrata do código.''')
def conceitoSintaxe():
    print('''A sintaxe é a parte "concreta" do código, as palavras e comandos utilizados. Ela checa se eles estão escritos da forma correta perante as regras de cada um e se funcionam dentro de seu contexto.''')
def inputDoUsuario():
    while True:
        opcaoUsuario = input("Insira a opção que deseja escolher: ").strip().lower()
        if (opcaoUsuario == ""):
            print("Insira algo.")
        elif (opcaoUsuario == "sair"):
            break
        elif (opcaoUsuario == "1"):
            conceitoVariavel()
            break
        elif (opcaoUsuario == "2"):
            conceitoLacoInfinito()
            break
        elif (opcaoUsuario == "3"):
            conceitoSemantica()
            break
        elif (opcaoUsuario == "4"):
            conceitoSintaxe()
            break
        elif (opcaoUsuario.isdigit == True):
            print("Insira um número disponível no menu.")
        else:
            print("Para sair do programa, digite 'sair'.")
print('''Para cada, opção, digite seu número correspondente:
      1 - Conceito de variáveis
      2 - Conceito de loops infinitos 
      3 - Conceito de semântica
      4 - Conceito de sintaxe''')
inputDoUsuario()


#6
('''- Uma letra maiúscula;
- Uma letra minúscula;
- Um caracter especial ($#!@&)
- Mínimo de 6 caracteres;
- Máximo de 20 caracteres.''')
def criarSenha():
    while True:
        senhaOriginal = input("Insira a senha:\n").strip()
        if (len(senhaOriginal) < 6):
            print("A senha deve ter mais de 6 caracteres.")
        elif (len(senhaOriginal) > 20):
            print("A senha deve ter menos de 20 caracteres.")
        elif (not any(i.isupper() for i in senhaOriginal)):
            print("A senha deve conter pelo menos uma letra maiúscula.")
        elif (not any(i.islower() for i in senhaOriginal)):
            print("A senha deve conter pelo menos uma letra minúscula.")
        elif (not any(i in "$#!@&" for i in senhaOriginal)):
            print("A senha deve conter pelo menos um caracter especial ($#!@&).")
        else:
            print("Senha criada com sucesso! (espaços retirados!)")
            return senhaOriginal
def verificarSenha(senhaOriginal):
    while True:
        tentativaConfirmacao = input("Confirme a senha criada:\n")
        if (tentativaConfirmacao != senhaOriginal):
            print("A senha inserida não está correta. Tente novamente.")
        else:
            print("Senha confirmada com sucesso!")
            break
senha = criarSenha()
verificarSenha(senha)

#7
def string_para_palavras_minusculas(StringMaiuscula):
    StringMaiuscula = StringMaiuscula.lower()
    return StringMaiuscula.title()
palavraStringParaDeixarmaiuscula = str(input("Insira o seu nome completo em letras minusculas: \n"))
ResultadoJamaiusculo = string_para_palavras_minusculas(palavraStringParaDeixarmaiuscula)
print(f"{palavraStringParaDeixarmaiuscula.title()}")


#8
TextoString = str(input("Insira uma palavra ou texto:   \n"))
CaracterSelecionado = input("Insira um caracter para ser colocado entre as letras:  \n")
def inserir_caractere_na_string(TextoString, CaracterSelecionado):
    return CaracterSelecionado.join(TextoString)
resultado = inserir_caractere_na_string(f"{TextoString}", f"{CaracterSelecionado}")
print(resultado)









































