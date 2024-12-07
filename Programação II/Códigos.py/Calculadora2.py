def checar_numeros(a, b):
    if not (a.isnumeric() and b.isnumeric()):
        print("Digite números válidos!")
        return False
    else:
        return True
while True:
    num1 = input("Digite o primeiro número: ")
    num2 = input("Digite o segundo número: ")
    if checar_numeros(num1, num2):
        num1, num2 = int(num1), int(num2)  
        break

