peso = float(input("Digite quantos quilos há de peixes: "))
pesoExcedente = peso - 50
multa = pesoExcedente * 4

if peso > 50:
    print("A pesagem indicou um excedente de peso de", pesoExcedente, "Kg")
    print("A multa por passar do limite de peso é de R$", multa)
else:
    if peso <= 50:
        print("A pesagem não indicou excesso de peso.")