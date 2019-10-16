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