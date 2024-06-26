'''
Exemplo onde o sistema verifica em qual intervalo o numero digitado se encontra dentro da lista, aceita numero x.xx
'''

valor = float(input("Insiva um valor: "))

intervalo = ([0, 25], 
             [25, 50], 
             [50, 75], 
             [75, 100])

a, b, c, d = intervalo

if valor >= a[0] and valor <= a[1]:
    print("Intervalo [0,25]")

elif valor > b[0] and valor <= b[1]:
    print("Intervalo [25,50]")

elif valor > c[0] and valor <= c[1]:
    print("Intervalo [50,75]")

elif valor > d[0] and valor <= d[1]:
    print("Intervalo [75,100]")

else:
    print("Fora de intervalo")
