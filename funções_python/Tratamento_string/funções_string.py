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



