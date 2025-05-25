from datetime import datetime, timedelta

tipo_carro = input("\nTipo de carro (P, M, G): ").strip().upper()

tempo_pequeno = 30
tempo_medio = 45
tempo_grande = 60   
data_atual = datetime.now()
mascara_ptbr = "%a dia %d/%m/%Y ás %H:%Mhs"

if tipo_carro == "P":
    data_estimada = data_atual + timedelta(minutes=tempo_pequeno)  
    print(f'\nO carro  chegou {data_atual.strftime(mascara_ptbr)} \nE ficará pronto {data_estimada.strftime(mascara_ptbr)}\n')

elif tipo_carro == "M":
    data_estimada = data_atual + timedelta(minutes=tempo_medio)
    print(f'\nO carro  chegou {data_atual.strftime(mascara_ptbr)} \nE ficará pronto {data_estimada.strftime(mascara_ptbr)}\n')

else:
    data_estimada = data_atual + timedelta(minutes=tempo_grande)
    print(f'\nO carro  chegou {data_atual.strftime(mascara_ptbr)} \nE ficará pronto {data_estimada.strftime(mascara_ptbr)}\n')