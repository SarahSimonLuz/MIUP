import sys
import string

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
