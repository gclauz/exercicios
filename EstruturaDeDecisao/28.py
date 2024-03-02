#O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. 
# Confira:
#                      Até 5 Kg           Acima de 5 Kg
#File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
#Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
#Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg
#Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção, porém não há limites para a quantidade de carne por cliente. Se compra for feita no cartão Tabajara o cliente receberá ainda um desconto de 5% sobre o total da compra. 
# Escreva um programa que peça o tipo e a quantidade de carne comprada pelo usuário e gere um cupom fiscal, contendo as informações da compra: tipo e quantidade de carne, preço total, tipo de pagamento, valor do desconto e valor a pagar.

menu = '''

            [F] = Filé Duplo
            [A] = Alcatra
            [P] = Picanha

'''
print(menu)

opcao = input("Escolha uma opção: ")
quantidade = float(input("Informe a quantidade de carne em Kg: "))

precoFile1 = 4.9 * quantidade
precoFile2 = 5.8 * quantidade

precoAlcatra1 = 5.9 * quantidade
precoAlcatra2 = 6.8 * quantidade

precoPicanha1 = 6.9 * quantidade
precoPicanha2 = 7.8 * quantidade

precoFile = 0
precoAlcatra = 0
precoPicanha = 0

if opcao == "F" or opcao == "f":
    tipo = "Filé Duplo"
    
    if quantidade <= 5:
        precoFile = precoFile1 
    else:
        precoFile = precoFile2

elif opcao == "A" or opcao == "a":
    tipo = "Alcatra"
    
    if quantidade <= 5:
        precoAlcatra = precoAlcatra1   
    else:
        precoAlcatra = precoAlcatra2
        
elif opcao == "P" or opcao == "p":
    tipo = "Picanha"
    
    if quantidade <= 5:
        precoPicanha = precoPicanha1  
    else:
        precoPicanha = precoPicanha2

preco_total = precoFile + precoAlcatra + precoPicanha
            
formas = '''
            Formas de pagamento
            
            [t] = Cartão Tabajara    
            [d] = Débito
            [c] = Crédito
            [m] = Dinheiro
            [p] = pix
                
    '''
print(formas)
forma_pagamento = input("Escolha uma opção: ")

if forma_pagamento == "d" or forma_pagamento == "D":
        tipo_de_pagamento = "Débito"
        valor_desconto = 0
        valor_a_pagar = preco_total
    
elif forma_pagamento == "c" or forma_pagamento == "C":
        tipo_de_pagamento = "Crédito"
        valor_desconto = 0
        valor_a_pagar = preco_total
    
elif forma_pagamento == "m" or forma_pagamento == "M":
        tipo_de_pagamento = "Dinheiro"
        valor_desconto = 0
        valor_a_pagar = preco_total
        
elif forma_pagamento == "p" or forma_pagamento == "P":
        tipo_de_pagamento = "Pix"
        valor_desconto = 0
        valor_a_pagar = preco_total
    
elif forma_pagamento == "t" or  forma_pagamento == "T":
    tipo_de_pagamento = "Cartão Tabajara" 
    valor_desconto = preco_total * 0.05
    valor_a_pagar = preco_total - valor_desconto

print(f"Tipo: {tipo}")
print(f"Quantidade: {int(quantidade)} Kg")
print(f"Preço total: R${preco_total:.2f}")
print(f"Tipo de pagamento: {tipo_de_pagamento}")
print(f"Valor do desconto: R${valor_desconto:.2f}")
print(f"Valor a pagar: R${valor_a_pagar:.2f}")