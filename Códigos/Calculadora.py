while True:
    num1 = input("Digite um número: ")
    if num1.isnumeric():
        num1 = int(num1)
    else:
        print("Digite um número válido!")
        print("###FIM DO PROGRAMA###")
        break
    num2 = input("Digite outro número: ")
    if num2.isnumeric():
        num2 = int(num2)
    else: 
        print("Digite um número válido!")   
        print("###FIM DO PROGRAMA###")
        break
        
    operacao = input("Qual operação você deseja?\n-> Digite 1 para SOMA.\n-> Digite 2 para SUBTRAÇÃO.\n-> Digite 3 para MULTIPLICAÇÃO.\n-> Digite 4 para DIVISÃO.\nQual a sua escolha?: ")
    if operacao.isnumeric():
        operacao = int(operacao)
    else: 
        print("Digite um número válido!")   
        print("###FIM DO PROGRAMA###")
        break
    if operacao == 1:
        resultado = num1 + num2
        print(f"{num1} + {num2} = {resultado}")
    if operacao == 2:
        resultado = num1 - num2
        print(f"{num1} - {num2} = {resultado}")
    if operacao == 3:
        resultado = num1 * num2
        print(f"{num1} x {num2} = {resultado}")
    if operacao == 4:
        resultado = num1 / num2
        print(f"{num1} / {num2} = {resultado}")
    if operacao > 4 or operacao < 1:
        print("Digite um número válido!")
        print("###FIM DO PROGRAMA###")
        break
    
    