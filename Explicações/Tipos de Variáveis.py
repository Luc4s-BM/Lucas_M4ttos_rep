# Variáveis servem para armazenar valores, palavras etc... São essenciais para o funcionamento do código.
# Variáveis podem conter 4 tipos: Int, Float, String e Boolean.
# Cada uma com suas determinadas funcionalidades, aqui está alguns exemplos delas sendo utilizadas.

#===================================================================================

# Variável tipo "Int".
# Esse tipo de variável serve para armazenar valores INTEIROS.

# EXEMPLO:

idade = 34     # 1. O valor da variável "idade" é 34, um valor inteiro.
print(idade)   # 2. Imprime o valor da variavel "idade".

#===================================================================================

# Variável tipo "Float".
# Esse tipo de variável serve para armazenar números com CASAS DECIMAIS.

# EXEMPLO:

dinheiro = 20.45    # 1. O valor da variável "dinheiro" é 20.45, um valor com casas decimais.
print(dinheiro)     # 2. Imprime o valor da variavel "dinheiro".

#===================================================================================

# Variável tipo "String".
# Esse tipo de variável serve para armazenar CARACTERES, ou seja, não valores númericos.

# EXEMPLO:

nome = "joão"   # 1. A string da variável "nome" é "joão".
print(nome)     # 2. Imprime a string da variável "nome".

#===================================================================================

# Variável tipo "Boolean".
# Esse tipo de variável serve para armazenar valores verdadeiros (TRUE) ou falsos (FALSE).

# EXEMPLO TRUE:

palavra = True      # 1. Define a variável "palavra" como verdadeira (True).
print(palavra)      # 2. Imprime a condição da variável "palavra".

# EXEMPLO FALSE:

palavra2 = False    # 1. Define a variável "palavra" como falsa (False).
print(palavra2)     # 2. Imprime a condição da variável "palavra".

#===================================================================================

# Como descobrir qual o tipo da variável:

# Podemos usar a função "type()", ela mostrará qual o tipo da variável no terminal.

# Estrutura da função "type()":
    # variavel_exemplo = 235
    # print(type(variavel_exemplo))

# Vamos utilizar os exemplos acima. 

#===================================================================================

# EXEMPLO INT:

idade = 34 
print(type(idade))
# Mensagem no Terminal: <class 'int'>

#===================================================================================

# EXEMPLO FLOAT:

dinheiro = 20.45
print(type(dinheiro))
# Mensagem no Terminal: <class 'float'>

#===================================================================================

# EXEMPLO STRING:

nome = "joão"
print(type(nome))  
# Mensagem no Terminal<class 'str'>


#===================================================================================

# EXEMPLO BOOLEAN:

palavra = True 
print(type(palavra))
# Mensagem no Terminal: <class 'bool'>

#===================================================================================