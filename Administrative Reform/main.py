#Exercicio 4


matriz, line1, line2 = matriz()
matriz, line1, line2 = to_int(matriz, line1, line2)
C = line1[0]
X = line2[0]
Y = line2[1]
n1, n2, n3 = estradas(matriz, X, Y, C)
print(n1, n2, n3)
