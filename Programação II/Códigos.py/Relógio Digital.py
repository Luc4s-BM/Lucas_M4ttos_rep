import datetime, time

while True:
    horario = datetime.datetime.now()
    time.sleep(0.5)
    print(horario.strftime("%H:%M:%S"),  end='\r')
    time.sleep(0.5)
