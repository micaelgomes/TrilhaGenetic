'''
Controlador de Jogo
testa as interceções 
'''

import numpy as np

class Controller:    
    def __init__(self):
        # Configurações gerais
        self.points = [[61, 63], [140, 146], [220, 229], [300, 63], [300, 146], [300, 229], [540, 63], [461, 146], [382, 229], [61, 304], [140, 304], [220, 304], [381, 304], [460, 304], [538, 304], [61, 539], [140, 461], [220, 380], [300, 539], [300, 461], [300, 380], [540, 539], [461, 461], [382, 380]]    
        
        # Ligações entre os nodos
        self.neighbor = {0: [3, 9], 1: [4, 10], 2: [5, 11], 3: [0, 4, 6], 4: [1, 3, 5, 7], 5: [2, 4, 8], 6: [3, 14], 7: [4, 13], 8: [5, 12], 9: [0, 10, 15], 10: [1, 9, 11, 16], 11: [2, 10, 17], 12: [8, 13, 23], 13: [7, 12, 14, 22], 14: [6, 13, 21], 15: [9, 18], 16: [10, 19], 17: [11, 20], 18: [15, 19, 21], 19: [16, 18, 20, 22], 20: [17, 19, 23], 21: [14, 18], 22: [13, 19], 23: [12, 20]}
        self.qtdPoints = len(self.points)
        self.radius = 30

        # stage Controller
        self.stage1_player = False
        self.stage2_player = False
        self.stage3_player = False
        
        self.stage1_machine = False
        self.stage2_machine = False
        self.stage3_machine = False

        # Controlador de Turnos
        self.playerTurn = True
        
        # já passou do 1º estágio e dimininuio o número de peças
        self.passed1Stage = False
        self.machinePassed1Stage = False

        # controlador de exclusão após trilha
        self.executeOrder66 = False
        self.executePiecePlayer = False

        # array de trilhas formadas
        self.trailPlayer = np.zeros((self.qtdPoints, self.qtdPoints, self.qtdPoints))
        self.trailMachine = np.zeros((self.qtdPoints, self.qtdPoints, self.qtdPoints))
        self.setTrailPositionsPlayer()
        self.setTrailPositionsMachine()

        # last trail
        self.lastTrailPlayer = []
        self.lastTrailMachine = []

    def getNeighbor(self, i):
        if i >= 0 and i <= self.qtdPoints:
            return self.neighbor[i]

        return -1

    def getX(self, x):
        for i in range(self.qtdPoints):
            if x >= self.points[i][0] - self.radius and x <= self.points[i][0]:
                return self.points[i][0] - 15

        return -30

    def getY(self, y):
        for i in range(self.qtdPoints):
            if y >= self.points[i][1] - self.radius and y <= self.points[i][1]:
                return self.points[i][1] - 15

        return -30

    def getXY(self, i):
        if i <= self.qtdPoints:
            return self.points[i]

        return [-100, -100]

    def match(self, x, y):
        for i in range(self.qtdPoints):
            if x >= self.points[i][0] - self.radius and x <= self.points[i][0] + self.radius and y >= self.points[i][1] - self.radius and y <= self.points[i][1] + self.radius:
                return True

        return False

    def getMark(self, x, y):
        for i in range(self.qtdPoints):
            if x >= self.points[i][0] - self.radius and x <= self.points[i][0] + self.radius and y >= self.points[i][1] - self.radius and y <= self.points[i][1] + self.radius:
                return i

        return -1

    def setTrailPositionsPlayer(self):
        self.trailPlayer[0][3][6] = 1
        self.trailPlayer[1][4][7] = 1
        self.trailPlayer[2][5][8] = 1
        self.trailPlayer[17][20][23] = 1
        self.trailPlayer[16][19][22] = 1
        self.trailPlayer[15][18][21] = 1
        self.trailPlayer[12][13][14] = 1
        self.trailPlayer[9][10][11] = 1
        self.trailPlayer[0][9][15] = 1
        self.trailPlayer[1][10][16] = 1
        self.trailPlayer[2][11][17] = 1
        self.trailPlayer[8][12][23] = 1
        self.trailPlayer[7][13][22] = 1
        self.trailPlayer[6][14][21] = 1
        self.trailPlayer[3][4][5] = 1
        self.trailPlayer[20][19][18] = 1

    def setTrailPositionsMachine(self):
        self.trailMachine[0][3][6] = 1
        self.trailMachine[1][4][7] = 1
        self.trailMachine[2][5][8] = 1
        self.trailMachine[17][20][23] = 1
        self.trailMachine[16][19][22] = 1
        self.trailMachine[15][18][21] = 1
        self.trailMachine[12][13][14] = 1
        self.trailMachine[9][10][11] = 1
        self.trailMachine[0][9][15] = 1
        self.trailMachine[1][10][16] = 1
        self.trailMachine[2][11][17] = 1
        self.trailMachine[8][12][23] = 1
        self.trailMachine[7][13][22] = 1
        self.trailMachine[6][14][21] = 1
        self.trailMachine[3][4][5] = 1
        self.trailMachine[20][19][18] = 1

    def isTrailPlayer(self, chromosome):
        for i in range(self.qtdPoints):
            for j in range(self.qtdPoints):
                for k in range(self.qtdPoints):
                    if self.trailPlayer[i][j][k] != 0:

                        if self.trailPlayer[i][j][k] == 1:
                            if chromosome[i] == 1 and chromosome[j] == 1 and chromosome[k] == 1:
                                last = i, j, k
                                self.lastTrailPlayer.append(last)
                                self.trailPlayer[i][j][k] = 2
                                return True
                        else:
                            self.trailPlayer[i][j][k] = 2

        return False
                            
    def isTrailMachine(self, chromosome):
        for i in range(self.qtdPoints):
            for j in range(self.qtdPoints):
                for k in range(self.qtdPoints):
                    if self.trailMachine[i][j][k] != 0:
                        if self.trailMachine[i][j][k] == 1:
                            if chromosome[i] == 2 and chromosome[j] == 2 and chromosome[k] == 2:
                                last = i, j, k
                                self.lastTrailMachine.append(last) 
                                self.trailMachine[i][j][k] = 2
                                return True
                        else:
                            self.trailMachine[i][j][k] = 2
        return False

    def disolveTrail(self, chromosome):
        tmpNewTrailPlayer = []
        tmpNewTrailMachine = []

        for i in range(len(self.lastTrailPlayer)):
            k = self.lastTrailPlayer[i]
            if not (chromosome[k[0]] == 1 and chromosome[k[1]] == 1 and chromosome[k[2]] == 1):
                self.trailPlayer[k[0]][k[1]][k[2]] = 1
            else:
                tmpNewTrailPlayer.append(self.lastTrailPlayer[i])

        for i in range(len(self.lastTrailMachine)):
            k = self.lastTrailMachine[i]
            if not (chromosome[k[0]] == 2 and chromosome[k[1]] == 2 and chromosome[k[2]] == 2):
                self.trailMachine[k[0]][k[1]][k[2]] = 1
            else:
                tmpNewTrailMachine.append(self.lastTrailMachine[i])

        self.lastTrailPlayer = tmpNewTrailPlayer
        self.lastTrailMachine = tmpNewTrailMachine


def main():
    control = Controller()

    print(control.neighbor[4])


if __name__ == "__main__":
    main()