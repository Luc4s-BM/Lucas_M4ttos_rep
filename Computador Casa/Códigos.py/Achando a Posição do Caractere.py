def funcao_achar_caractere(caractere, frase):
    posicoes = []
    for i, c in enumerate(frase): 
        if c == caractere:
            posicoes.append(i) 
    return posicoes

frase = input("Digite sua frase: ")
achar_caractere = input("Digite o caractere que deseja encontrar: ")

resultado = funcao_achar_caractere(achar_caractere, frase)

if resultado:
    print(f"O caractere '{achar_caractere}' aparece nas posições: {resultado}")
else:
    print(f"O caractere '{achar_caractere}' não foi encontrado na frase.")

