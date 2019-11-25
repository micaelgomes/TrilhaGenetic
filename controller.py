'''
Controlador de Jogo
testa as interceções 
'''

import numpy as np

class Controller:    
    def __init__(self):
        inv = -30

        # Configurações gerais
        self.points = [[inv, inv], [61, 63], [140, 146], [220, 229], [300, 63], [300, 146], [300, 229], [540, 63], [461, 146], [382, 229], [61, 304], [140, 304], [220, 304], [inv, inv], [inv, inv], [inv, inv], [381, 304], [460, 304], [538, 304], [61, 539], [140, 461], [220, 380], [300, 539], [300, 461], [300, 380], [540, 539], [461, 461], [382, 380]]    
        
        # Ligações entre os nodos
        self.neighbor = {1: [4, 10], 2: [5, 11], 3: [6, 12], 4: [1, 5, 7], 5: [2, 4, 6, 8], 6: [3, 5, 9], 7: [4, 18], 8: [5, 17], 9: [6, 16], 10: [1, 11, 19], 11: [2, 10, 12, 20], 12: [3, 11, 21], 16: [9, 17, 27], 17: [8, 16, 18, 26], 18: [7, 17, 25], 19: [10, 22], 20: [11, 23], 21: [12, 24], 22: [19, 23, 25], 23: [20, 22, 24, 26], 24: [21, 23, 27], 25: [18, 22], 26: [17, 23], 27: [16, 24]}
        self.qtdPoints = len(self.points)
        self.radius = 30
        self.excluds = [0,13,14,15]
        
        # stage Controller
        self.stage1 = False
        self.stage2 = False
        self.stage3 = False

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
        if i <= 27 and i not in self.excluds:
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

        return 0

    def getNeighbor(self, i):
        if i >= 0 and i <= 27 and not i in self.excluds :
            return self.neighbor[i]

        else:
            return []


def main():
    control = Controller()

    # matriz de interesse
    # print(control.match(290, 390))
    # print(control.getMarkPosition(3))


if __name__ == "__main__":
    main()