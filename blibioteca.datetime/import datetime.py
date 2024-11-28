import time
import datetime

while True:
    hora = datetime.datetime.now()
    time.sleep(0.5)
    print(hora.strftime("%H:%M:%S"))
    time.sleep(0.5)