from random import randint
import random
import numpy as np
from copy import deepcopy
import sys

evaluaciones = 0
n = 10
tamanoPoblacion = 100
tasaMutacion = 0.1
tamTorneo = 3
def main():
    
    global n
    global tamanoPoblacion
    global tasaMutacion
    global tamTorneo
    if(len(sys.argv) >= 5):
        if(sys.argv[1].isdigit()):
            n = int(sys.argv[1])
        if(sys.argv[2].isdigit()):
            tamanoPoblacion = int(sys.argv[2])
        if(sys.argv[3].isdigit()):
            tamTorneo = int(sys.argv[3])
        
        tasaMutacion = float(sys.argv[4])
    print('[N-Queens GA GeneticoModificado]')
    print('N:' + str(n) + ' Poblacion:' + str(tamanoPoblacion) + ' Torneo:' + str(tamTorneo) + ' Mutacion:' + str(tasaMutacion))
    poblacion = []
    cromosoma = np.arange(n)

    puntuacionIndividuo = []
    start = 0
    end = 0
    for i in range(tamanoPoblacion):
        cromosoma = range(n)
        random.shuffle(cromosoma)
        poblacion.append(cromosoma)
        
    contador = 0

    
    while(True):
    #for i in range(3):
        #hay que hacerlo para cada elemento en la poblacion
        for ind in poblacion:
            matriz = convertir(ind, n)
            queens = checkQueens(matriz)
            puntos = checkAttack(matriz, queens)
            puntuacionIndividuo.append(puntos)
            if(puntos == 0):
                suma = 0
                
                for i in matriz:
                    suma = suma + sum(i)
                    
                if(suma == n):
                    global evaluaciones
                    
                    print(ind)
                    print(evaluaciones)
                    return
        #print(media(puntuacionIndividuo))
        nuevaPoblacion = torneo(poblacion, puntuacionIndividuo, tamTorneo, tamanoPoblacion)
        #print(len(nuevaPoblacion))
        
        poblacionFinal = cruce(nuevaPoblacion, (n))
        
        poblacionMutada = mutacion(poblacionFinal, tasaMutacion, (n))
        
        contador = contador + 1
        puntuacionIndividuo = []
        #print('---------------')
        poblacion = deepcopy(poblacionMutada)


    #print(poblacionMutada)

def diff(first, second):
        second = set(second)
        return [item for item in first if item not in second]

def media(puntos):
    sum=0.0
    for i in range(0,len(puntos)):
        sum=sum+puntos[i]
 
    return sum/len(puntos)

#Convierte el genotipo en fenotipo
def convertir(queen, n):
    l = [0] * (n*n)
    matrx = ([l[i:i + n] for i in range(0, len(l), n)])
    for i in range(len(queen)):
        matrx[i][queen[i]] = 1
    '''print(queen)
    print(matrx)
    print('-------')
    '''
    return matrx

#devuelve la posicion de las reinas dado un tablero
def checkQueens(matrix):
    queens = []
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if(matrix[i][j] == 1):
                queens.append([i,j])
    return queens

#Calculo del fitnes
#para cada reina comprobar si ataca a alguna otra reina
def checkAttack(Matrix, queens):
    global evaluaciones
    evaluaciones = evaluaciones + 1
    attack = 0
    for queen in queens:
        #horizontal
        x = queen[0]
        y = queen[1] 
        
        #for i in range(len(Matrix[x])):
        #    print(Matrix[i])
        
        #hotizontal
        for i in range(len(Matrix[x])):
            if(Matrix[x][i] == 1 and i != y ):
                attack = attack + 1
        
        #vertical
        for j in range(len(Matrix[0])):
            if(Matrix[j][y] == 1 and j != x):
                attack = attack + 1
        
        #Diagonal principal       
        for k in range(len(Matrix[x])):
            if (x+k < n and y+k < n):
                if(Matrix[x+k][y+k] == 1 and x+k != x and y+k != y):
                    attack = attack + 1
            
            if (x-k > -1 and y-k > -1):
                if(Matrix[x-k][y-k] == 1 and x-k != x and y-k != y):
                    attack = attack + 1
        
        #Diagonal Inversa        
        for l in range(len(Matrix[x])):
            
            if (x+l < n and y-l >= 0 and x+l != x and y-l != y):
                if(Matrix[x+l][y-l] == 1):
                    attack = attack + 1
            
            if (x-l > -1 and y+l < n):
                if(Matrix[x-l][y+l] == 1 and x-l != x and y+l != y):
                    attack = attack + 1


    return attack



#elegir aleatoriamente k individuos y quedarte con el que menor puntuacion tenga hasta llenar una 
#poblacion nueva del mismo tamano de la de origen
def torneo(poblacion, puntos, k, tamanoPoblacion):
    
    poblacionFinal = []
    while(len(poblacionFinal) < tamanoPoblacion):
        arena = []
        valores = []
        for i in range(k):
            numero = randint(0, (len(poblacion)-1))
            arena.append({puntos[numero]:numero})
            valores.append(puntos[numero])
        pos = sorted(valores)
        orden = sorted(arena)
        
        individuo =  orden[0][pos[0]]
        poblacionFinal.append(poblacion[individuo])

    return poblacionFinal

def cruce(poblacion, n):
    poblacionCruzada = []
    for i,k in zip(poblacion[0::2], poblacion[1::2]):
        corte = randint(1, n-1)
        p1 = i[:corte]
        p2 = i[corte:]
        p3 = k[:corte]
        p4 = k[corte:]
       
        h1 = p1 + p4
        h2 = p3 + p2
        poblacionCruzada.append(h1)
        poblacionCruzada.append(h2)
    return poblacionCruzada

def mutacion(poblacion, tasaMutacion, n):
    poblacionMutada = []
    for item in poblacion:
        rand = random.uniform(0, 1)
        if(rand <= tasaMutacion):
            #print('_MUTA_')
            
            pos = randint(0, n-1)
            while(True):   
                num = randint(0, n-1)
                if(item[pos] != num):
                    break
            item[pos] = num
            poblacionMutada.append(item)
        else:
            poblacionMutada.append(item)
    return poblacionMutada

def aleatorios(start, end):
    r1 = randint(start, end)
    r2 = randint(start, end)
    if (r1 == r2):
        r1, r2 = aleatorios(start, end)
    return r1, r2

if __name__ == '__main__':
    main()