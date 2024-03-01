#Um posto está vendendo combustíveis com a seguinte tabela de descontos:

#a. Álcool:
#b. até 20 litros, desconto de 3% por litro
#c. acima de 20 litros, desconto de 5% por litro

#d. Gasolina:
#e. até 20 litros, desconto de 4% por litro
#f. acima de 20 litros, desconto de 6% por litro 

# Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.
menu = '''

[A] = Álcool
[G] = Gasolina

'''
print(menu)

opcao = input("Escolha uma opção: ")

if opcao == "A" or opcao == "a":
    litros_combustivel = float(input("Informe a quantidade de litros desejada: "))
    preco = 1.90 * litros_combustivel
    
    if litros_combustivel <= 20:
        preco = preco - (1.90 * litros_combustivel * 0.03)
    else:
        preco = preco - (1.90 * litros_combustivel * 0.05)
        
    print(f"Valor a ser pago: {preco}")    
    
elif opcao == "G" or opcao == "g":
    litros_combustivel = float(input("Informe a quantidade de litros desejada: "))
    preco = 2.50 * litros_combustivel
    
    if litros_combustivel <= 20:
        preco = preco - (2.50 * litros_combustivel * 0.04)
    else:
        preco = preco - (2.50 * litros_combustivel * 0.06)
        
    print(f"Valor a ser pago: R${preco:.2f}")     