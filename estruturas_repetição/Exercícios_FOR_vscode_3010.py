#1
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

#2    
    print("Números pares de 0 a 20:")
    for numeros_de_0_a_20 in range(0,21, 2):
        print("->", numeros_de_0_a_20)
  
#3
    tabuada_escolhida_pelo_usuario = int(input("Qual tabuada você gostaria de ver?: ")) 
    
    for numero_da_tabuada in range (0,11):
        print(f"{numero_da_tabuada} x {tabuada_escolhida_pelo_usuario} = {numero_da_tabuada * tabuada_escolhida_pelo_usuario}")
        
#4






        