def mediana (sequencia_maior):
        #calcula a mediana da sequencia 
        if len(sequencia_maior)%2!= 0:
                return statistics.median(sequencia_maior)
        else: 
                sequencia_maior.sort()
                tamanho = len(sequencia_maior)
                return sequencia_maior[tamanho//2]


