'''
Exemplo onde tempos um valor X ex: 1 e uma lista data de x valores ex: 1 2 4 1 2, o codigo conta quantas vezes o valor x foi repetido dentro da lista. 
'''

x = int(input())
valores = list(map(int, input().split()))

quantidade = valores.count(x)

print(quantidade)
