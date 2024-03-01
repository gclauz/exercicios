#Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.

p1 = float(input("Digite o preço do primeiro produto: R$"))
p2 = float(input("Digite o preço do segundo produto: R$"))
p3 = float(input("Digite o preço do terceiro produto: R$"))

menorPreco = p1

if p2 < p1:
    p2 = menorPreco
    
if p3 < p1:
    p3 = menorPreco
    
print(f"O produto que você deve comprar levando em consideração o preço final é o de R${menorPreco}")