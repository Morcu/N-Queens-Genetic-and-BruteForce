import requests
import json
import time
API = 'http://memento.evannai.inf.uc3m.es/age/test?c='
BASE = 64

def main():
    resultado = []
    binary = []
    potencia = pow(2,64)
    i = 0
    t= time.time()
    while(i < 1000):
        binario = get_bin(i, BASE)
        respuesta = requests.get(API + binario)
        resultado.append(float(respuesta.text))
        binary.append(binario)
        if((i % 1000) == 0):
            print('i es = a: ')
            print(i)
            
        i = i + 1
    print(time.time() - t)
    with open('resultado.txt','w') as fp:
        json.dump(resultado, fp)
    with open('binary.txt','w') as fp:
        json.dump(binary, fp)
    
    indice = resultado.index(min(resultado))
    print('-------------')
    print(resultado[indice], binary[indice])
   
def get_bin(x,n):
    return format(x,'b').zfill(n)
if __name__ == '__main__':
    main()