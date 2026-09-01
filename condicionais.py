print("temperatura: ")
temperatura = float(input()) # Entrada de dados do usuário

# Condição compostas
if temperatura > 25:
    print("está quente, irei ligar a ventilação")
elif temperatura < 15:
    print("está frio, irei ligar o aquecimento")
else:
    print("está agradável, não preciso ligar nem o aquecimento nem a ventilação")