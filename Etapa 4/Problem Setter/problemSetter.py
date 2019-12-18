def leitura(nome_ficheiro): #leitura do input
    f = open(nome_ficheiro,"r")
    escolhas = f.read().splitlines()
    return escolhas 

def decrementar(equipas): #decrementa o numero de emails por mandar, e remove da lista
	for i in equipas:
		i[0]-=1
	return equipas
