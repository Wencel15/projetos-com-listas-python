'''
Exemplo onde converte a quantidade de dias em anos, meses e dias.
'''

# Entrada de valores convertido em inteiro
dias = int(input("Digite a quantidade de dias: "))

# Lista com os valores de doas por anop, mes e dia
tempo = [365, 30, 1]
quantidades = []

# Itera sobre cada item da lista, contado quantas divisões são possiveis pelo valor do dia, adicionando a contagem em uma lista (quantidades) e posteriormente subtrai o valor usado para o proximo laço.
for contador in tempo:
    quantidade = dias // contador
    quantidades.append(quantidade)
    dias %= contador

# Nomeando cada item dentro da lista quantidades
ano, mes, dia = quantidades

print(f"{ano} ano(s), {mes} mes(es), {dia} dia(s)")
