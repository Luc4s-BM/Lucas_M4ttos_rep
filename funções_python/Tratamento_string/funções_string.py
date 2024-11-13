#1

def calcular_tamanho_string(caracteres_da_string):
    if type(caracteres_da_string) == str:
        return len(caracteres_da_string)
    else:    
        return - 1 
    
letra_da_musica = input("Digite a String: ").strip()
tamanho_da_string_inserida = calcular_tamanho_string(letra_da_musica)

if tamanho_da_string_inserida <= 0: 
    print("Entrada inválida!")
else:
    print(tamanho_da_string_inserida)
    print(f'A String tem {tamanho_da_string_inserida} caracteres.')



