'''
Exemplo formula de Bhaskara simples
'''

# Entrada de tres valores float = 1.0 1.0 1.0, que seram salvos em listas
valores = list(map(float, input().split()))


# Nomeando os valores de cada lista
a = valores[0]
b = valores[1]
c = valores[2]

# Formula de Bhaskara
delta = (b ** 2) - (4 * a * c)

# Validado se delta menor que zero ou a igual a zero, retorna erro
if delta < 0 or a == 0 :
    print("Impossivel calcular")

# Caso a validação estiver ok faz o calculo das raizes
else:
    r1 = (-b + delta ** (1 / 2)) / (2 * a)
    r2 = (-b - delta ** (1 / 2)) / (2 * a)

    print("R1: {:.5f}".format(r1))
    print("R2: {:.5f}".format(r2))
