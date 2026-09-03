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

# Usando FOR novamente 
for ciclo in range(1, 6):
    consumo = 50 + (ciclo * 4)
    print(f"Ciclo {ciclo} - Consumo de energia atual: {consumo} Kw")

# FOR percorrendo listas 
leituras = [50, 60, 70, 80, 90, 100]
for leitura in leituras:
    print(f"Leitura de energia: {leitura} Kw")


#For percorrendo dicionários
Setores_consumo = {
    "Refrigeração": 50,
    "Iluminação": 40, 
    "Computadores": 100,
}

for setor, consumo in Setores_consumo.items():
    if consumo > 80:
        print(f"O setor {setor} está consumindo muita energia: {consumo} Kw")
    else:
        print(f"O setor {setor} está consumindo energia dentro do esperado: {consumo} Kw")