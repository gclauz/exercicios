a = float(input("Digite a sua altura em metros: "))
sexo = int(input("Digite 1 para homem e 2 para mulher: "))
homem = (72.7 * a) - 58
mulher = (62.1 * a) - 44.7

if sexo == 1:
    print("Seu peso ideal é", homem)
else:
    if sexo == 2:
        print("Seu peso ideal é", mulher)