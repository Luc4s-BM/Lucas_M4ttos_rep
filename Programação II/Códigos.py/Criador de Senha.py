lista_especial = ["#", "@", "$", "&", "*"]
print("Crie sua senha!")

# Funções de validação
def verificar_numero(senha):
    if any(caractere.isdigit() for caractere in senha):
        return True
    print("A senha deve conter pelo menos um número!")
    return False

def verificar_letra_maiuscula(senha):
    if any(caractere.isupper() for caractere in senha):
        return True
    print("A senha deve conter pelo menos uma letra maiúscula!")
    return False

def verificar_caractere_especial(senha):
    if any(caractere in lista_especial for caractere in senha):
        return True
    print("A senha deve conter pelo menos um caractere especial!")
    return False

def verificar_letra_minuscula(senha):
    if any(caractere.islower() for caractere in senha):
        return True
    print("A senha deve conter pelo menos uma letra minúscula!")
    return False

while True:
    print(
        "A senha deve atender aos seguintes requisitos:\n"
        "-> Precisa haver pelo menos 1 letra maiúscula.\n"
        "-> Precisa haver pelo menos 1 letra minúscula.\n"
        "-> Precisa haver pelo menos 1 desses caracteres especiais: ('#@$&*').\n"
        "-> Precisa haver pelo menos 1 número."
    )
    senha_digitada_pelo_usuario = input("Digite sua senha: ")

    validar_numero = verificar_numero(senha_digitada_pelo_usuario)
    validar_letra_maiuscula = verificar_letra_maiuscula(senha_digitada_pelo_usuario)
    validar_letra_minuscula = verificar_letra_minuscula(senha_digitada_pelo_usuario)
    validar_caractere_especial = verificar_caractere_especial(senha_digitada_pelo_usuario)

    if validar_numero and validar_letra_maiuscula and validar_letra_minuscula and validar_caractere_especial:
        print("Senha criada com sucesso!")
        break
    else:
        print("A senha não atende os requisitos! Tente novamente.")
