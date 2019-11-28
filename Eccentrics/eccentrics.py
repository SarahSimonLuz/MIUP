import sys
import string

def print_camadas(max_linhas, camadas):
	i = 0
	print("Camadas:")
	while i<max_linhas:
		j = 0
		for j in range(max_linhas):
			print(camadas[i][j]),
			j = j+1

		i = i+1
		print("\n")


def mover_bolas(camadas, max_linhas, n_camadas, l, c, primeiro):
	if l >= max_linhas-n_camadas or l == -1:
		return

	l_procura = l+1+primeiro
	c_procura = c
	l_aux = -1
	c_aux = -1
	max_peso = -1

	if camadas[l_procura][c_procura] != -1 and camadas[l_procura][c_procura] > max_peso:
		max_peso = camadas[l_procura][c_procura]
		l_aux = l_procura
		c_aux = c_procura

	if camadas[l_procura+1][c_procura] != -1 and camadas[l_procura+1][c_procura] > max_peso:
		max_peso = camadas[l_procura+1][c_procura]
		l_aux = l_procura+1
		c_aux = c_procura

	if camadas[l_procura+1][c_procura+1] != -1 and camadas[l_procura+1][c_procura+1] > max_peso:
		max_peso = camadas[l_procura+1][c_procura+1]
		l_aux = l_procura+1
		c_aux = c_procura+1

	if max_peso == -1:
		return

	camadas[l][c] = max_peso
	camadas[l_aux][c_aux] = -1
	
	#print_camadas(max_linhas, camadas)

	mover_bolas(camadas, max_linhas, n_camadas, l_aux, c_aux, primeiro+1)

n = 0
n_bolas_out = 0
n_bolas_in = 0
max_peso = 0

n_camadas = input()
max_linhas = (n_camadas *(n_camadas + 1))/2

i = 1
linha = 0

camadas = [[-1]*max_linhas for _ in range(max_linhas)]

while i<=n_camadas:
	j = 1

	while j<=i:
		k = 1

		while k<=j:
			n = raw_input()

			if len(str(n)) > 1:
				n = n.split(" ")
				tamanho = len(n)
				max_n = max(n)
				max_peso = max(max_peso, max_n)

				aux = 0
				while aux<tamanho:
					camadas[linha][aux] = int(n[aux])
					aux = aux + 1

				n_bolas_in = n_bolas_in + tamanho
				k = k +tamanho

			else:
				max_peso = max(max_peso, n)
				n_bolas_in = n_bolas_in + 1
				k = k +1
				camadas[linha][0] = int(n)

			linha = linha + 1
		j = j + 1
	i = i +1


while n_bolas_out != n_bolas_in:
	print(camadas[0][0])
	mover_bolas(camadas, max_linhas, n_camadas, 0, 0, 0)
	n_bolas_out = n_bolas_out+1
