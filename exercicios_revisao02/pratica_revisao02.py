"""1) Escreva um programa que peça ao usuário que informe dois valores
numéricos de entrada, em seguida, exiba em tela o resultado da soma,
subtração, multiplicação e divisão desses números. NÃO UTILIZAR
FUNÇÃO P/ RESOLVER ESSA QUESTÃO. Se desejarem poderão
utilizar o conceito de FString, concatenação de String, qualquer uma das
sobrecargas de função responsável por imprimir no stdout."""

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

import random
def tamanho_da_senha(senha_tamanho):
    try: 
        tamanho_da_senha_a_ser_gerada = int(input("Digite o tamanho da senha (Max: 128): "))
        return tamanho_da_senha_a_ser_gerada
    except ValueError:
        print("Erro, digite apenas números!")
tamanho_da_senha_a_ser_gerada = tamanho_da_senha()     
uuid_gerador_senha = '35b35f68-9687-4ca6-bb79-f59201d40b0739e5b006-f4ab-49cb-a072-6549876b35dc'
senha_gerada = "  ".join(random.sample(uuid_gerador_senha, tamanho_da_senha_a_ser_gerada))
print(f"Senha gerada com {tamanho_da_senha_a_ser_gerada} caracteres: {senha_gerada}")








