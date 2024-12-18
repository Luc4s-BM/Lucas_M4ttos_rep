from custom_utils import utils

#1
dias_da_semana = ("Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sabádo", "Domingo")
meses_do_ano = ("Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro")
estacoes_do_ano =  ("Verão", "Outono"," Inverno", "Primavera")
data = (dias_da_semana, meses_do_ano, estacoes_do_ano)
print("Data Tipo Tupla:")
utils.main(data)
print("="*50)

#2
dias_da_semana2 = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sabádo", "Domingo"]
meses_do_ano2 = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
estacoes_do_ano2 = ["Verão", "Outono"," Inverno", "Primavera"]
data2 = [dias_da_semana2, meses_do_ano2, estacoes_do_ano2]
print("Data Tipo Lista:")   
utils.main2(data2)
print("="*50)

#3
dias_da_semana3 = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sabádo", "Domingo"]
meses_do_ano3 = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
estacoes_do_ano3 = ["Verão", "Outono","Inverno", "Primavera"]
utils.imprimir(dias_da_semana3)
utils.imprimir(meses_do_ano3)
utils.imprimir(estacoes_do_ano3)
print("="*50)

#4 - 5
utils.questao4()
print("=" * 50)

#6
linguagens_ocultas = ["C", "C++", "JavaScript", "Java", "Lua", "Python"]
utils.adivinhar_linguagem_oculta()
print("="*50)

#7
lista_de_medicos = ["alice monteiro", "lucas almeida", "beatriz carvalho", "gabriel nogueira", "marina fernandes", "rafael costa", "sofia martins"]
utils.escolher_medico()
print("="*50)