import numpy as np
import random as rd
import gameMoviment as gm
'''
The representation space value is : 0,1,2 (0 - not ocupped, 1 - play1, 2 - play2 )
Chromosome, in this problem, is state of game (or a possible solution).

'''
f = open('PrintTesteArq.txt', 'w')


def convertToGame(l):
    printTeste(l)
    b = np.reshape(l, (8, 3))
    return b


def printTeste(*args):
    print('-->  ' + str(args), file=f)


class Genetico:
    def __init__(self, estado_atual,stage=1):
        self.estado_atual = estado_atual
        self.num_solutions = 10
        self.num_places_in_board = 24
        self.pop_size = (self.num_solutions, self.num_places_in_board)
        self.factorMutagenese = 9
        self.pin_IA = 2
        self.old_pop = []
        self.new_pop = []
        self.result = None
        self.first_generation = True
        self.stage = stage

    def initial_population(self):
        # distribuição uniforme inicial
        self.old_pop = np.random.randint(low=0.0, high=3.0, size=(
            self.num_solutions - 1, self.num_places_in_board))
        printTeste(self.old_pop)
        self.old_pop = np.append(self.old_pop, self.estado_atual, axis=0)
        printTeste(self.old_pop)

    def calcFit(self, cromossomo):
        # para fase nao voo
        # linhas ou qudrante com 2 peças implica em mais pontos
        # se trancar jogador melhor forma
        cromossomo = convertToGame(cromossomo)
        estado_atual_game = convertToGame(self.estado_atual)
        fit = 0
        for i in range(8):
            if i % 2 != 0:
                if cromossomo[i][0] == cromossomo[i][1] or cromossomo[i][0] == cromossomo[i][2] or cromossomo[i][1] == cromossomo[i][2]:
                    fit += 1
            if i % 2 == 0:
                if i+2 != 8:
                    for j in range(3):
                        if cromossomo[i][j] == cromossomo[i+1][j] or cromossomo[i][j] == cromossomo[i+2][j] or cromossomo[i+1][j] == cromossomo[i+2][j]:
                            fit += 1
                else:
                    for j in range(3):
                        if cromossomo[i][j] == cromossomo[i+1][j] or cromossomo[i][j] == cromossomo[0][j] or cromossomo[i+1][j] == cromossomo[0][j]:
                            fit += 1
        value_discrepance = len(np.where(estado_atual_game != cromossomo)[0])
        printTeste('discrepance : ', value_discrepance, ' fit value: ', fit, 'result fit = ',
                   fit / value_discrepance if value_discrepance == 2 else -9999999999999999999)

        # return fit / value_discrepance if value_discrepance != 0 else -9999999999999999999
        return fit / value_discrepance if value_discrepance == 2 else -9999999999999999999

    def fitness(self, Pop):
        self.fitness_pop = np.zeros(self.num_solutions)
        printTeste('pop : ', len(Pop))
        for index, individuo in enumerate(Pop):
            printTeste('index >;', index)
            self.fitness_pop[index] = self.calcFit(individuo)
        # return array of each solution's fitness value

    def parents(self):
        # return peer of sulutions for crossover
        if not self.first_generation:
            a = np.amax(self.fitness_pop)
            #print('maior fit : ',a)
            cp = self.fitness_pop.copy()
            cp_ind = np.where(cp == a)
            # print(cp_ind)
            cp = np.delete(cp, cp_ind[0][0])
            # print(cp)
            b = np.amax(cp)
            #print('segunda maior fit : ', b)
            a_ind = np.where(self.fitness_pop == a)
            a_ind = a_ind[0][0] if type(a_ind) != int else a_ind
            # print(a_ind)
            b_ind = np.where(self.fitness_pop == b)
            b_ind = b_ind[0][0] if type(b_ind) != int else b_ind
            # print(b_ind)
        else:
            a_ind, b_ind = 0, 1

        return self.old_pop[a_ind], self.old_pop[b_ind]

    def survive(self):
        '''
            melhor resultado é o de maior fit
        '''
        a = np.amax(self.fitness_pop)
        printTeste('matriz fitness ', len(self.fitness_pop))
        a_ind = np.where(self.fitness_pop == a)
        a_ind = a_ind[0][0] if type(a_ind) != int else a_ind
        printTeste('new_pop ',  len(self.new_pop))
        self.best = self.new_pop[a_ind]
        printTeste('best = ', self.best, ' fit = ', a)
        # return the best solution (the best fitness)

    def crossover(self):
        # return new children(or offspring )
        f1, f2 = self.parents()
        f1_ind = rd.randint(0, self.num_places_in_board - 1)
        f2_ind = rd.randint(0, self.num_places_in_board - 1)
        f1[f1_ind], f2[f2_ind] = f2[f2_ind], f1[f1_ind]
        self.new_pop.append(list(f1))  # escolha de f1 foi aleatoria
        if len(self.new_pop) < self.num_solutions:
            self.new_pop.append(list(f2))

    def mutation(self):
        children = rd.randint(0, 9)
        gene_for_mutation = rd.randint(0, 23)
        # aleatory change at defined gene (define new phenotype)
        # if rd.randint(0, 100) % self.factorMutagenese == 0:
        if rd.randint(1, 100) <= 3:
            self.new_pop[children][gene_for_mutation] = self.pin_IA

    # condições de movimento
    def compare(self, cromossomo):
        cromo_like_game = convertToGame(cromossomo)
        estado_atual_game = convertToGame(self.estado_atual)
        indices = np.where(estado_atual_game != cromo_like_game)
        printTeste('indices fora : ', indices, len(indices[0]))
        if len(indices[0]) == 2:  # verifica se ha apenas duas tuplas alterada
            # verificar se o indices correspondem a um moviment
            print('indices: ', indices)
            return gm.isMoveValid(estado_atual_game, cromo_like_game, indices)
        return False

    def solutionIsReady(self):
        for cromo in self.new_pop:
            if self.compare(cromo):
                self.result = cromo
                return True
        return False

    def rePreparing(self):
        self.old_pop = self.new_pop
        self.new_pop = []
        self.new_pop.append(self.best)
        self.first_generation = False

    def newGeneration(self):
        self.initial_population()
        self.fitness(self.old_pop)
        self.new_pop.append(self.old_pop[9])
        ind_geracao = 0
        print("Buscando solução ...")
        while True:
            # Teste:
            ind_geracao += 1
            #print('geracao %i' % (ind_geracao))
            # fimTeste
            #print('Geracao anterior : ',self.old_pop)
            # for _i in range(self.num_solutions-1):
            while len(self.new_pop) < self.num_solutions:
                # get the best result fitness
                self.crossover()
            self.mutation()
            self.fitness(self.new_pop)
            if self.solutionIsReady():
                break
            self.new_pop = np.asarray(self.new_pop)
            self.survive()
            #print('Geracao posterior : ', self.new_pop)
            self.rePreparing()
            # if ind_geracao >= 10 :
            #    break
        print('Solucao encontrado na geracao ', ind_geracao)
        return self.result

