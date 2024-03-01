#Faça um Programa que verifique se uma letra digitada é vogal ou consoante

letra = input("Digite uma letra: ")

if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u" or letra == "A" or letra == "E" or letra == "I" or letra == "O" or letra == "U":
    print("A letra é uma vogal")
    
elif letra == "1" or letra == "2" or letra == "3" or letra == "4" or letra == "5" or letra == "6" or letra == "7" or letra == "8" or letra == "9" or letra == "0":
    print("Inválido")
    
else:
    print("A letra é uma consoante")