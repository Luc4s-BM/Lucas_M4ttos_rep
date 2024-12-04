import time
limite_do_programa = 1
valor_informado = int(input("Informe um número: "))
print(f"Aqui está todos os números entre {valor_informado} e 1:")
while valor_informado >= limite_do_programa:
    print(f"-> {valor_informado}")
    time.sleep(0.2)
    valor_informado -= 1    