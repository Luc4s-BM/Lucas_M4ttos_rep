# -> A função "def", serve para armazenar um bloco de código para ser reutilizado ao decorrer do código.
# -> Serve para organização, e entendimento do código.

# -> Estrutura do "def":
    # def nome_função(parâmetros)
        # instrução1
        # instrução2
        # instrução3
        # ...
        # return valor <- *opcional*

# EXEMPLOS SIMPLES:

# Fazer somas

def soma(a,b):                             # 1. Define a função "soma()", com os parâmetros sendo (a,b).               
    resultado = a + b                      # 2. A varável "resultado" atribui a soma das variáveis "a + b".                                                                   
    print(resultado)                       # 3. Imprime o "reesultado".                                                                      
num1 = int(input("Digite um valor: "))     # 4. A variável "num1" recebe seu valor pelo usuário.                                                     
num2 = int(input("Digite outro valor: "))  # 5. A variável "num2" recebe seu valor pelo usuário.                                                                                                                       
soma(num1, num2)                           # 6. Executa o código que estava dentro da função "soma()".                                                                               

#===================================================================================

# Calcular impostos

def calcular_imposto(valor):                         # 1. Define a função "calcular_imposto()", com o parâmetro sendo o (valor).                                                                          
    if valor < 1000:                                 # 2. Verifica se o "valor" é menor que 1000.                                    
        imposto = valor * 0.1                        # 3. Se for TRUE, retorna "imposto" atribuindo o "valor" multiplicado por 0.1.                                                     
    elif valor < 2000:                               # 4. Verifica se o "valor" é maior que 1000 e menor que 2000.                                             
        imposto = valor * 0.15                       # 5. Se for TRUE, retorna "imposto" atribuindo o "valor" multiplicado por 0.15.                                                                                                      
    else:                                            # 6. Caso nenhuma das condições acima foram veradeiras.                                
        imposto = valor * 0.2                        # 7. Retorna "imposto" atribuindo o "valor" multiplicado por 0.2.                                                                                                          
    return imposto                                   # 8. A função irá retornar o "imposto".                                       
valor_produto = int(input("Digite o valor: "))       # 9. A variável "valor_produto" recebe seu valor pelo usuário.                                                                    
imposto_calculado = calcular_imposto(valor_produto)  # 10. A variável "imposto_calculado" atribui seu valor pela função "calcular_imposto()", e como parâmetro da função temos "valor_produto".                                                                         
print(f"R${imposto_calculado + valor_produto:.2f}")  # 11. Imprime o "valor_produto" somado com o "imposto_calculado".             