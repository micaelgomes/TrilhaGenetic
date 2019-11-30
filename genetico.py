import gameMoviment as gm 
import random as rd
import methodsList as ml



def printTeste(conteudo, path = 'PrintTesteArq.txt', modoescrita = 'w'):
    f = open(path, modoescrita)
    print('-->  ' + conteudo,file=f)

class Genetico:
    def __init__(self, estado_atual, stage=2, outputResult = 'PrintTesteArq.txt'):
        self.num_solutions = 10
        self.tamCromo = 24
        self.old_pop = []
        self.new_pop = []
        self.estado_atual = estado_atual # deve ser uma lista
        self.fitness_pop = None
        self.memoryOfBests = {}
        self.factorMutagenese = 9
        self.result = None
        self.output = outputResult
        self.modoescrita = 'a'

    def calcFit(self, cromossomo):
        cromo_game = ml.convertListinGameBoard(cromossomo) #convertToGame(cromossomo)
        estado_atual_game = ml.convertListinGameBoard(self.estado_atual) #convertToGame(self.estado_atual)
        potencial = 0
        for i in range(8):
            if i % 2 != 0:
                if cromo_game[i][0] == cromo_game[i][1] or cromo_game[i][0] == cromo_game[i][2] or cromo_game[i][1] == cromo_game[i][2]:
                    potencial += 1
            if i % 2 == 0:
                if i+2 != 8:
                    for j in range(3):
                        if cromo_game[i][j] == cromo_game[i+1][j] or cromo_game[i][j] == cromo_game[i+2][j] or cromo_game[i+1][j] == cromo_game[i+2][j]:
                            potencial += 1
                else:
                    for j in range(3):
                        if cromo_game[i][j] == cromo_game[i+1][j] or cromo_game[i][j] == cromo_game[0][j] or cromo_game[i+1][j] == cromo_game[0][j]:
                            potencial += 1
        value_discrepance = self.calcDiscrepance(estado_atual_game, cromo_game)
        fit = (5*value_discrepance + 2*potencial)/(5+2)
        printTeste(f'discrepance :  {value_discrepance},  potencial value: {potencial},  fit:  {fit}', path=self.output,modoescrita = self.modoescrita )
        return fit
    
    def calcDiscrepance(self, cromo1, cromo2):
        # estabelece um valor para discrepancia
        tab_value = [2,1,0,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27]
        # ind = len(np.where(cromo1!= cromo2)[0])
        flag,indices = ml.compareLists(cromo1, cromo2)
        ind = 0 if flag else len(indices)
        value = tab_value[ind]  
        return 28 - value
    
    def fitness(self, Pop):
        self.fitness_pop = []
        for index, individuo in enumerate(Pop):
            printTeste(f'Cromossomo Selecionado:  {index}', path=self.output,modoescrita = self.modoescrita )
            self.fitness_pop.append(self.calcFit(individuo))

    def parents(self):
        # pais = rd.choices(self.old_pop,weights=self.fitness_pop,k=2)
        pais = rd.choices(self.old_pop,k=2)
        return pais[0].copy(), pais[1].copy() 
            
    def crossover(self):
        p1, p2 = self.parents()
        i1 = rd.randint(0, 23)
        i2 = rd.randint(0, 23)
        p1[i1], p2[i2] = p2[i2] , p1[i1]
        self.new_pop.append(p1)
        if len(self.new_pop) < self.num_solutions:
            self.new_pop.append(p2)
        return # 2 listas

    def mutation(self):
        a = rd.randint(0,100)
        ind = rd.randint(0,9)
        gene = rd.randint(0,23)
        value = rd.randint(0,2)
        if a % self.factorMutagenese == 0 :
            self.new_pop[ind][gene] = value
        return
    
    def survive(self):
        # salva o melhor para a proxima geração
        self.best = None
        for i in range(1,self.num_solutions + 1):
            _, ind = ml.rankList(self.fitness_pop, i)
            self.best = self.new_pop[ind]
            if str(self.best) not in self.memoryOfBests.keys():
                # self.memoryOfBests[str(self.best)] = self.best
                break
        return
    
    def inicialPopulation(self, old_pop):
        #lista randomica de valores inteiros de 0 a 2
        while len(old_pop) < self.num_solutions - 1 :
            old_pop.append( ml.crateListRandomic(self.tamCromo,0,2) )
        old_pop.append(self.estado_atual.copy())
        
    def initAlg(self):
        geracao = 0
        self.inicialPopulation(self.old_pop)
        self.fitness(self.old_pop)
        while True:
            geracao+=1
            while len(self.new_pop) < self.num_solutions:
                self.crossover()
            self.mutation()
            self.fitness(self.new_pop)
            if self.solutionIsReady():
                break
            self.survive()
            self.rePreparing()
        print(f"Resultado encontrado na geracao {geracao} !")
        return self.result , geracao

    def solutionIsReady(self):
        for cromo in self.new_pop:
            cromo_game = ml.convertListinGameBoard(cromo)
            estado_atual_game = ml.convertListinGameBoard(self.estado_atual)
            flag, ind_x, ind_y = ml.compareMatriz(cromo_game, estado_atual_game)
            printTeste(f' self.estado atual = {estado_atual_game} , cromo = {cromo_game}', path=self.output,modoescrita = self.modoescrita )
            print(f'flag = {flag}, ind_x = {ind_x}, ind_y = {ind_y}')
            if flag:
                continue
            if len(ind_x)==2 and len(ind_y)==2 and gm.isMoveValid(estado_atual_game,cromo_game,(ind_x,ind_y)):
                self.result = cromo
                return True
        return False
        
    def rePreparing(self):
        self.old_pop = self.new_pop
        self.new_pop = []
        self.new_pop.append(self.best)
        self.new_pop.append(self.estado_atual.copy())
        self.best = []

