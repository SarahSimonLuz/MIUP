
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
        
        

