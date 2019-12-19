

#pontos2=[[1,0],[7,0],[5,6],[5,5],[3,3],[4,7],[0,6],[1,0],[7,0],[5,6],[5,5],[3,3],[4,7],[0,6]]
#pontos=[[1,0],[7,0],[5,6],[5,5],[3,3],[4,7],[0,6]]

#size = 7
#size = 4
#pontos=[[0,0],[1,0],[1,1],[0,1]]
#pontos2=[[0,0],[1,0],[1,1],[0,1],[0,0],[1,0],[1,1],[0,1]]


def recebecalcula(pontos,size):
    import numpy as np
    x = np.array(pontos[0])
    y = np.array(pontos[1])
    for i in range(int((size-1)/2)):
        x = np.append(x, pontos[(i*2)+2])
        y = np.append(y, pontos[(i*2)+3])
    return PolyArea(x,y)

def verifica(x):
    if x[0]<0 or x[0]>1 or x[1]<0 or x[1]>1:
        return False
    return True





