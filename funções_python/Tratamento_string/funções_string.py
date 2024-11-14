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
def pegar_caracteres_da_string(lista_dos_caracteres, posicao_dos_caracteres):
    tamanho_da_string_passada = len(lista_dos_caracteres)
    
    if posicao_dos_caracteres >= tamanho_da_string_passada or posicao_dos_caracteres < 0:
        return -1 
    else:
        return lista_dos_caracteres[posicao_dos_caracteres]  # Retorna o caractere na posição

string_passada = input("Digite uma frase qualquer:\n")
indice_acessado_string = input("Informe um índice numérico a ser acessado na frase (Começará do zero): ")

if not indice_acessado_string.isdigit():
    print("Por favor, informe um índice válido!")
elif int(indice_acessado_string) < 0:
    print("Por favor, informe um índice positivo ou ZERO!")
else:
    indice_acessado_string = int(indice_acessado_string)
    caractere = pegar_caracteres_da_string(string_passada, indice_acessado_string)
    
    if caractere == -1:
        print(f"A posição {indice_acessado_string} não existe na string \"{string_passada}\" \n")
        for indice_caracter in enumerate(len(string_passada)):
            print(f"No índice {indice_caracter} temos o caractere '{string_passada[indice_caracter]}'")
    else:
        print(f"Na {indice_acessado_string}ª posição da string \"{string_passada}\" temos o caractere '{caractere}'")
        
#3
def exibir_caracteres_e_posicoes(string):
    for indice, caracter in enumerate(string):
        print(f"{caracter} - {indice + 1}º caracter da String")
string_passada = input("Digite uma frase qualquer:\n")
exibir_caracteres_e_posicoes(string_passada)

#4








































