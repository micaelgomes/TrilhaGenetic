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
    print('aux ', aux, 'comparar : ' ,(other_pos in aux))
    return (other_pos in aux)

'''
def rotation(estado_atual, cromossomo, linha, qd):
    if linha != lastRow:
        return estado_atual[linha + 1][qd] == cromossomo[linha][qd]
    else:
        return cromossomo[0][qd] == cromossomo[linha][qd]

def antirotation(estado_atual, cromossomo, linha, qd):
    if linha != firstRow:
        return cromossomo[linha - 1][qd] == cromossomo[linha][qd]
    else:
        return cromossomo[0][qd] == cromossomo[linha][qd]

def changeQd(estado_atual, cromossomo, linha, qd, move_qd):
    if qd == 1:
        return cromossomo[linha][qd+1] == cromossomo[linha][qd]
    elif qd == 3:
        return cromossomo[linha][qd-1] == cromossomo[linha][qd]
    elif move_qd == 'interno':
        return cromossomo[linha][qd+1] == cromossomo[linha][qd]
    elif move_qd == 'externo':
        return cromossomo[linha][qd-1] == cromossomo[linha][qd]

'''

def isMoveValidStage2(estado_atual, cromossomo, tupla):
    #linhas e qds são ambos de len = 2
    linhas = tupla[0]
    qds = tupla[1]
     #primeiro parametro é a posicao no estado atual e  
    pos = (linhas[0], qds[0])
    other_pos = (linhas[1], qds[1])
    print('pos ',pos, 'otherpos ', other_pos )
    if isAdjacent(pos, other_pos):
        if estado_atual[pos[0]][pos[1]] == 2 and cromossomo[pos[0]][pos[1]] == 0:
            print('ok')
            if estado_atual[other_pos[0]][other_pos[1]] == 0 and cromossomo[other_pos[0]][other_pos[1]]  == 2 :
                print('MOVE IS VALID')
                return True
    return False

def isMoveValidStage1(estado_atual,cromossomo, tupla):
    linha = tupla[0]
    qd = tupla[1]
    #há apenas uma posicao para ser avaliada
    posicao = (linha[0],qd[0])
    if estado_atual[posicao[0]][posicao[1]] == 0 and cromossomo[posicao[0]][posicao[1]] == 2:
        print('Move is Valid')
        return True
    return False

def isMoveValidStage3(estado_atual, cromossomo, tupla):
    pass