# Declarando uma lista de temperaturas em Celsius
temp_celsius = [23.5, 25.6, 33.3]
print(f"Temperature in Celsius: {temp_celsius}")

# Fazendo modificações na lista> Adicionando novos itens e removendo um item
temp_celsius.append(28.4)
temp_celsius.append(25.7)
temp_celsius.append(33.3)
temp_celsius.remove(33.3)
print(f"Atualização Temperature in Celsius: {temp_celsius}")

# Primeira e última leitura sendo mostrada na tela
primeira_leitura = temp_celsius[0]
print(f"Primeira leitura: {primeira_leitura}")
ultima_leitura = temp_celsius[-1]
print(f"Última leitura: {ultima_leitura}")

# Atualizando item em posição específica
temp_celsius[3] = 26.0
print(f"Atualização em 4ª posição: {temp_celsius}")

# Removendo item em posição específica
temp_celsius.pop(2)
print(f"Atualização após remover 3ª posição: {temp_celsius}")

# Ordenação da lista 
temp_celsius.sort()
print(f"Temperaturas ordenadas: {temp_celsius}")

# Quantidade de itens na lista
print(f"Quantidade de leituras: {len(temp_celsius)}")

if 26.1 in temp_celsius:
    print("A temperatura 26.1 está na lista.")
else:
    print("A temperatura 26.1 não está na lista.")