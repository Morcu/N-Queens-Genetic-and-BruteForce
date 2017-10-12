import copy

n = 10
global Matrix
q = 9

def main():
    #Genera la matriz de N x N
    global Matrix 
    Matrix= [[0 for x in range(n)] for y in range(n)] 
    #Matriz que contendra todos los resultados
    global Result
    Result = []

    recursive_solver(Matrix, 0)
    print('FIN')
    print(len(Result))
    
#Se comprueba si puede ponerse o no la reina
def setQueen(x, y, Matrix):
    
    #horizontal
    for i in range(len(Matrix[x])):
        if(Matrix[x][i] == 1):
            return False
    #vertical
    for j in range(len(Matrix[x])):
        if(Matrix[j][y] == 1):
            return False

    #Diagonal principal       
    for k in range(len(Matrix[x])):
        if (x+k < n and y+k < n):
            if(Matrix[x+k][y+k] == 1):
                return False
        if (x-k > -1 and y-k > -1):
            if(Matrix[x-k][y-k] == 1):
                return False
   
    #Diagonal Inversa        
    for l in range(len(Matrix[x])):
        
        if (x+l < n and y-l >= 0):
            if(Matrix[x+l][y-l] == 1):
                return False
        if (x-l > -1 and y+l < n):
            if(Matrix[x-l][y+l] == 1):
                return False
    return True

def recursive_solver(matrix, col):
    
    n = len(matrix[0])

    if (col >= n):
        return
    for x in range(n):
        if setQueen(x, col, matrix):
            matrix[x][col] = 1
            if col == n - 1:
                solucion = saved_board = copy.deepcopy(matrix)
                Result.append(solucion)
                matrix[x][col] = 0
                return
            recursive_solver(matrix, col + 1)
            
            #Si hay que aplicar backtracking, se puede aplicar poniendo esa reina a 0 y siguiendo con el algoritmo
            matrix[x][col] = 0

if __name__ == '__main__':
    main()