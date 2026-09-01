a, b, c , d = 7, 3, 5, 2
print(((a * b) + (c / d)) - (a ** b))

x, y, z = 10, 20, 30
print((x < y and y > z) or (x + y == z and not (z == x * 3)))

m, n, p = 25, 35, 45
print(((m + n) > (p * 2)) and ((p / n) < m) or (n == m + p))

# Leitura das variáveis (não altere estas linhas)
a = int(input())
b = int(input())
c = int(input())
d = int(input())

# Escreva abaixo a expressão matemática e imprima o resultado:
r = ((a * b) + (c / d)) - (a ** b) 
print(r)