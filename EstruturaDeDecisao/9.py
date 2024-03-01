#Faça um Programa que leia três números e mostre-os em ordem decrescente

n1 = int(input("Digite um número: "))
n2 = int(input("Digite um número: "))
n3 = int(input("Digite um número: "))

if n1 > n2 and n1 > n3:
    maior = n1
elif n2 > n1 and n2 > n3:
    maior = n2
elif n3 > n1 and n3 > n2:
    maior = n3
    
if n1 < n2 and n1 < n3:
    menor = n1
elif n2 < n1 and n2 < n3:
    menor = n2
elif n3 < n1 and n3 < n2:
    menor = n3
    
if n1 < n2 < n3 or n3 < n2 < n1:
    meio = n2
elif n1 < n3 < n2 or n2 < n3 < n1:
    meio = n3
elif n2 < n1 < n3 or n3 < n1 < n2:
    meio = n1


print(f"A ordem decrescente é: {maior}, {meio}, {menor}")