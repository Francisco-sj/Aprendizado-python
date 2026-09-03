# Importamos a biblioteca time para simular o tempo
import time

energia_atual = 50
energia_maxima = 100

while True:
    print(f"Energia atual: {energia_atual}")
    if energia_atual >= energia_maxima:
        print("Consumo de energia excedido! Desligando o sistema...")
        break

    # Incrementa a energia atual em 10 a cada iteração
    energia_atual += 10
    time.sleep(2) # Simula o tempo de carregamento