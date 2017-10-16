from random import randint
import random
import numpy as np
from copy import deepcopy

n = 10
def main():
    poblacion = []
    cromosoma = [0] * (n*n)
    tamanoPoblacion = 1000
    tasaMutacion = 0.4
    puntuacionIndividuo = []
    start = 0
    end = 0
    for i in range(tamanoPoblacion):
        for j in range(n):
            start = j * n
            end = ((j + 1) * n) - 1 
            pos = randint(start, end)
            cromosoma[pos] = 1        
        poblacion.append(cromosoma)
        cromosoma = [0] * (n*n)
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
                conv = convertir(ind,n)
                for i in conv:
                    suma = suma + sum(i)
                    
                if(suma == n):
                    print('_stop_')
                    
                    print('contador:  ' + str(contador))
                    for i in conv:
                        print(i)
                    return
        #print(media(puntuacionIndividuo))
        nuevaPoblacion = torneo(poblacion, puntuacionIndividuo, 3 , tamanoPoblacion)
        #print(len(nuevaPoblacion))
        
        poblacionFinal = cruce(nuevaPoblacion, (n))
        
        poblacionMutada = mutacion(poblacionFinal, tasaMutacion, (n))
        print('contador:  ' + str(contador))
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
def convertir(l, n):
    return([l[i:i + n] for i in range(0, len(l), n)])

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
        posCorte = randint(1, n-1)
        corte = (posCorte * n)  
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
            '''
            elegir subconjunto aleatorio
            elegir 2 valores aleatorios en el rango del subconjunto
            intercambiar esos valores 
            '''
            pos = randint(1, n-1)
            topSubconjunto = (pos * n)
            endSubconjunto = (topSubconjunto + n) - 1
            pos1, pos2 = aleatorios(topSubconjunto, endSubconjunto)
            aux = item[pos1]
            item[pos1] = item[pos2]
            item[pos2] = aux
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