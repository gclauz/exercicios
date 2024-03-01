#Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
#a. par ou ímpar;
#b. positivo ou negativo;
#c. inteiro ou decimal.


menu = '''
            MENU:
            
            [a] = Par ou Ímpar
            [b] = Positivo ou Negativo
            [c] = Inteiro ou Decimal
            [q] = Sair
            
'''

while True:
    numero1 = int(input("Digite um número: "))
    numero2 = int(input("Digite um número: "))
    opcao = input(f"{menu} Informe uma opção: ")
    
    if opcao == "a":
        
        if numero1 % 2 == 0:
            print("Número par")
        else:
            print("Número ímpar")
            
        if numero2 % 2 == 0:
            print("Número par")
        else:
            print("Número ímpar")
            
    elif opcao == "b":
        
        if numero1 > 0:
            print("Positivo")
        else:
            print("Negativo")
            
        if numero2 > 0:
            print("Positivo")
        else:
            print("Negativo")    
            
    elif opcao == "c":
        
        if numero1 == round(numero1):
            print("Inteiro")
        else:
            print("Decimal") 
        
        if numero2 == round(numero2):
            print("Inteiro")
        else:
            print("Decimal")    
            
    elif opcao == "q":
        break                
    