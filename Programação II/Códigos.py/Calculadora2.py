class Calculadora:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def soma(self):
        return self.num1 + self.num2

    def subtracao(self):
        return self.num1 - self.num2

    def multiplicacao(self):
        return self.num1 * self.num2

    def divisao(self):
        if self.num2 == 0:
            return "Erro: Divisão por zero!"
        return self.num1 / self.num2

    def exponenciacao(self):
        return self.num1 ** self.num2

    def divisao_inteira(self):
        if self.num2 == 0:
            return "Erro: Divisão por zero!"
        return self.num1 // self.num2

    def modulo(self):
        if self.num2 == 0:
            return "Erro: Divisão por zero!"
        return self.num1 % self.num2

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
operacao = Calculadora(num1, num2)

print("\n--- Escolha a operação desejada ---")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")
print("5 - Exponenciação")
print("6 - Divisão Inteira")
print("7 - Módulo")

escolha = int(input("Digite o número da operação: "))
if escolha == 1:
    print(f"O resultado da soma entre {num1} e {num2} é: {operacao.soma()}")
elif escolha == 2:
    print(f"O resultado da subtração entre {num1} e {num2} é: {operacao.subtracao()}")
elif escolha == 3:
    print(f"O resultado da multiplicação entre {num1} e {num2} é: {operacao.multiplicacao()}")
elif escolha == 4:
    print(f"O resultado da divisão entre {num1} e {num2} é: {operacao.divisao()}")
elif escolha == 5:
    print(f"O resultado da exponenciação entre {num1} e {num2} é: {operacao.exponenciacao()}")
elif escolha == 6:
    print(f"O resultado da divisão inteira entre {num1} e {num2} é: {operacao.divisao_inteira()}")
elif escolha == 7:
    print(f"O resultado do módulo entre {num1} e {num2} é: {operacao.modulo()}")
else:
    print("Opção inválida! Por favor, escolha um número entre 1 e 7.")
