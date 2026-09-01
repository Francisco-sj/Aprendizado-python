# Dicionário de estados de máquinas
estados_de_maquinas = {
    "maquina1" : ["ligada", "desligada"],
    "maquina2" : "desligada",
    "maquina3" : "sem energia",
    "maquina4" : "defeito"
}

# Atualizando o dicionário com novos estados de máquinas(Utilizando o método update())
estados_de_maquinas.update({
    "maquina5" : "ligada",
    "maquina4" : "em manutenção"
})

# Acessando os estados de máquinas específicos
    # Forma direta e sem guardar valor em uma variável
print("Estado da máquina 1:", estados_de_maquinas["maquina1"])
print("Estado da máquina 4:", estados_de_maquinas["maquina4"])
    # Guardando valor em uma variável
estado_de_maquina2 = estados_de_maquinas["maquina2"]
print("Estado da máquina 2:", estado_de_maquina2)

# Atualizando o estado da máquina 4 diretamente
estados_de_maquinas["maquina4"] = "operacional"  

# Removendo um estádo de máquina do dicionário
del estados_de_maquinas["maquina5"]
print(f"Estados de máquinas atualizados: {estados_de_maquinas}")

# Verificando o tamanho do dicionário
print(f"Tamanho do dicionário de estados de máquinas: {len(estados_de_maquinas)}")

# Listando todas as máquinas cadastradas no dicionário
print(f"Lista de todas as máquinas cadastradas: {list(estados_de_maquinas.keys())}")

print(f"\nComando para as máquinas: {estados_de_maquinas}")

print(f"Primeiro comando para a máquina 1: {estados_de_maquinas['maquina1'].pop(0)}")
print(f"Segundo comando para a máquina 1 : {estados_de_maquinas['maquina1']}")