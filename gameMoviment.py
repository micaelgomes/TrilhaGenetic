firstRow = 0
lastRow = 7
# 3 dimensoes correspondem e os valores internos correspondem a tuplas dos indices de posicao
# as duas primeiras dimensoes representam o indice da posicao da qual deseja-se saber as adjacencias
table_of_adj = [
    [ [(1,0),(7,0)], [(1,1),(7,1)], [(1,2),(7,2)] ], # linha 0
    [ [(0,0),(2,0),(1,1)], [(0,1),(2,1),(1,0),(1,2)], [(0,2),(2,2),(1,1)] ], # linha 1
    [ [(1,0),(3,0)], [(1,1),(3,1)], [(1,2),(3,2)] ], #linha 2
    [ [(2,0),(4,0),(3,1)], [(2,1),(4,1),(3,0),(3,2)], [(2,2),(4,2),(3,1)] ], #linha 3
    [ [(3,0),(5,0)], [(3,1),(5,1)], [(3,2),(5,2)] ], #linha 4
    [ [(4,0),(6,0),(5,1)], [(4,1),(6,1),(5,0),(5,2)], [(4,2),(6,2),(5,1)] ], #linha 5
    [ [(5,0),(7,0)], [(5,1),(7,1)], [(5,2),(7,2)] ], #linha 6
    [ [(6,0),(0,0),(7,1)], [(6,1),(0,1),(7,0),(7,2)], [(6,2),(0,2),(7,1)] ], #linha 7
]

def isAdjacent(pos, other_pos):
    aux = table_of_adj[pos[0]][pos[1]]
    # print('aux ', aux, 'comparar : ' ,(other_pos in aux))
    return (other_pos in aux)

def isMoveValidStage1(estado_atual,cromossomo, tupla, geracao):
    linha = tupla[0]
    qd = tupla[1]
    #há apenas uma posicao para ser avaliada
    posicao = (linha[0],qd[0])
    if estado_atual[posicao[0]][posicao[1]] == 0 and cromossomo[posicao[0]][posicao[1]] == 2:
        if not isFirstTime(estado_atual):
            if verifyInMat(estado_atual, posicao):
                print('Move is Valid')
                return True
            elif geracao > 200:
                return True
        else:
            return True
    return False

def isMoveValidStage2(estado_atual, cromossomo, tupla, geracao):
    #linhas e qds são ambos de len = 2
    linhas = tupla[0]
    qds = tupla[1]
     #primeiro parametro é a posicao no estado atual e  
    pos = (linhas[0], qds[0])
    other_pos = (linhas[1], qds[1])
    print('pos ',pos, 'otherpos ', other_pos )
    if isAdjacent(pos, other_pos):
        if estado_atual[pos[0]][pos[1]] == 2 and cromossomo[pos[0]][pos[1]] == 0:
            # print('ok')
            if estado_atual[other_pos[0]][other_pos[1]] == 0 and cromossomo[other_pos[0]][other_pos[1]]  == 2 :
                print('MOVE IS VALID')
                if hasTrail(cromossomo, other_pos):
                    return True
                elif geracao > 300:
                    if verifyInMat(cromossomo, other_pos):
                        return True
                    elif geracao > 400:
                        return True
                        
    return False

def isMoveValidStage3(estado_atual, cromossomo, tupla, geracao):
    linhas = tupla[0]
    qds = tupla[1]
     #primeiro parametro é a posicao no estado atual e  
    pos = (linhas[0], qds[0])
    other_pos = (linhas[1], qds[1])
    # print('pos ',pos, 'otherpos ', other_pos )
    if estado_atual[pos[0]][pos[1]] == 2 and cromossomo[pos[0]][pos[1]] == 0:
        # print('ok')
        if estado_atual[other_pos[0]][other_pos[1]] == 0 and cromossomo[other_pos[0]][other_pos[1]]  == 2 :
            if hasTrail(cromossomo, other_pos):
                return True
            elif geracao > 300:
                if verifyInMat(cromossomo, other_pos):
                    return True
                elif geracao > 400:
                    return True
                    # print('MOVE IS VALID')
    return False


def verifyInMat(estado_atual, pos):
    adj = table_of_adj[pos[0]][pos[1]] if pos else None
    if adj:
        for it in adj:
            if estado_atual[it[0]][it[1]] == 2:
                return True
    return False

def isFirstTime(estado_atual):
    for k in estado_atual:
        if 2 in k:
            return False
    return True

def hasTupleAdj(listTuple):
    for k in listTuple:
        for j in listTuple:
            if k == j:
                continue
            if isAdjacent(k,j):
                return k
    return None

def hasTupleAdjInLists(listTuple1, listTuple2):
    for player in listTuple1:
        for ia in listTuple2:
            if isAdjacent(player,ia):
                return player
    return None

def hasTrail(cromo, newpos):
    adj = table_of_adj[newpos[0]][newpos[1]]
    values = []
    for pos in adj:
        values.append(cromo[pos[0]][pos[1]])
    if all(i == 2 for i in values):
        return True
    return False

