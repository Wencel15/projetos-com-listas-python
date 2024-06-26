segundos = int(input("Digite os segundos: "))

tempo = [3600, 60, 1]
quantidades =[]


for contador in tempo:
    quantidade = segundos // contador
    quantidades.append(quantidade)
    segundos %= contador

hh, mm, ss = quantidades

print(f"{hh:02}:{mm:02}:{ss:02}")
