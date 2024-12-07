# Os controles de loop, muda a ordem de execução do loop determinado.

# Tipos de loop: "while" e o "for".

# Tipos de controles de loop:

# break = Termina o loop por completo.
# continue = Pula para a próxima parte do loop.
# pass = Não faz nada, serve como um marcador.

#===================================================================================

# EXEMPLO BREAK:

while True:
    nome = input("Digite seu nome: ")
    if nome != "":
        break

# Esse loop vai continuar até que o usuário digite algo no terminal.

#===================================================================================

# EXEMPLO CONTINUE:

numero_de_telefone = "1234-5678"

for i in numero_de_telefone:
    if i == "-":
        continue
    print(i, end="")
    

# Esse loop vai checar cada caractere do "numero_de_telefone", e quando o "i" for igual á "-", pulará esse caractere, imprimindo apenas os números.

#===================================================================================

# EXEMPLO PASS

for i in range(1, 21):
    if i == 13:
        pass
    else:
        print(i, end=", ")

# Esse loop imprime números de 1 a 20, mas ele pulará o número 13













