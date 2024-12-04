ano_digitado_pelo_usuario = int(input("Digite algum ano aleatório: ")) 
if (ano_digitado_pelo_usuario % 4 == 0 and ano_digitado_pelo_usuario % 100 != 0) or ano_digitado_pelo_usuario % 400 == 0: 
    print(f"O ano de {ano_digitado_pelo_usuario} é bisexto!")
else: 
    print(f"O ano de {ano_digitado_pelo_usuario} não é bisexto!")