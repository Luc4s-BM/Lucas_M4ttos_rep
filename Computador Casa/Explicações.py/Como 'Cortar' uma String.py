# Podemos "cortar" uma String usando "[]" ao lado da variável.

# Estrutura: variável_exemplo[começo:fim:passo]

# EXEMPLOS:
#===================================================================================

#1. Cortar do início ao meio

texto = "Python"
corte = texto[:3]  # Pega do início (índice 0) até o índice 3 (não incluso)
print(corte)  # Saída: Pyt

#===================================================================================

#2. Cortar do meio até o final

texto = "Python"
corte = texto[3:]  # Pega do índice 3 até o final
print(corte)  # Saída: hon

#===================================================================================

#3. Cortar usando índices específicos

texto = "Python"
corte = texto[1:4]  # Pega do índice 1 até o 4 (não incluso)
print(corte)  # Saída: yth

#===================================================================================

#4. Cortar com um passo

texto = "Python"
corte = texto[::2]  # Pega do início ao final, pulando de 2 em 2
print(corte)  # Saída: Pto

#===================================================================================

#5. Inverter a string

texto = "Python"
invertida = texto[::-1]  # Passo negativo (-1) inverte a string
print(invertida)  # Saída: nohtyP

#===================================================================================

#6. Cortar com passo negativo

texto = "Python"
corte = texto[4:1:-1]  # Pega do índice 4 ao índice 1 (exclusivo), na ordem inversa
print(corte)  # Saída: oht

#===================================================================================

#7. Remover os primeiros e últimos caracteres

texto = "Python"
corte = texto[1:-1]  # Pega do índice 1 ao penúltimo caractere
print(corte)  # Saída: ytho

#===================================================================================

# Método ".split()" e "slice()".
# Essas são outras formas de "cortar" strings.

# 1. "split()": Separa palavras com base em espaços ou outro delimitador.

frase = "Aprendendo Python é divertido"
palavras = frase.split()  # Divide a string em palavras
print(palavras)  # Saída: ['Aprendendo', 'Python', 'é', 'divertido']

#===================================================================================

# 2. "slice()": Separa strings (ou sequências como listas, tuplas, etc.) em Python. 
# Ele cria um objeto de slice, que pode ser usado para realizar fatiamentos mais explícitos.

# Estrutura do "slice()": slice(início, fim, passo)

#EXEMPLO: 

texto = "Python"
corte = slice(1, 4)  # Cria um objeto slice que equivale a [1:4]
print(texto[corte])  # Saída: yth


