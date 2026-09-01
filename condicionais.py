print("temperatura: ")
temperatura = 30 

# Condição compostas
if temperatura > 25:
    print("está quente, irei ligar a ventilação")
elif temperatura < 15:
    print("está frio, irei ligar o aquecimento")
else:
    print("está agradável, não preciso ligar nem o aquecimento nem a ventilação")

# Condições compostas com operadores lógicos (Copiado do curso para realizar a correção da atividade)

pressao_atual = 6.0  # Pressão atual em bar
pressao_maxima = 5.0  # Pressão máxima permitida em bar
pressao_minima = 1.0  # Pressão mínima segura em bar

print(f'Pressão atual: {pressao_atual} bar')

# Lógica condicional para controle da pressão
if pressao_atual > pressao_maxima or pressao_atual >= 4.0:
    print("Atenção: Pressão crítica! Acionando alívio de pressão.")
elif pressao_atual < pressao_minima or pressao_atual < 2.0:
    print("Atenção: Pressão muito baixa! Acionando compressor.")
else:
    print("Pressão dentro dos limites normais.")