#Saul Milu
import numpy as np

def inicilaizarMatriz():
    tam = int(input('Informe a quantidade de estados: '))
    matriz = np.zeros([tam,tam])
    firstRead = True
    for a in range(tam):
        while not (isStochastic(matriz, a, firstRead)):
            firstRead = False 
            for b in range(tam):
                matriz[a][b] = digitValid(a, b)
        firstRead = True
    print(matriz)

def digitValid(ind_1, ind_2):
    while True:
        try:
            n = float(input('A probabilidade de %i para %i: ' %(ind_1, ind_2)))
            if n < 0 or n > 1:
                print('digite um valor de zero a 1')
            else :
                return n
        except NameError:
            print('Digite um numero')

def isStochastic(mat, linha, flagFirst):
    result = mat.sum(axis=1)
    if flagFirst: return False
    if result[linha] > 1 or result[linha] < 1 :
        print(' --- Atencao, a soma das probabilidades de uma linha devem ser iguais a 1! --- ')
        return False
    return True


if __name__ == "__main__":
    inicilaizarMatriz()
    '''
    x = int(-1)
    y = int(2.8)
    z = int("3")
    print(x)
    print(y)
    print(z)
    '''