'''
Algoritmo Genético do Jogo
'''

class Genetic:
    def __init__(self):
        self.sizeChromosome = 27
        # Random
        # self.chromosome = [1,1,0,1,2,0,1,0,1,2,1,2,1,2,0,0,0,2,1,2,0,2,0,2,0,2,1]
        # start
        self.chromosome = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        # begin 2nd stage
        # self.chromosome = [2,2,2,2,2,2,2,2,2,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1]


    def getChromosome(self):
        return self.chromosome

    def setPositionPlayer(self, position):
        if position >= 0 and position <= 27:
            self.chromosome[position] = 1

    def removePiece(self, position):
        if position >= 0 and position <= 27:
            self.chromosome[position] = 0

    def setPositionMachine1stage(self):
        for i in range(self.sizeChromosome):
            if self.chromosome[i] == 0:
                self.chromosome[i] = 2
                break

    def setPositionMachine2stage(self):
        pass

    def setPositionMachine3stage(self):
        pass

    def getQtdPiecesPlayer(self):
        qtd = 0

        for i in range(self.sizeChromosome):
            if self.chromosome[i] == 1:
                qtd = qtd + 1

        return qtd

    def getQtdPiecesMachine(self):
        qtd = 0

        for i in range(27):
            if self.chromosome[i] == 2:
                qtd = qtd + 1

        return qtd

    def isTrailPlayer(self):
        if self.chromosome[0] == 1 and self.chromosome[3] == 1 and self.chromosome[6] == 1: return True
        elif self.chromosome[1] == 1 and self.chromosome[4] == 1 and self.chromosome[7] == 1: return True
        elif self.chromosome[2] == 1 and self.chromosome[5] == 1 and self.chromosome[8] == 1: return True
        elif self.chromosome[6] == 1 and self.chromosome[17] == 1 and self.chromosome[24] == 1: return True
        elif self.chromosome[7] == 1 and self.chromosome[16] == 1 and self.chromosome[25] == 1: return True
        elif self.chromosome[8] == 1 and self.chromosome[15] == 1 and self.chromosome[26] == 1: return True
        elif self.chromosome[18] == 1 and self.chromosome[21] == 1 and self.chromosome[24] == 1: return True
        elif self.chromosome[19] == 1 and self.chromosome[22] == 1 and self.chromosome[25] == 1: return True
        elif self.chromosome[20] == 1 and self.chromosome[23] == 1 and self.chromosome[26] == 1: return True
        elif self.chromosome[0] == 1 and self.chromosome[9] == 1 and self.chromosome[18] == 1: return True
        elif self.chromosome[1] == 1 and self.chromosome[10] == 1 and self.chromosome[19] == 1: return True
        elif self.chromosome[2] == 1 and self.chromosome[11] == 1 and self.chromosome[20] == 1: return True
        elif self.chromosome[3] == 1 and self.chromosome[4] == 1 and self.chromosome[5] == 1: return True
        elif self.chromosome[15] == 1 and self.chromosome[16] == 1 and self.chromosome[17] == 1: return True
        elif self.chromosome[21] == 1 and self.chromosome[22] == 1 and self.chromosome[23] == 1: return True
        elif self.chromosome[9] == 1 and self.chromosome[10] == 1 and self.chromosome[11] == 1: return True
        else: return False

    def isTrailMachine(self):
        if self.chromosome[0] == 2 and self.chromosome[3] == 2 and self.chromosome[6] == 2: return True
        elif self.chromosome[1] == 2 and self.chromosome[4] == 2 and self.chromosome[7] == 2: return True
        elif self.chromosome[2] == 2 and self.chromosome[5] == 2 and self.chromosome[8] == 2: return True
        elif self.chromosome[6] == 2 and self.chromosome[17] == 2 and self.chromosome[24] == 2: return True
        elif self.chromosome[7] == 2 and self.chromosome[16] == 2 and self.chromosome[25] == 2: return True
        elif self.chromosome[8] == 2 and self.chromosome[15] == 2 and self.chromosome[26] == 2: return True
        elif self.chromosome[18] == 2 and self.chromosome[21] == 2 and self.chromosome[24] == 2: return True
        elif self.chromosome[19] == 2 and self.chromosome[22] == 2 and self.chromosome[25] == 2: return True
        elif self.chromosome[20] == 2 and self.chromosome[23] == 2 and self.chromosome[26] == 2: return True
        elif self.chromosome[0] == 2 and self.chromosome[9] == 2 and self.chromosome[18] == 2: return True
        elif self.chromosome[1] == 2 and self.chromosome[10] == 2 and self.chromosome[19] == 2: return True
        elif self.chromosome[2] == 2 and self.chromosome[11] == 2 and self.chromosome[20] == 2: return True
        elif self.chromosome[3] == 2 and self.chromosome[4] == 2 and self.chromosome[5] == 2: return True
        elif self.chromosome[15] == 2 and self.chromosome[16] == 2 and self.chromosome[17] == 2: return True
        elif self.chromosome[21] == 2 and self.chromosome[22] == 2 and self.chromosome[23] == 2: return True
        elif self.chromosome[9] == 2 and self.chromosome[10] == 2 and self.chromosome[11] == 2: return True
        else: return False

def main():
    print('genetic works!')

if __name__ == "__main__":
    main()