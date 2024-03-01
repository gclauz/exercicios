area = float(input("Digite o tamanho, em metros quadrados, da área a ser pintada: "))

litros = area / 3
latas = int(litros / 18)

if litros > 18:
    latas += 1
else:
    if litros <= 18:
        latas = 1

print("Você deve comprar", latas, "latas")
print("O preço total será de", latas * 80)