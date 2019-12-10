import random as rd

def compareLists(lista1, lista2):
    ''' idenbtifica se duas listas são iguais. Caso não retorna os indices
        retorno: bool, lista_ind
    ''' 
    if len(lista1) != len(lista2):
        return False, None
    if lista1 == lista2:
        return True,None
    lista_ind = []
    for i in range(len(lista1)):
        if lista1[i] != lista2[i]:
            lista_ind.append(i)
    return False,lista_ind

def compareMatriz(mat1, mat2):
    ''' indentifica se duas matrizes são iguais. Caso não rerotnar os indices nas listas ind_x e ind_y
    '''
    if mat1 == mat2:
        return True,None,None
    ind_x = []
    ind_y = []
    for x in range(len(mat1)):
        for y in range(len(mat1[0])):
            if mat1[x][y] != mat2[x][y]:
                ind_x.append(x)
                ind_y.append(y)
    return False, ind_x, ind_y

def convertListinGameBoard(lista):
    ''' para formato do jogo trilha
    '''
    nova = []
    x_axis = 8
    y_axis = 3
    linha, qd = 0,0
    for _i in range(x_axis):
        nova.append(lista([],[],[]))
    for i in range(9):
        if i != 0 and i % 3 == 0:
            linha += 1
            qd = 0
        nova[linha][qd] = lista[i]
        qd += 1
    j = 0
    for i in range(9,12):
        nova[7][j]= linha[i]
        j+=1
    j = 2
    for i in range(12,15):
        nova[3][j] = linha[i]
        j-=1
    linha, qd = 6, 0
    for i in range(15,24):
        if i != 15 and i % 3 == 0:
            linha -=1
            qd = 0
        nova[linha][qd] = linha[i]
        qd+=1
    return nova
    # x_axis = 8
    # y_axis = 3
    # cont = 0
    # for _i in range(x_axis):
    #     nova.append(lista[cont:cont+y_axis])
    #     cont += y_axis
    # return nova

def crateListRandomic(tam, minValue, maxValue):
    lista = []
    for _i in range(tam):
        lista.append(rd.randint(minValue, maxValue))
    return lista

def rankList(lista, pos_rank):
    '''
    A partir de um rank de posicao Retorna o objeto e o indice na lista
    '''
    order_list = lista.copy()
    order_list.sort(reverse=True)
    ob = order_list[pos_rank-1]
    ind = lista.index(ob)
    return ob, ind

def convertGameBoardInList(game):
    nova = []
    x_axis = 8
    y_axis = 3
    for linha in range(3):
        for qd in range(y_axis):
            nova.append(game[linha][qd])
    nova.append(game[7][0])
    nova.append(game[7][1])
    nova.append(game[7][2])
    nova.append(game[3][2])
    nova.append(game[3][1])
    nova.append(game[3][0])
    for linha in range(6,3,-1):
        for qd in range(3):
            nova.append(game[linha][qd])
    return nova

    # for _,linhas in enumerate(game):
    #     for _,value in enumerate(linhas):
    #         nova.append(value)
    # return nova

if __name__ == "__main__":
    print(convertListinGameBoard([0,1,0, 2,0,1, 0,2,1, 1,2,2, 0,1,0, 2,1,1,2,2,0,1,0,2]))