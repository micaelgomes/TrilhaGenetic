#Saul Milu
import numpy as np

def matrizTransicaoInput():
    c = np.zeros([3,3])
    print("inicializando a matriz de transicao")
    for a in range(3):
        for b in range(3):
            c[a][b] = input("Digite um valor para elemento linha %i e coluna %i: " %(a,b))
        
    return c

def matrizChapsonKomogorov():
    step = input("passos: ")
    mat_T = matrizTransicaoInput()
    print("mat_T")
    print(mat_T)
    result = mat_T
    for b in range(step):
        result = np.dot(result,mat_T)
        print(result)
    
    return result

def chapmanKamogorov():
    step = input("passos: ")
    mat = matrizTransicaoInput()
    print(" estado inicial 1 e final 2 com %i passos" %(step))
    res = recursaoChapman(mat, 1, 2, step)
    print("chapman result :")
    print(res)

#mt - matriz
#I- estado Inicial
#F - estado  Final
def recursaoChapman(mt, I, F, passo):
    print("passo %i" %(passo))
    if passo > 2 :
        n1 = mt[I][0]*recursaoChapman(mt,0,F,passo-1)
        n2 = mt[I][1]*recursaoChapman(mt,1,F,passo-1)
        n3 = mt[I][2]*recursaoChapman(mt,2,F,passo-1)
        print("n1 : %f  n2: %f  n3:%f " %(n1,n2,n3))
        return  n1 + n2 + n3 
    
    #quando passo 2
    return mt[I][0]*mt[0][F] + mt[I][1]*mt[1][F] + mt[I][2]*mt[2][F]

if __name__ == "__main__":
    #print(matrizChapsonKomogorov())
    chapmanKamogorov()


    

