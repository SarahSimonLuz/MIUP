

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


def calcula_areaponto(pontos,pontos2,size):
    import numpy as np
    from shapely.geometry import Point, Polygon
    
    countp = 0
    poly = Polygon(pontos)
    area = 0
    areaponto = []
    for i in range(size):
        armazena = np.array(pontos2[i])
        pcertos = 0
    
        for x in range(size-1):
            inside = 0
            countp=0

            for y in range(size):
                if verifica(resolve_matriz(pontos2[i],pontos2[i+x+1],pontos2[y],pontos2[y+1])) == True:
                    countp+=1
            if countp <= 4:
                p1x = (pontos2[i][0] + pontos2[i+x+1][0])/2
                p1y = (pontos2[i][1] + pontos2[i+x+1][1])/2
                p1 = Point(p1x,p1y)
            
                if p1.within(poly) or p1.intersects(poly):
                    armazena = np.append(armazena, pontos2[i+x+1])
                
        if recebecalcula(armazena,(len(armazena)-1)) == area:
            areaponto.append(i)
        if recebecalcula(armazena,(len(armazena)-1)) > area:
            area = recebecalcula(armazena,(len(armazena)-1))
            areaponto = [i]
    return areaponto



def arrayduplo(pontos):
    pontos2 = []
    for i in range(2):
        for i in range(len(pontos)):
            pontos2.append(pontos[i])
    return pontos2

