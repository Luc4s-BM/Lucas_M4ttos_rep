"""1) Escreva um programa que peça ao usuário que informe dois valores
numéricos de entrada, em seguida, exiba em tela o resultado da soma,
subtração, multiplicação e divisão desses números. NÃO UTILIZAR
FUNÇÃO P/ RESOLVER ESSA QUESTÃO. Se desejarem poderão
utilizar o conceito de FString, concatenação de String, qualquer uma das
sobrecargas de função responsável por imprimir no stdout."""
def dois_valores_numericos():
    def testar_caractere():
        while True:
            try:
                num1 = int(input("Digite o primeiro valor: "))
                num2 = int(input("Digite o segundo valor: "))
                return num1, num2
            except ValueError:
                print("Erro: Digite apenas números.")
    num1, num2 = testar_caractere()
    soma = num1 + num2
    subtracao = num1 - num2
    multiplicacao = num1 * num2
    divisao = "Indefinido" if num2 == 0 else num1 / num2
    print(f"A soma: {soma}\nA subtração: {subtracao}\nA multiplicação: {multiplicacao}\nA divisão: {divisao}")


#===========================================================================================

"""2) Escreva um programa que calcule o “índice de massa corporal” (IMC).
IMC = peso em quilos / altura
2
. Exiba o resultado na tela. Utilizar valores
em ponto flutuante, precisão simples."""
def questao_imc():
    def calcular_imc(a, b):
        imc = a / (b * b)
        return imc

    print("Vamos calcular seu IMC: ")
    peso = float(input("Digite seu peso (Obs: Escreva em quilos):"))
    altura = float(input("Digite sua altura (Obs: Digite em metros):"))
    imc = calcular_imc(peso ,altura)
    print(f"O resultado do seu IMC: {imc:.2f}")
    if imc > 40:
        print("Você está muito obeso!")
    elif imc < 18.5:
        print("Você está muito magro!")
    elif imc > 18.5 and imc < 24.9:
        print("Você está no peso normal!")
    elif imc > 25 and imc < 29.9:
        print("Você está com excesso de peso!")
    elif imc > 30 and imc < 34.9:
        print("Você está com obesidade classe I!")
    elif imc > 35 and imc < 39.9 :
        print("Você está com obesidade classe II!")
    elif imc > 40:
        print("Você está com obesidade classe III!")
    calcular_imc(peso ,altura)

#===========================================================================================


"""3) Escreva um programa que exiba no terminal a mensagem: “Bem vindo
turma da Programação II ao mundo da programação Python!!!” de trás p/
a frente. Ou seja, o resultado esperado, deverá ser: !!!nohtyP
oãçamargorp ad odnum oa II oãçamargorP ad amrut odniv meB. NÃO
UTILIZAR FUNÇÃO P/ RESOLVER ESSA QUESTÃO. A função
responsável por imprimir no stdout é uma das formas de resolver a
questão."""

def frase_invertida():
    def inverter_frase(invertido):
        print(invertido[::-1])
        frase = "“Bem vindoturma da Programação II ao mundo da programação Python!!!”"
        inverter_frase(frase)

#===========================================================================================

"""4) Crie um programa que gere uma senha aleatória, com um tamanho
definido pelo usuário. O tamanho da senha deverá ser representado por
um número inteiro, positivo, maior do que ZERO. A SENHA GERADA
NÃO PODERÁ TER MAIS DO QUE 128 CARACTERES. Ou seja, se o
usuário digitar o valor 8, uma senha de 8 caracteres de verá ser gerada.
Funções da Biblioteca Padrão do Python: https://docs.python.org/ptbr/3/library/ 
poderão ser utilizadas. Utilize como base da senha, 
um valorUUID (universally unique identifier) 
identificador universalmente exclusivo.Procurar na Internet 
por gerador online UUID p/ obter valores UUID."""

def senha_uuid():
    import random
    tamanho_da_senha_a_ser_gerada = int(input("Digite o tamanho da senha (Max: 128): "))
    uuid_gerador_senha = '35b35f68-9687-4ca6-bb79-f59201d40b0739e5b006-f4ab-49cb-a072-6549876b35dc'
    senha_gerada = "  ".join(random.sample(uuid_gerador_senha, tamanho_da_senha_a_ser_gerada))
    print(f"Senha gerada com {tamanho_da_senha_a_ser_gerada} caracteres: {senha_gerada}")


#===========================================================================================

"""5)  Crie  um  programa  que  mostra  a  data  atual,  no  formato:  dia/mês/ano 
hora:minuto:segundo.  Funções  da  Biblioteca  Padrão  do  Python: 
https://docs.python.org/pt-br/3/library/ poderão ser utilizadas. """

import datetime

def relogio():
    agora = datetime.datetime.now()
    print(agora.strftime("%d/%m/%Y - %H:%M:%S"))


#===========================================================================================

"""6)  Crie  2  variáveis  com  dois  valores  numéricos  inteiros  informados  pelo 
usuário, caso o valor do primeiro número for maior do que o segundo, 
exiba em tela uma mensagem de acordo, caso contrário, exiba em tela 
uma  mensagem  dizendo  que  o  primeiro  valor  digitado  é  menor  que  o 
segundo.  Os  números  informados  pelo  usuário  devem  aparecer  em 
ambas as mensagens. """

def numero_maior_que_o_outro():
    num1 = int(input("Digite um número: "))
    num2 = int(input("Digite outro número: "))

    if num1 > num2:
        print(f"O primeiro número: {num1}, é maior que o segundo número: {num2}!")
    elif num2 > num1:
        print(f"O segundo número: {num2} é maior que o primeiro número: {num1}!")   
    else:
        print("Os dois números são iguais!")

#===========================================================================================

"""7)  Crie um programa que possa marcar uma consulta médica. Como opções, 
teremos  disponíveis  apenas  03  médicos,  que  devem  ter  seus  nomes 
exibidos  na  tela,  p/  que  possam  ser  escolhidos.  Após  a  escolha  do 
profissional médico, exibir mensagem na tela informando que a consulta 
foi marcada com o médico escolhido (nome do médico).  """

def escolha_de_medicos():
    while True:

        medico = int(input("Qual médico você deseja?\nDigite 1 para escolher o médico LUCAS.\nDigite 2 para escolher o médico TAYNAN.\nDigite 3 para escolher o médico VICTOR.\nQual a sua escolha?: "))

        if medico == 1:
            print("Você escolheu o médico LUCAS!")
            break
        elif medico == 2:
            print("Você escolheu o médico TAYNAN!")
            break
        elif medico == 3:
            print("Você escolheu o médico VICTOR!")
            break
        else:
            print (f"Não existe a opção: {medico}\nDigite outra opção!")

#===========================================================================================

"""8)  Escreva um programa que verifica se uma determinada palavra consta 
em  um  texto  de  origem.  O  texto  não  será  conhecido  pelo  usuário  que 
usará  de  palavras  aleatórias  na  tentativa  de  adivinhar  que  palavras 
compõem a frase oculta. Frase: "Python é uma excelente linguagem de 
programação!!!  Se  acertar,  a  mensagem:  "A  palavra  (palavra  digitada 
pelo usuário) está na frase". Se errar, a mensagem: "A palavra (palavra 
digitada pelo usuário) não está na frase". Use a função "find", referenciada 
na documentação: 
https://docs.python.org/3/library/stdtypes.html"""

def python_e_uma_otima_linguagem():
    frase = "python é uma excelente linguagem de programação!!!"
    
    palavra = input("Qual palavra deseja saber se está na frase?: ").lower()
    
    tem_na_frase = frase.find(palavra)
    
    if  tem_na_frase == -1:
        print(f"A palavra ({palavra}) não está na frase.")
    
    else:
        print(f"A palavra ({palavra}) está na frase.")

#===========================================================================================

"""9) Crie um programa que leia um número e verifique se ele é par ou ímpar."""

def numero_par_ou_impar():
    numero = int(input("Digite qualquer número: "))
    if numero % 2 == 0: 
        print('Esse número é par!') 
    else:
        print('Ele é ímpar!')

#===========================================================================================

"""10) Escreva um programa que receba dois números e verifique se ambos são 
positivos."""

def numeros_positivos():
    numero1 = int(input("Digite qualquer número: "))
    numero2 = int(input("Digite qualquer número: "))
    if numero1 >= 0 and numero2 >= 0:
        print("Ambos são positivos!")
    elif numero1 < 0 and numero2 < 0:
        print("Ambos são negativos!")
    elif numero1 < 0 or numero2 < 0: 
        print("Um dos números é negativo!")

#===========================================================================================

"""11) Crie um programa que leia dois números e exiba o maior entre eles. Caso 
sejam iguais, exiba uma mensagem informando isso."""

def numero_maior_que_o_outro():
    number1 = int(input("Digite o primeiro número: "))
    number2 = int(input("Digite o segundo número: "))
    if number1 > number2: 
        print(f"O primeiro número: {number1}, é maior que o segundo número: {number2}")
    elif number2 > number1:
        print(f"O segundo número: {number2}, é maior que o primeiro número: {number1}")
    elif number1 == number2:
        print("Os valores são iguais!")

#===========================================================================================

"""12) Crie um programa que receba o peso e a altura de uma pessoa e calcule 
seu Índice de Massa Corporal (IMC). imc = peso / (altura * altura) . O 
programa deve exibir uma mensagem na tela de acordo com a seguinte 
tabela:
     Abaixo de 18.5: Abaixo do peso
     Entre 18.5 e 24.9: Peso normal
     Entre 25 e 29.9: Sobrepeso
     Acima de 30: Obesidade sdg"""

def calcular_imc():
    print("Vamos calcular seu IMC: ")
    peso = float(input("Digite seu peso (Obs: Escreva em quilos):"))
    altura = float(input("Digite sua altura (Obs: Digite em metros):"))
    imc = peso / (altura * altura)
    print(f"O resultado do seu IMC: {imc:.2f}")

    if imc < 18.5:
        print("Abaixo do peso!")

    elif imc > 18.5 and imc < 24.9:
        print("Peso normal!")

    elif imc > 25 and imc < 29.9:
        print("Sobrepeso!")

    elif imc > 30:
        print("Obesidade!")

#===========================================================================================

"""13) Crie e inicialize uma variável do tipo inteiro. Enquanto o valor dessa variável for 
menor ou igual a um valor definido por você, exiba uma mensagem na tela e o 
valor dessa variável. Explique em um comentário como o controle do laço vai 
funcionar."""

import time
# "import time" Apenas para deixar um intervalo entre os valores
def explicacao_while():    
    limite = 10
    valor = 0
    while valor <= limite:
        print(f"Valor da variável: {valor}")
        time.sleep(1)
        # "time.sleep()" Da um certo tempo antes de executar outra linha de código
        valor += 1

"""O "while" foi configurado para repetir o código enquanto o "valor"
for menor que o  "limite", quando o "valor" for igual ao "limite" o
código se encerra, pois, se passar do limite, a condição do "while"
não é mais verdadeira."""

#===========================================================================================

"""14) Escreva um programa que gera um número aleatório entre 0 a 10, salvando 
esse número em uma variável. Solicite ao usuário que tente adivinhar o 
número que foi gerado aleatoriamente através da digitação via stdin. Caso o 
usuário acerte o número, exiba uma mensagem parabenizando-o e mostrando 
na mensagem o número adivinhado. Utilize a instrução “import” para que a 
biblioteca Random possa ser utilizada. O número aleatório deverá ser 
gerado através da função randint. Restrinja ao máximo de 5 tentativas por 
parte do usuário, caso não acerte, exiba mensagem e termine o programa."""

import random

def numero_aleatorio_de_um_a_10():
    numero_aleatorio = random.randint(0, 10)
    print("Um número aleatório de 0 a 10 foi gerado!")

    chute = 0
    chances = 5

    while chute != numero_aleatorio:
        chute = input("Tente adivinhar o número gerado: ")
        if chute.isnumeric():
            chute = int(chute)
            chances = chances - 1
        else: 
            print("Digite um número válido!!!")
        if chute != numero_aleatorio:
            print("Número incorreto!")

        if chute == numero_aleatorio:
            print(f"Parabéns você acertou era o número {numero_aleatorio}!!!")
            break
        if chances == 0:
            print(f"Que pena suas chances acabaram! O número correto era: {numero_aleatorio}")
            break
    print("### FIM DE JOGO ###")           
 
#===========================================================================================

"""15)  Escreva um programa que verifica se um endereço URL de um site foi digitado 
levando-se em conta o prefixo “www.” e o sufixo “.com.br”. Se o endereço foi 
digitado nesse formato corretamente, exiba mensagem, inclusive mostrando o 
endereço digitado, e finalize o programa. Se não digitou corretamente, exiba 
uma mensagem informando que a URL é inválida, mostre o endereço no 
formato errado e solicite ao usuário que digite novamente a URL do site. Uma 
forma de resolver esse problema é utilizar métodos da classe String do Python, 
como por exemplo: startswith() e endswith(). A documentação desses métodos 
pode ser encontrada em: https://docs.python.org/pt-
br/3/library/stdtypes.html.dgs 
Enquanto a URL informada não estiver correta, o programa não deve ser 
finalizado."""

def url():
    while True:
        url = input("Digite seu URL corretamente: ")
        resultado = url.startswith('www.')
        resultado = url.endswith('.com.br')
        if resultado == False:
            print(f"O endereço: {url} é inválido!")
            print("Tente novamente!")
        else:
            print(f"O endereço: {url} é válido!")
            break

#===========================================================================================

"""16) Código exemplo validação da entrada via stdin"""

def via_stdin():
    primeiroValorInformadoPeloUsuario = input("Digite o primeiro número: ")
    segundoValorInformadoPeloUsuario  = input("Digite o segundo número: ")
    if not (primeiroValorInformadoPeloUsuario.strip().isnumeric()):
        print(f"O primeiro valor informado: \"{primeiroValorInformadoPeloUsuario}\" não é um valor numérico válido.")
    elif (not (segundoValorInformadoPeloUsuario.strip().isnumeric())):
        print(f"O segundo valor informado: \"{segundoValorInformadoPeloUsuario}\" não é um valor numérico válido.")
    else:
        opcaoDigitadaPeloUsuario = input("Informe um valor numérico de 1 a 10: ")

        #Validação do tipo de entrada informada pelo Stdin (teclado)
        if not (opcaoDigitadaPeloUsuario.strip().isnumeric()):
            print(f"A opção informada: \"{opcaoDigitadaPeloUsuario}\" é inválida. As opções numéricas válidas são: 1, 2, 3 ou 4.")

        elif (int(opcaoDigitadaPeloUsuario) <= 0 or int(opcaoDigitadaPeloUsuario) > 10):
            print(f"A opção informada: \"{opcaoDigitadaPeloUsuario}\" é inválida. As opções numéricas válidas são: 1, 2, 3 ou 4.")
        else:
            print("Todos os valores numéricos informados via stdin foram válidos.")    
        
#===========================================================================================

"""17) Crie uma estrutura de repetição que percorra a String “Instituto Federal 
de Santa Catarina” exibindo na tela letra por letra dessa String, tanto na 
orientação horizontal quanto na vertical."""

def string_vertical():
    class range:
        frase_fornecida =  "Instituto Federal de Santa Catarina"
        print("Vertical: \n")
        for cada_letra_da_frase in frase_fornecida:
            print(" ", cada_letra_da_frase)
        print(" ")
        print("Horizontal:")
        for item_da_lista in "Instituto Federal de Santa Catarina":
            palavra_na_horizontal = ""
        for item_da_lista in "Instituto Federal de Santa Catarina":
            palavra_na_horizontal = palavra_na_horizontal + item_da_lista
        print("\n" + palavra_na_horizontal)
        print("")

#===========================================================================================

"""18) Crie um programa que realiza a contagem de 0 a 20, exibindo apenas os 
números pares."""
def numeros_0_20():    
    print("Números pares de 0 a 20:")
    for numeros_de_0_a_20 in range(0,21, 2):
        print("->", numeros_de_0_a_20)
  
#===========================================================================================

"""19) Crie um programa que exiba na tela a tabuada de um determinado número 
fornecido pelo usuário."""

def tabuada():
    tabuada_escolhida_pelo_usuario = int(input("Qual tabuada você gostaria de ver?: ")) 

    for numero_da_tabuada in range (0,11):
        print(f"{numero_da_tabuada} x {tabuada_escolhida_pelo_usuario} = {numero_da_tabuada * tabuada_escolhida_pelo_usuario}")
    
#===========================================================================================

"""20) Crie um programa que realiza a contagem regressiva de 20 segundos."""

def contagem_regressiva_20():
    import time
    numeros_regressivos_20 = 0
    print("Contagem regressiva de 20 segundos: ")
    for numeros_regressivos_20 in range(1, 21):
        print(" ", numeros_regressivos_20)
        time.sleep(1)

#===========================================================================================

"""21) Crie um programa que realiza a contagem de 1 até 100, considerando 
apenas os números ímpares. Exiba na tela quantos números ímpares 
foram encontrados nesse intervalo e qual a soma desses números
ímpares."""

def somaImpar1a100():
    soma= 0
    quantidadeDeImpares = 0
    for i in range(1,101,2):
        print(i, end=", ")
        soma = soma + i
        quantidadeDeImpares = quantidadeDeImpares + 1
    print(f"A soma dos números ímpares resulta em: {soma} e foram encontrados {quantidadeDeImpares} números ímapares.")


#===========================================================================================

"""22) Crie um programa que pede ao usuário que digite um número qualquer, 
em seguida retorne se esse número é primo ou não, caso não, retorne 
também quantas vezes esse número é divisível."""

def isprimo():
    quantidadeDeDivisores = 0
    numeroDoUsuario = int(input("Digite um número: "))
    for i in range(1, numeroDoUsuario+1):
        if numeroDoUsuario%i==0:
            quantidadeDeDivisores += 1
    if quantidadeDeDivisores > 2:
        print(f"O número escolhido não é primo e possui {quantidadeDeDivisores} divisores")
    else:
        print(f"O número escolhido é primo, possuindo {quantidadeDeDivisores} divisores")



#===========================================================================================

"""23) Crie um programa que pede que o usuário digite um nome ou uma frase, 
verifique se esse conteúdo digitado é um palíndromo ou não, exibindo em 
tela esse resultado."""

def palindromo():
    frase_palindromo = str(input("Digite alguma frase: "))
    if frase_palindromo == frase_palindromo[::-1]: 
        print(f"{frase_palindromo}É um palíndromo!") 
    else: print(f"{frase_palindromo}Não é um palíndromo!")

#===========================================================================================

"""24) Crie uma função de número de parâmetros indefinido, que realize a soma 
dos números passados como parâmetro, independentemente da 
quantidade de parâmetros."""

def soma_com_numero_variavel_de_parametros(*args):
    soma_numeros = 0
    for numero in args:
        soma_numeros += numero
        
    print(f"Soma dos valores {args} é {soma_numeros}")


#===========================================================================================

"""25) Escreva um programa que lê uma palavra ou frase digitada pelo usuário, 
retornando o número de letras maiúsculas e minúsculas da mesma. Usar 
apenas de logica e de funções embutidas ao sistema."""

def quantasMaiusculasEMinusculas():
    texto = input('Digite um texto: ')

    maiusculas = 0
    minusculas = 0

    for letra in texto:
        if (letra.islower()):
            minusculas += 1
        elif (letra.isupper()):
            maiusculas += 1

    print(f'No texto {texto} foram encontradas {maiusculas} letras maiusculas')
    print(f'No texto {texto} foram encontradas {minusculas} letras minusculas')


#===========================================================================================

def funcaoPrincipal(escolha):
    if escolha == '1':
        dois_valores_numericos()
    elif escolha == '2':
        questao_imc()
    elif escolha == '3':
        frase_invertida()
    elif escolha == '4':
        senha_uuid()
    elif escolha == '5':
        relogio()
    elif escolha == '6':
        numero_maior_que_o_outro()
    elif escolha == '7':
        escolha_de_medicos()
    elif escolha == '8':
        python_e_uma_otima_linguagem()
    elif escolha == '9':
        numero_par_ou_impar()
    elif escolha == '10':
        numeros_positivos()
    elif escolha == '11':
        numero_maior_que_o_outro()
    elif escolha == '12':
        calcular_imc()
    elif escolha == '13':
        explicacao_while()
    elif escolha == '14':
        numero_aleatorio_de_um_a_10()
    elif escolha == '15':
        url()
    elif escolha == '16':
        via_stdin()
    elif escolha == '17':
        string_vertical()
    elif escolha == '18':
        numeros_0_20()
    elif escolha == '19':
        tabuada()
    elif escolha == '20':
        contagem_regressiva_20()
    elif escolha == '21':
        somaImpar1a100()
    elif escolha == '22':
        isprimo()
    elif escolha == '23':
        palindromo()
    elif escolha == '24':
        soma_com_numero_variavel_de_parametros()
    elif escolha == '25':
        quantasMaiusculasEMinusculas()
    elif escolha.lower() == "sair":
        print("Você escolheu SAIR.")
        return False 
    else:
        print("Digite uma opção válida!")
    return True  
while True:
    opcao = input("""
        1 = Calcular Operações Básicas (Soma, Subtração, Multiplicação e Divisão).
        2 = Calcular Índice de Massa Corporal (IMC).
        3 = Inverter Frase.
        4 = Gerar Senha Aleatória.
        5 = Mostrar Hora Atual.
        6 = Comparar Dois Números.
        7 = Marcar Consulta Médica.
        8 = Verificar Palavra em Frase.
        9 = Verificar Par ou Ímpar.
        10 = Verificar Números Positivos.
        11 = Comparar Dois Números (Maior/Menor).
        12 = Calcular IMC com Classificação.
        13 = Exemplo de Laço de Repetição (While).
        14 = Jogo de Adivinhação (Número Aleatório).
        15 = Validar URL.
        16 = Exemplo de Validação de Entrada (Stdin).
        17 = Exibir Frase Vertical e Horizontal.
        18 = Exibir Números Pares de 0 a 20.
        19 = Exibir Tabuada.
        20 = Contagem Regressiva de 20 Segundos.
        21 = Somar Números Ímpares de 1 a 100.
        22 = Verificar se um Número é Primo.
        23 = Verificar Palíndromo.
        24 = Somar Números com Quantidade Variável de Parâmetros.
        25 = Contar Letras Maiúsculas e Minúsculas.
        SAIR = Sair o programa.
        -> Digite sua escolha: """)
    
    if not funcaoPrincipal(opcao):
        break
