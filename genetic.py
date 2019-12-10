'''
Algoritmo Genético do Jogo
'''
from genetico import Genetico
import numpy as np

class Genetic:
    def __init__(self):
        self.sizeChromosome = 24
        # Random
        # self.chromosome = [1,2,1,0,2,0,1,0,1,2,1,2,1,2,0,0,2,2,1,2,1,1,0,2]
        # self.chromosome = [0,2,0,0,0,0,2,0,1,0,1,0,2,2,0,0,2,2,1,2,0,0,0,0]
        # start
        self.chromosome = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        self.clone = self.chromosome[:]

        self.qtdFixedPlayer = 1
        self.qtdFixedMachine = 1

    def getChromosome(self):
        return self.chromosome

    def getClone(self):
        return self.clone

    def resetClone(self):
        self.clone = self.chromosome[:]

    def resetChromosome(self):
        self.chromosome = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

    def getSizeChromosome(self):
        return self.sizeChromosome

    def setPositionPlayer(self, position):
        if position >= 0 and position <= self.sizeChromosome:
            self.chromosome[position] = 1

    def kill1PieceMachine(self, position):
        if position >= 0 and position <= self.sizeChromosome:
            self.chromosome[position] = 0

    def setPossibleMovePlayer(self, position):
        if position >= 0 and position <= self.sizeChromosome:
            self.clone[position] = 3

    def removePiecePlayer(self, position):
        if position >= 0 and position <= self.sizeChromosome:
            self.chromosome[position] = 0

    def removePieceMachine(self):
        g = Genetico(self.chromosome)
        self.chromosome = g.removePieceAdv(self.chromosome.copy())
    
    def setPositionMachine1stage(self):
        g = Genetico(self.chromosome, stage=1)
        solution, _geracao = g.initAlg()
        self.chromosome = solution

    def setPositionMachine2stage(self):
        # Buscando nova jogada a partir do estado atual
        g = Genetico(self.chromosome, stage=2)
        solution, _geracao = g.initAlg()
        self.chromosome = solution

    def setPositionMachine3stage(self):
        g = Genetico(self.chromosome, stage=3)
        solution, _geracao = g.initAlg()
        self.chromosome = solution

    def getQtdPiecesPlayer(self):
        qtd = 0

        for i in range(self.sizeChromosome):
            if self.chromosome[i] == 1:
                qtd = qtd + 1

        return qtd

    def getQtdPiecesMachine(self):
        qtd = 0

        for i in range(self.sizeChromosome):
            if self.chromosome[i] == 2:
                qtd = qtd + 1

        return qtd

def main():
    print('genetic works!')

if __name__ == "__main__":
    main()
