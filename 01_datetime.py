from datetime import date, datetime

data = date(2025, 1, 2)
print(data) # 2025-05-24
print(data.year) # ano 2025
print(data.month) # mês 5
print(data.day) # dia 24

data_hoje = date.today()
print(data_hoje) # data de hoje

print(data.today()) # data de hoje

data_hoje = datetime.today()
print(data_hoje) # data e hora de hoje