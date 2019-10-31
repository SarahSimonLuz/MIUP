#Exercicio 4

def dividir_familias (matriz):
	#dividir a lista matriz por familias 
	arr_F0 = []
	arr_F1 = []
	for i in matriz:
		if i[2] == '0':
			arr_F0.append(i)
		else:
			arr_F1.append(i)
	#Teste : print (arr_F0)
	#Teste : print (arr_F1)
	return arr_F0, arr_F1


def matriz():
	# colocar em linhas separadas do input numa lista
	f = open("input.txt", "r")
	a = f.readlines()
	matriz = []

	for i in a:
		matriz.append(i.split())
	matriz.pop(0)
	f.close()
	#Teste : print (matriz)
	return matriz


matriz = matriz()
arr_F0, arr_F1 = dividir_familias(matriz)
arr_F0, arr_F1 = to_int(arr_F0,arr_F1)
m = menor(arr_F0, arr_F1)
print(m)
