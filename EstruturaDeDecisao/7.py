#Faça um Programa que leia três números e mostre o maior e o menor deles

n1 = float(input("Digite um número: "))
n2 = float(input("Digite um número: "))
n3 = float(input("Digite um número: "))

maior = n1

if n2 > maior:
    maior = n2
    
if n3 > maior:
    maior = n3
    
menor = n2

if n1 < n2:
    menor = n1

if n3 < n2:
    menor = n3 
    
print(f"O maior número é {maior} e o menor é {menor}")
