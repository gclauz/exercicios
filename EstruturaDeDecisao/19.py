#Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do mesmo.
#Observando os termos no plural a colocação do "e", da vírgula entre outros. 
# Exemplo:
# 326 = 3 centenas, 2 dezenas e 6 unidades
#12 = 1 dezena e 2 unidades 
#Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16

n = int(input("Digite um número: "))

if n >= 1000:
    print("Digite um número maior que 0 e menor que 1000")
    n = int(input("Digite um número: "))
    
uni = n % 10

n = (n - uni)/10
dez = n % 10

n = (n - dez)/10
cent = n

uni = int(uni)
dez = int(dez)
cent = int(cent)

if uni > 1 and dez > 1 and cent > 1:
    print(f"{cent} centenas, {dez} dezenas e {uni} unidades")
    
elif uni <= 1 and dez > 1 and cent > 1:
    print(f"{cent} centenas, {dez} dezenas e {uni} unidade")
    
elif uni <= 1 and dez <= 1 and cent > 1:
    print(f"{cent} centenas, {dez} dezena e {uni} unidade")
    
elif uni <= 1 and dez <= 1 and cent <= 1:
    print(f"{cent} centena, {dez} dezena e {uni} unidade")
    
elif uni > 1 and dez > 1 and cent <= 1:
    print(f"{cent} centena, {dez} dezenas e {uni} unidades")
    
elif uni > 1 and dez <= 1 and cent <= 1:
    print(f"{cent} centena, {dez} dezena e {uni} unidades")
    
elif uni <= 1 and dez > 1 and cent <= 1:
    print(f"{cent} centena, {dez} dezenas e {uni} unidade")
    
else: 
    uni > 1 and dez <= 1 and cent > 1
    print(f"{cent} centenas, {dez} dezena e {uni} unidades")