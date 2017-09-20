n = 4
global Matrix
q = 9

def main():
    print "Hello, world!"
    queens = n -1
    startX = 0
    startY = 0
    Matrix = [[0 for x in range(n)] for y in range(n)] 
    Result = []

    while(queens != 0):
        print(queens)
        posx, posy = findPlace(0, 0, 0, Matrix)
        setQueen(posx, posy, Matrix)
        for i in range(len(Matrix[x])):
            print(Matrix[i])
        print('----------')
        queens = queens - 1
        for check in range(len(Matrix[x])):
            if (len(set(Matrix[check])) <= 1 and Matrix[check][0] == 1):
                print('nope')
                if(startY == n-1):
                    startX = startX + 1
                    startY = 0
                else:
                    startY = startY + 1
                Matrix = [[0 for x in range(n)] for y in range(n)]
                posx, posy = findPlace(1,startX ,startY, Matrix)
                setQueen(posx, posy, Matrix)
                for i in range(len(Matrix[x])):
                    print(Matrix[i])
                print('----------')
                queens = n -1
    

def setQueen(x, y, Matrix):
    print(x, y)
    Matrix[x][y] = q
    #horizontal
    for i in range(len(Matrix[x])):
        if(Matrix[x][i] == 0):
            Matrix[x][i] = 1
    #vertical
    for j in range(len(Matrix[x])):
        if(Matrix[j][y] == 0):
            Matrix[j][y] = 1

    #Revisar diagonales desde la reina hacia arriba
    #Diagonal principal       
    for k in range(len(Matrix[x])):
        if (x+k < n and y+k < n):
            if(Matrix[x+k][y+k] == 0):
                Matrix[x+k][y+k] = 1
        if (x-k > -1 and y-k > -1):
            if(Matrix[x-k][y-k] == 0):
                Matrix[x-k][y-k] = 1
   
    #Diagonal Inversa        
    for l in range(len(Matrix[x])):
        
        if (x+l < n and y-l >= 0):
            if(Matrix[x+l][y-l] == 0):
                Matrix[x+l][y-l] = 1
        if (x-l > -1 and y+l < n):
            if(Matrix[x-l][y+l] == 0):
                Matrix[x-l][y+l] = 1
    
def findPlace(start, startX, startY, Matrix):
    if(start == 0):
        for x in range(n):
            for y in range(n):
                if(Matrix[x][y] == 0):
                    return x, y
    else:
        return startX, startY

if __name__ == '__main__':
    main()