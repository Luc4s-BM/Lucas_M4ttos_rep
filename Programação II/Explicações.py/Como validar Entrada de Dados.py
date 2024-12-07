# Formas de avaliar uma entrada de dados INT:

# 1 - Validação com `try` e `except` dentro de um loop
def validar_entrada1():
    while True:
        try:
            valor = int(input("Digite um número: "))
            return valor
        except ValueError:
            print("Erro! Isso não é um número válido. Tente novamente.")

numero1 = validar_entrada1()
print(f"Você digitou o número: {numero1}")

# ===================================================================================

# 2 - Validação usando `isdigit`
def validar_entrada2():
    while True:
        valor = input("Digite um número: ")
        if valor.isdigit():  # Verifica se a string contém apenas dígitos
            return int(valor)
        else:
            print("Erro! Isso não é um número válido. Tente novamente.")

numero2 = validar_entrada2()
print(f"Você digitou o número: {numero2}")

# ===================================================================================

# 3 - Validação recursiva com `try` e `except`
def validar_entrada3():
    valor = input("Digite um número: ")
    try:
        return int(valor)
    except ValueError:
        print("Erro! Isso não é um número válido. Tente novamente.")
        return validar_entrada3()  # Chama a função novamente

numero3 = validar_entrada3()
print(f"Você digitou o número: {numero3}")

# ===================================================================================

# 4 - Validação com retorno explícito de `None` para valores inválidos
def validar_entrada4(valor):
    try:
        return int(valor)  # Tenta converter para inteiro
    except ValueError:
        return None  # Retorna None se houver erro

while True:
    numero4 = input("Digite um número: ")
    numero_valido4 = validar_entrada4(numero4)
    if numero_valido4 is not None:
        print(f"Você digitou o número: {numero_valido4}")
        break
    else:
        print("Erro! Isso não é um número válido. Tente novamente.")

# ===================================================================================

# 5 - Validação recursiva simplificada
def validar_entrada5():
    valor = input("Digite um número: ")
    try:
        return int(valor)
    except ValueError:
        print("Erro! Isso não é um número válido. Tente novamente.")
        return validar_entrada5()  # Recursão

numero5 = validar_entrada5()
print(f"Você digitou o número: {numero5}")

# ===================================================================================

# 6 - Validação com loop e retorno imediato
def validar_entrada6():
    while True:
        valor = input("Digite um número: ")
        try:
            valor = int(valor)
            return valor
        except ValueError:
            print("Erro! Isso não é um número válido. Tente novamente.")

numero6 = validar_entrada6()
print(f"Você digitou o número: {numero6}")

# ===================================================================================

# Forma de avaliar uma entrada de dados STR:

def validar_frase():
    while True:
        entrada = input("Digite uma frase contendo apenas letras e espaços: ").strip()
        if entrada.replace(" ", "").isalpha():
            return entrada
        else:
            print("Erro! A frase só pode conter letras e espaços.")

frase = validar_frase()
print(f"Você digitou: '{frase.capitalize()}'")