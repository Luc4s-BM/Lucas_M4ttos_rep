1#
"""
Pytz é uma bilioteca do Python que permite calular fusoshorários e
resolver problemas com horários ambiguos no final do horário de verão.

O Tzdata é um "pacote" de dados do Python que fornece dadosde fuso horário
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

#OU
from datetime import datetime, date
print(date.today())


#4
from datetime import datetime, time
horario_espeifico = time(14, 30, 59)
print(horario_espeifico)


















