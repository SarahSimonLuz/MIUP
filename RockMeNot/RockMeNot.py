def possivel(a,x,y,c,l):
        count = 0
        if x != 0:
                if y != 0:
                        if a[x-1][y-1]=='#':
                                count+=1
                if y != c:
                        if a[x-1][y+1]=='#':
                                count+=1
                if y == 0 or y == c:
                        count+=1
        if x != l:
                if y != 0:
                        if a[x+1][y-1]=='#':
                                count+=1
                if y != c:
                        
                        if a[x+1][y+1]=='#':
                                count+=1
                if y == 0 or y == c:
                        count+=1
        if x == 0 or x == l:
                
                        count+=1                        
        if count <= 2:
                return True
        return False


def rock(x):
        import filecmp
        
        f = open(x, "r")
        a = f.readlines()
        f.close()

        d,c,l= matriz(a)
        value = str(count(d,c,l))

        file = open("resultado.txt", "w")
        file.write(value)
        file.close()
        if x=='teste1.txt':
                return filecmp.cmp('res1.txt','resultado.txt')
        elif x=='teste2.txt':
                return filecmp.cmp('res2.txt','resultado.txt')
        
        

