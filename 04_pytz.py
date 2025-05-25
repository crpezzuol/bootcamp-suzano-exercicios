from datetime import datetime, timedelta, timezone

import pytz

# pytz é uma biblioteca que permite trabalhar com fusos horários de forma mais fácil
data = datetime. now(tz=pytz.timezone("Europe/Oslo"))
data2 = datetime. now(tz=pytz.timezone("America/Sao_Paulo"))

# timezone é uma classe do módulo datetime que permite trabalhar com fusos horários
data_oslo = datetime.now(timezone(timedelta(hours=2)))
data_sao_paulo = datetime.now(timezone(timedelta(hours=-3)))


print('\n')
print(data)
print(data2)
print('\n')
print(data.strftime("%d/%m/%Y %H:%M:%S"))
print(data2.strftime("%d/%m/%Y %H:%M:%S"))
print('\n')
print(data.strftime("%d/%m/%Y %H:%M:%S %Z"))
print(data2.strftime("%d/%m/%Y %H:%M:%S %Z"))
print('\n')
print(data.strftime("%d/%m/%Y %H:%M:%S %Z %z"))
print(data2.strftime("%d/%m/%Y %H:%M:%S %Z %z"))
print('\n')
print(data.strftime("%d/%m/%Y %H:%M:%S %Z %z %A"))
print(data2.strftime("%d/%m/%Y %H:%M:%S %Z %z %A"))
print('\n')
print(data.strftime("%d/%m/%Y %H:%M:%S %Z %z %A %B"))
print(data2.strftime("%d/%m/%Y %H:%M:%S %Z %z %A %B"))
print('\n')