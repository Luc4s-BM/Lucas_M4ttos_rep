"""

Os métodos de string em Python são funções integradas que podem ser usadas 
diretamente em objetos do tipo "str" para realizar operações comuns, como 
modificar, formatar ou analisar textos. Strings são imutáveis em Python, então 
a maioria desses métodos retorna uma nova string sem alterar a original.

"""

#===================================================================================

# Principais Métodos de String:

# 1. "str.upper()": Converte todos os caracteres para maiúsculas.
texto = "hello"
print(texto.upper())  # Saída: HELLO

# ===================================================================================

# 2. "str.lower()": Converte todos os caracteres para minúsculas.
texto = "HELLO"
print(texto.lower())  # Saída: hello

# ===================================================================================

# 3. "str.capitalize()": Converte apenas o primeiro caractere da string para maiúscula.
texto = "python"
print(texto.capitalize())  # Saída: Python

# ===================================================================================

# 4. "str.title()": Converte o primeiro caractere de cada palavra para maiúscula.
texto = "python programming"
print(texto.title())  # Saída: Python Programming

# ===================================================================================

# 5. "str.strip()": Remove espaços (ou caracteres especificados) no início e no final da string.
texto = "  hello  "
print(texto.strip())  # Saída: hello

# ===================================================================================

# 6. "str.replace(old, new)": Substitui todas as ocorrências de old por new.
texto = "banana"
print(texto.replace("a", "o"))  # Saída: bonono

# ===================================================================================

# 7. "str.startswith(prefix)": Verifica se a string começa com o prefixo fornecido.
texto = "Python"
print(texto.startswith("Py"))  # Saída: True

# ===================================================================================

# 8. "str.endswith(suffix)": Verifica se a string termina com o sufixo fornecido.
texto = "Python"
print(texto.endswith("on"))  # Saída: True

# ===================================================================================

# 9. "str.isalpha()": Verifica se todos os caracteres são letras.
texto = "Hello"
print(texto.isalpha())  # Saída: True

# ===================================================================================

# 10. "str.isdigit()": Verifica se todos os caracteres são números.
texto = "12345"
print(texto.isdigit())  # Saída: True

# ===================================================================================

# 11. "str.isspace()": Verifica se a string contém apenas espaços.
texto = "   "
print(texto.isspace())  # Saída: True

# ===================================================================================

# 12. "str.split(sep)": Divide a string em uma lista usando o delimitador sep.
texto = "maçã,banana,laranja"
print(texto.split(","))  # Saída: ['maçã', 'banana', 'laranja']

# ===================================================================================

# 13. "str.join(iterable)": Junta elementos de um iterável em uma string usando o separador.
frutas = ["maçã", "banana", "laranja"]
print(", ".join(frutas))  # Saída: maçã, banana, laranja

# ===================================================================================

# 14. "str.find(sub)": Retorna o índice da primeira ocorrência de sub ou -1 se não encontrado.
texto = "banana"
print(texto.find("na"))  # Saída: 2

# ===================================================================================

# 15. "str.count(sub)": Conta o número de ocorrências de sub na string.
texto = "banana"
print(texto.count("a"))  # Saída: 3

# ===================================================================================

# 16. "str.zfill(width)": Adiciona zeros à esquerda até alcançar o comprimento especificado.
texto = "42"
print(texto.zfill(5))  # Saída: 00042