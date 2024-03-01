#Uma fruteira está vendendo frutas com a seguinte tabela de preços:
#                Até 5 Kg                Acima de 5 Kg
#Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
#Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg
#Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá ainda um desconto de 10% sobre este total. Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.

qtd_quilos_morango = int(input("Informe a quantidade de morango em quilos: "))
qtd_quilos_maca = int(input("Informe a quantidade de maçãs em quilos: "))

preco_morango1 = 2.50 * qtd_quilos_morango
preco_morango2 = 2.20 * qtd_quilos_morango

preco_maca1 = 1.80 * qtd_quilos_maca
preco_maca2 = 1.50 * qtd_quilos_maca

if qtd_quilos_morango <= 5:
    preco_morango = preco_morango1
    
else:
    preco_morango = preco_morango2
    

if qtd_quilos_maca <= 5: 
    preco_maca = preco_maca1
    
else:
    preco_maca = preco_maca2

soma_preco = preco_maca + preco_morango
soma_quilos = qtd_quilos_maca + qtd_quilos_morango

if (soma_quilos > 8) or (soma_preco > 25):
    soma_preco = soma_preco - (soma_preco * 0.10)
    print(f"O preço total é R${soma_preco:.2f}")
else:
    print(f"O preço total é R${soma_preco:.2f}")
    