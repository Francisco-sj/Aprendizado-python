# Estrutura de repetição FOR
for i in range(10):
    print("Produto ", i+1)

# Estrutura de repetição WHILE
temperatura = float(input("Digite a temperatura: "))
while temperatura < 250:
    print("Adicionando mais lenha!")
    temperatura += 10

# Desafio simples: Imaginando um forno de pizza, que precisa se manter a uma temperatura de 180 graus Celsius para assar a pizza corretamente. Faça um programa que pergunte ao usuário a temperatura atual do forno e, caso esteja abaixo de 180 graus, o programa irá incrementar a temperatura em 10 graus até que atinja ou ultrapasse 180 graus, informando a cada incremento a temperatura atual do forno. E se a temperatura estiver acima de 180 graus, o programa irá retirar 10 graus até que atinja 180 graus, informando a cada decremento a temperatura atual do forno.
temperatura_forno = float(input("Digite a temperatura atual do forno: "))
temperatura_forno = round(temperatura_forno / 10) * 10 # Arredonda para o múltiplo de 10 mais próximo, fazendo assim a lógica de incremento e decremento funcionar corretamente.

if temperatura_forno < 180:
    while temperatura_forno < 180:
        print("Aquecendo o forno! Temperatura atual: ", temperatura_forno)
        temperatura_forno += 10
    print("O forno atingiu a temperatura ideal de 180 graus Celsius.")
elif temperatura_forno > 180:
    while temperatura_forno > 180:
        print("Resfriando o forno! Temperatura atual: ", temperatura_forno)
        temperatura_forno -= 10
    print("O forno atingiu a temperatura ideal de 180 graus Celsius.")
else:
    print("O forno já está na temperatura ideal de 180 graus Celsius.")