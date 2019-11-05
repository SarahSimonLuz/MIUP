#Exercicio 4

def matriz():
	# colocar em linhas separadas do input numa lista
	f = open("input2.txt", "r")
	a = f.readlines()
	matriz = []

	for i in a:
		matriz.append(i.split())
	line1 = matriz.pop(0)
	line2 = matriz.pop(len(matriz)-1)
	f.close()

	#Teste: print (matriz, line1, line2)
	return matriz, line1, line2 

def to_int(matriz, line1, line2):
	#Passar as strings da lista em ints
	for i in matriz:
		i[1] = int(i[1]) 
		i[2] = int(i[2]) 
		i[0] = int(i[0]) 

	line1[0] = int(line1[0])
	line1[1] = int(line1[1])
	line2[0] = int(line2[0])
	line2[1] = int(line2[1])

	#Teste : print(matriz, line1, line2) 
	return matriz, line1, line2


matriz, line1, line2 = matriz()
matriz, line1, line2 = to_int(matriz, line1, line2)
C = line1[0]
X = line2[0]
Y = line2[1]
n1, n2, n3 = estradas(matriz, X, Y, C)
print(n1, n2, n3)
