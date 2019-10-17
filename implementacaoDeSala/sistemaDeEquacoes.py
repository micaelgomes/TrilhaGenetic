#Saul Milu
import numpy as np

def matrizTransicaoInput():
    c = np.zeros([3,3])
    print("inicializando a matriz de transicao")
    for a in range(3):
        for b in range(3):
            c[a][b] = input("Digite um valor para elemento linha %i e coluna %i: " %(a,b))
        
    return c

def sistema(c):
    P = np.array([
        [ c[0][0], 1 + c[1][0], 1 + c[2][0] ],
        [ 1 + c[0][1], c[1][1], 1 + c[2][1] ],
        [ 1 + c[0][2], 1 + c[1][2], c[2][2] ]
                ])
    R = np.array([ [1],[1],[1] ])
    #P x A = R entao A = P inversa x R
    P_inv = np.linalg.inv(P)
    # Logo X (matriz de coeficiente) 
    X = np.dot(P_inv, R)
    print("Probabilidade a longo Prazo -->")
    print("Probabilidade do estado 0: %f , do estado 1: %f, do estado 2: %f " %(X[0], X[1], X[2]))


if __name__ == "__main__":
    mat = matrizTransicaoInput()
    sistema(mat)

