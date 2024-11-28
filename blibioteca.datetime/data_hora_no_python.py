#1
"""
Pytz é uma bilioteca do Python que permite calular fusoshorários e
resolver problemas com horários ambiguos no final do horário de verão.

O Tzdata é um "pacote" de dados do Python que fornece dados pppipde fuso horário
IANA. Ele é principalmente usado pelo módulo "zoneinfo" da blioteca padrão, 
mas também pode ser usado como fonte de dados de fuso horário para outras
bibliotecas de fuso horário.
"""

#2
from datetime import datetime, date, time, timedelta
print(datetime.now())


#3
import datetime
hora_de_agora = datetime.datetime.now()
print(hora_de_agora.strftime("%d/%m/%Y"))

#Formato americano
from datetime import datetime, date
print(date.today())


#4
from datetime import datetime, time
horario_especifico = time(14, 30, 59)
print(horario_especifico)


#5

from datetime import datetime, date, time, timedelta
import locale
locale.setlocale(locale.LC_ALL, "UTF-8.pt-BR")
data_hora_locale = datetime.now()
data_formatada = data_hora_locale.strftime("%x")
hora_formatada = data_hora_locale.strftime("%X")
print("Data formatada: ", data_formatada)
print("Hora formatada: ", hora_formatada)


















