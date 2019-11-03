'''
Controlador de Jogo
testa as interceções 
'''

import numpy as np

class Controller:    
    def __init__(self):
        inv = -30

        # Configurações gerais
        self.points = [[inv, inv], [61, 63], [140, 146], [220, 229], [300, 63], [300, 146], [300, 219], [540, 63], [461, 146], [382, 229], [61, 304], [140, 304], [220, 304], [inv, inv], [inv, inv], [inv, inv], [381, 304], [460, 304], [538, 304], [61, 539], [140, 461], [220, 380], [300, 539], [300, 461], [300, 380], [540, 539], [461, 461], [382, 380]]    
        self.qtdPoints = len(self.points)
        self.radius = 30

        # controlador de quem vai jogar
        self.turnPlayer = False
        self.turnMachine = False
        
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


def main():
    control = Controller()

    # matriz de interesse
    print(control.match(290, 390))

if __name__ == "__main__":
    main()