def contar_consoantes(texto):
    consoantes = "BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyzÇçÑñ" 
    contador = 0
    for letra in texto:  
        if letra in consoantes: 
            contador += 1 
    return contador

texto_usuario = input("Digite um frase: ")

total_consoantes = contar_consoantes(texto_usuario)

def contar_vogais(texto):
    vogais = "aeiouáéíóúàèìòùãõâêîôûAEIOUÁÉÍÓÚÀÈÌÒÙÃÕÂÊÎÔÛ" 
    contador = 0
    for letra in texto:  
        if letra in vogais: 
            contador += 1 
    return contador
total_vogais = contar_vogais(texto_usuario)

print(f"A frase contém {total_vogais} vogais e {total_consoantes} consoantes.")