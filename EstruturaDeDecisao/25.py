#Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
#a. "Telefonou para a vítima?"
#b. "Esteve no local do crime?"
#c. "Mora perto da vítima?"
#d. "Devia para a vítima?"
#e. "Já trabalhou com a vítima?" 
#O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".

print("Responda as perguntas SOMENTE com sim ou não!")

pergunta1 = input("Telefonou para a vítima? ")
pergunta2 = input("Esteve no local do crime? ")
pergunta3 = input("Mora perto da vítima? ")
pergunta4 = input("Devia para a vítima? ")
pergunta5 = input("Já trabalhou com a vítima? ")

sim = 0

if pergunta1 == "sim":
    sim = sim + 1
    
if pergunta2 == "sim":
    sim = sim + 1
    
if pergunta3 == "sim":
    sim = sim + 1
    
if pergunta4 == "sim":
    sim = sim + 1
    
if pergunta5 == "sim":
    sim = sim + 1

if sim < 2:
    print("Inocente")
elif sim == 2:
    print("Supeita")
elif sim < 5:
    print("Cúmplice")
else:
    print("Assassino")