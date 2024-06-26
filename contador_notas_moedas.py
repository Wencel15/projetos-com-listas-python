'''
Exemplo 01

Suponha que você tenha um valor de R$ X,XX e queira saber quantas notas e moedas são necessárias para formar esse valor.
O código imprime as quantidades de notas e moedas necessárias para compor o valor inserido
'''

valor = float(input("Digite o valor: ")) # O valor de entrada como float para valores com centavos
valor = int(round(valor * 100))  # Converte o valor incerido para centavos

notas = [10000, 5000, 2000, 1000, 500, 200]  # Valores das notas em centavos
moedas = [100, 50, 25, 10, 5, 1]  # Valores das moedas em centavos

quantidades_notas = []
quantidades_moedas = []

# Calculando a quantidade de notas com for: Itera sobre cada valor na lista notas, depois divide o valor atual pelo valor da moeda usando divisão inteira (//), e retorna a quantidade máxima de notas,
# adiciona quantidade .append em (quantidades) por fim subtrai o valor total das notas  valor atual, atualizando valor para o restante que ainda precisa ser convertido.
for nota in notas:
    quantidade = valor // nota
    quantidades_notas.append(quantidade)
    valor -= quantidade * nota

# Calculando a quantidade de moedas. 
for moeda in moedas:
    quantidade = valor // moeda
    quantidades_moedas.append(quantidade)
    valor -= quantidade * moeda

# Imprimindo os resultados. for Itera sobre os índices da lista imprimindo a quantidade armazenada.
print("NOTAS:")
for i in range(len(notas)):
    print(f"{quantidades_notas[i]} nota(s) de R$ {notas[i] / 100:.2f}")

print("MOEDAS:")
for i in range(len(moedas)):
    print(f"{quantidades_moedas[i]} moeda(s) de R$ {moedas[i] / 100:.2f}")
