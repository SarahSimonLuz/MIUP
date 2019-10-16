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
