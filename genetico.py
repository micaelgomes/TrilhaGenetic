import numpy as np
'''
The representation space value is : 0,1,2 (0 - not ocupped, 1 - play1, 2 - play2 )
Chromosome, in this problem, is state of game (or a possible solution).

'''

num_solutions = 10
num_places_in_board = 24
pop_size = (input_number, num_places_in_board)

def initial_population():
    #distribuição uniforme inicial
    new_pop = np.random.uniform(low=0.0, high=1.0, size=pop_size)
    return new_pop


def fitness(population):
    #return array of each solution's fitness value

def parents(population, fitness):
    #return peer of sulutions for crossover  

def survive(population, fitness):
    #return the best solution (the best fitness)

def crossover(parents):
    #return new children(or offspring )

def mutation(children, gene_for_mutation):
    #aleatory change a defined gene (define new phenotype)




