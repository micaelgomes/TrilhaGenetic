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
    return matriz

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

def stateAcessible(matriz, mat_result):
    num_states = matriz.shape[0]
    for a in range(num_states):
        for b in range(num_states):
            if a != b:
                text = '{}'.format(a)
                isAcessible(a, a, b, text, matriz, mat_result, num_states)


def isAcessible(start, actual, goal, text, matriz, mat_result, count):
    if actual == goal: 
        print('(%i -> %i) atraves de: (%s)' %(start, actual, text))
        mat_result[start][actual] = 'S'
        return
    if count == 0 : return

    count -= 1
    for b in range(matriz.shape[0]):
        if actual != b and matriz[actual][b] > 0 and matriz[b][goal] > 0 : 
            text = text + ', ' + str(b)
            isAcessible(start, b, goal, text, matriz, mat_result, count)

def isComunicated(mat):
    for a in range(len(mat[0])):
        for b in range(len(mat[0])):
            if mat[a][b] == 'S' and mat[b][a] == 'S':
                print('(%i <-> %i)'%(a,b))

def initMatResult(matriz):
    result = []
    for a in range(matriz.shape[0]):
        result.append([])
        for b in range(matriz.shape[0]):
            result[a].append('-')
    return result

if __name__ == "__main__":
    mat = inicilaizarMatriz()
    resultado = initMatResult(mat)
    #multiplicando a matriz 5 vezes
    for p in range(5):
        mat = np.dot(mat,mat)
    print('matriz final')
    print(mat)
    print('         1) Estados Acessiveis:    ')
    stateAcessible(mat, resultado)
    print('         2) Estados Comunicantes:   ')
    isComunicated(resultado)
    