from random import randint
import random
import numpy as np
from copy import deepcopy
import requests
API = 'http://memento.evannai.inf.uc3m.es/age/test?c='
n = 8
ciclos = 200
evaluaciones = 0
def main():
    poblacion = []
    cromosoma = []
    tamanoPoblacion = 100
    tasaMutacion = 0.2
    puntuacionIndividuo = []
    for i in range(tamanoPoblacion):
        for i in range(0, n*n):
            cromosoma.append(randint(0, 1))
        poblacion.append(cromosoma)
        cromosoma = []
    contador = 0
    minimo = []
    minimoCadena = []
    global ciclos
    while(contador < ciclos):
    
    #for i in range(3):
        #hay que hacerlo para cada elemento en la poblacion
        for ind in poblacion:
            
            puntos = obtenerPuntuacion(ind)
            puntuacionIndividuo.append(puntos)

        minimo.append(min(puntuacionIndividuo))    
        minimoCadena.append(poblacion[puntuacionIndividuo.index(min(puntuacionIndividuo))])
        #print(media(puntuacionIndividuo))
        nuevaPoblacion = torneo(poblacion, puntuacionIndividuo, 3 , tamanoPoblacion)
        #print(len(nuevaPoblacion))
        
        poblacionFinal = cruce(nuevaPoblacion, (n*n))
        poblacionMutada = mutacion(poblacionFinal, tasaMutacion, (n*n))
        print('contador')
        print(contador)
        global evaluaciones
        print('evaluaciones')
        print(evaluaciones)
        print('min')
        print(min(minimo))
        valor = minimoCadena[minimo.index(min(minimo))]
        print(''.join(str(x) for x in valor))
        contador = contador + 1
        puntuacionIndividuo = []
        print('---------------')
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


def obtenerPuntuacion(individuo):
    global evaluaciones
    evaluaciones = evaluaciones + 1
    global API
    return float(requests.get(API + ''.join(str(x) for x in individuo)).text)



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
        corte = randint(0, n)
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
            item[pos] = 1 - item[pos]
            poblacionMutada.append(item)
        else:
            poblacionMutada.append(item)
    return poblacionMutada
if __name__ == '__main__':
    main()