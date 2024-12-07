primeiroValorInformadoPeloUsuario = input("Digite o primeiro número: ")
segundoValorInformadoPeloUsuario  = input("Digite o segundo número: ")

#Validação do tipo de entrada informada pelo Stdin (teclado)
if not (primeiroValorInformadoPeloUsuario.strip().isnumeric()):
    print(f"O primeiro valor informado: \"{primeiroValorInformadoPeloUsuario}\" não é um valor numérico válido.")
elif (not (segundoValorInformadoPeloUsuario.strip().isnumeric())):
    print(f"O segundo valor informado: \"{segundoValorInformadoPeloUsuario}\" não é um valor numérico válido.")
else:
    opcaoDigitadaPeloUsuario = input("Informe um valor numérico de 1 a 10: ")
    
    #Validação do tipo de entrada informada pelo Stdin (teclado)
    if not (opcaoDigitadaPeloUsuario.strip().isnumeric()):
        print(f"A opção informada: \"{opcaoDigitadaPeloUsuario}\" é inválida. As opções numéricas válidas são: 1, 2, 3 ou 4.")
        
    elif (int(opcaoDigitadaPeloUsuario) <= 0 or int(opcaoDigitadaPeloUsuario) > 10):
        print(f"A opção informada: \"{opcaoDigitadaPeloUsuario}\" é inválida. As opções numéricas válidas são: 1, 2, 3 ou 4.")
    else:
        print("Todos os valores numéricos informados via stdin foram válidos.")    
        
        