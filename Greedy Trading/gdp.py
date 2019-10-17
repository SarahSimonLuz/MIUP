import statistics
sequencia_atual = []
sequencia_maior = []
index_maior = 0
count_u = 0
out=[]
escolhas = []

def mediana (sequencia_maior):
        #calcula a mediana da sequencia 
        if len(sequencia_maior)%2!= 0:
                return statistics.median(sequencia_maior)
        else: 
                sequencia_maior.sort()
                tamanho = len(sequencia_maior)
                return sequencia_maior[tamanho//2]

def output(sequencia_maior, index_maior):
    mediana_max = 0
    mediana_max = mediana(sequencia_maior)
    out.append([index_maior,count_u-1,mediana_max])

def soma(sequencia_maior, sequencia_atual):
        soma_maior = 0
        soma_atual = 0
        for valor in sequencia_maior:
                soma_maior=soma_maior+valor
        for valor in sequencia_atual:
                soma_atual=soma_atual+valor
        if soma_atual>soma_maior:
                return 0
        return 1

def subsequencia(sequencia_maior, sequencia_atual):
    soma_max = 0
    soma_max = soma(sequencia_maior,sequencia_atual)
    if soma_max==1:
        for i in sequencia_atual:
            sequencia_maior.append(i)
        output(sequencia_maior, count_u - len(sequencia_maior))
        return sequencia_maior
    else:
        sequencia_maior = sequencia_atual
        index_maior = count_u - len(sequencia_maior)
        output(sequencia_maior,index_maior )
        return sequencia_maior
    

escolha = input()
escolhas = escolha.split(' ')
while escolhas[0]!= 'x':
        if escolhas[0]=='u':
                sequencia_atual.append(int(escolhas[1]))
                count_u+=1
        else:
            sequencia_maior = subsequencia(sequencia_maior,sequencia_atual)
            sequencia_atual = []
        escolha = input()
        escolhas = escolha.split(' ')

for i in out:
    print(i[0],i[1],i[2])

