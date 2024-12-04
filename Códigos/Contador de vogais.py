def contar_vogais(texto):
    vogais = "aeiouáéíóúàèìòùãõâêîôûAEIOUÁÉÍÓÚÀÈÌÒÙÃÕÂÊÎÔÛ" 
    contador = 0
    for letra in texto:  
        if letra in vogais: 
            contador += 1 
    return contador

texto_usuario = input("Digite um frase: ")

total_vogais = contar_vogais(texto_usuario)

print(f"A frase contém {total_vogais} vogais.")
