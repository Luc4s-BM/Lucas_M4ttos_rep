"""frase = input("Digite sua frase: ")

def quantidade_de_letras(letras):
    return len(letras)

quantidade = quantidade_de_letras(frase)
print(f"A quantidade de caracteres na frase é: {quantidade}")

nome = "LucasMattos"
print(nome.find("a"))
print(nome.upper())
print(nome.lower())
print(nome.isdigit())
print(nome.isalpha())
print(nome.count("a"))

nome1 = input("Digite seu nome: ")
print("Olá "+ nome1)

x = 1
try:
    print(x)
except:
    print("An exception occurred")

try:
    print("Hello")
except:
    print("Something went wrong")
else:
    print("Nothing went wrong")

frase = "Hello World"
corte = frase.split()
print(corte)
num1 = 3
if not num1<4:
    print("ok")
else:
    print("Not ok")


texto = "python é muito chato"
print(texto.replace(" ",""))


print("Welcome to", end = ' ')
print("GeeksforGeeks", end= ' ')
print("Fodase")


x = 'apple', 'banana', 'cherry'
y = enumerate(x, start=1)
print(list(y))"""

"""def validar_dados():
    a = input("Digite um número: ")
    try:
        str(a)
    except TypeError:
        print("Digite um valor válido!")
        return validar_dados()
b = validar_dados()

"""

def validar_frase():
    while True:
        entrada = input("Digite uma frase contendo apenas letras e espaços: ").strip()
        if entrada.replace(" ", "").isalpha():
            return entrada
        else:
            print("Erro! A frase só pode conter letras e espaços.")

frase = validar_frase()
print(f"Você digitou: '{frase}'")
