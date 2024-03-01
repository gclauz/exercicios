area = int(input("Digite o tamanho, em metros quadrados, da área a ser pintada: "))

litros = area / 6
latas = litros / 18

if latas % 18 != 0:
    latas += 1
preco1 = latas * 80

galao1 = litros / 3.6
if galao1 % 3.6 != 0:
    galao1 += 1
preco2 = galao1 * 25

lata = int(litros / 18.0)
galao2 = int((litros - (lata * 18)) / 3.6)

if litros - (lata * 18) % 3.6 != 0:
    galao2 += 1
preco3 = lata * 80 + galao2 * 25

print(f"Comprar apenas latas de 18 litros, você precisará de {int(latas)} latas e pagará R$ {int(preco1)}")
      
print(f"Comprar apenas galões de 3,6 litros, você precisará de {int(galao1)} galões e pagará R$ {int(preco2)}")

print(f"Você precisará de {lata} latas de 18 litros e {galao2} galoes de 3.6 litros, o preço total é de R$ {preco3}")