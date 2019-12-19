def leitura(nome_ficheiro): #leitura do input
    f = open(nome_ficheiro,"r")
    escolhas = f.read().splitlines()
    return escolhas 

def decrementar(equipas): #decrementa o numero de emails por mandar, e remove da lista
	for i in equipas:
		i[0]-=1
	return equipas

def remover_equipas(abertos, equipas): #remover as equipas que estão no abertos
	for i in abertos:
		if i in equipas:
			equipas.remove(i)
	return equipas


def main(nome_ficheiro):
	abertos=[]
	mails_send = 0
	num_dias = 0
	dia = 1

	equipas = leitura(nome_ficheiro)
	num_equipas = int(equipas.pop(0))
	equipas = ordenar(divisao(equipas))

	while(num_equipas>0):
		out = []
		abertos = verificar_abertos(dia,equipas,abertos)
		equipas = remover_equipas(abertos,equipas)
		mails_send = verificar_data(dia, abertos)

		if mails_send==1:
			abertos = decrementar(abertos)
			num_dias+=1	

		for k in abertos:
			if k[0]==0:
				num_equipas-=1
				out.append(k)

		abertos = remover_equipas(out,abertos)
		dia+=1

	return num_dias

