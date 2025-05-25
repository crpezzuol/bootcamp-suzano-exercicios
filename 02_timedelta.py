from datetime import datetime, timedelta

tipo_carro = input("\nTipo de carro (P, M, G): ").strip().upper()

tempo_pequeno = 30
tempo_medio = 45
tempo_grande = 60   
data_atual = datetime.now()


if tipo_carro == "P":
    data_estimada = data_atual + timedelta(minutes=tempo_pequeno)  
    print(f'\nO carro  chegou ás : {data_atual} \nE ficará pronto ás : {data_estimada}\n')

elif tipo_carro == "M":
    data_estimada = data_atual + timedelta(minutes=tempo_medio)
    print(f'\nO carro  chegou ás : {data_atual} \nE ficará pronto ás : {data_estimada}\n')

else:
    data_estimada = data_atual + timedelta(minutes=tempo_grande)
    print(f'\nO carro  chegou ás : {data_atual} \nE ficará pronto ás : {data_estimada}\n')