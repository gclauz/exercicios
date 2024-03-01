mb = float(input("Tamanho do arquivo (em Mb): "))
v = float(input("Velocidade da internet (em Mbps): "))
tempo = mb / (v / 8) / 60

print(f"O tempo aproximado de download do arquivo é de {tempo} minutos")
