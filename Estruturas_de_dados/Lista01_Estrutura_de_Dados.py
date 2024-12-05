#1
dias_da_semana = ("Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sabádo", "Domingo")
meses_do_ano = ("Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro")
estacoes_do_ano =  ("Verão", "Outono"," Inverno", "Primavera")
data = (dias_da_semana, meses_do_ano, estacoes_do_ano)
def main(tupla):
    print("Dias da Semana: ", tupla[0])
    print("Meses do Ano: ", tupla[1])
    print("Estações do Ano: ", tupla[2])
print("Data Tipo Tupla:")
main(data)
print("="*50)

#2
dias_da_semana2 = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sabádo", "Domingo"]
meses_do_ano2 = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
estacoes_do_ano2 = ["Verão", "Outono"," Inverno", "Primavera"]
data2 = [dias_da_semana2, meses_do_ano2, estacoes_do_ano2]
def main2(lista):
    print("Dias da Semana: ", lista[0])
    print("Meses do Ano: ", lista[1])
    print("Estações do Ano: ", lista[2])
print("Data Tipo Lista:")   
main2(data2)
print("="*50)

#3
dias_da_semana3 = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sabádo", "Domingo"]
meses_do_ano3 = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
estacoes_do_ano3 = ["Verão", "Outono","Inverno", "Primavera"]

def imprimir(lista2):
    print("Tamanho: ", len(lista2))
    print("Dados: ", lista2[0], lista2[2], lista2[-1])
    
imprimir(dias_da_semana3)
imprimir(meses_do_ano3)
imprimir(estacoes_do_ano3)
print("="*50)

#4
def lista_de_compras():
    lista4 = []
    numero_do_item4 = 1
    while numero_do_item4 < 16: 
        item4 = input(f'-> Digite o {numero_do_item4}º item da sua lista de compras: ').strip().title()   
        numero_do_item4 = numero_do_item4 + 1 
        lista4.append(item4)
    print("Aqui está sua lista de compras: ", lista4, end=" ")
lista_de_compras()

""" Eu decidi usar o "while" junto com uma lista, achei o jeito mais simples de fazer isso. """

#5 
def menu_de_opcoes():
    decisao = input("Deseja fazer alguma alteração na sua lista?: ").lower().strip()
    if decisao == "sim":
        print("hjdsvw")
    elif decisao == "nao" or decisao == "não":
        print("Ok, fique com a sua lista!")

menu_de_opcoes()
"""  def adicionar_item_na_lista(item5):
    



"""