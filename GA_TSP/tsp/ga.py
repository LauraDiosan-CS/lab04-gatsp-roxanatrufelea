from random import randint
from tsp.chromosome import Chromosome




def evaluation(rep,nodes):
    
        fitness=0
        for i in range(len(nodes)):
            if(i==len(nodes)-1):
                fitness+=nodes[0][rep[i]]
            else:
                fitness+=nodes[rep[i]][rep[i+1]]
        return fitness
    
class GA:
    def __init__(self, __param):
        self.__param = __param
        self.__population = []
        
    @property
    def population(self):
        return self.__population
    
    def initialisation(self):
        for i in range(0, self.__param['popSize']):
            c = Chromosome(self.__param)
            self.__population.append(c)
    
    def evaluation(self):
        for c in self.__population:
            c.fitness = evaluation(c.repres,self.__param['nodes'])
            
            
    def bestChromosome(self):
        best_chromosome = self.__population[self.__param['popSize']-1]
        for i in range (len(self.__population)-1):
            if (self.__population[i].fitness < best_chromosome.fitness):
                self.__population[i]
        return best_chromosome
    
        
    def worstChromosome(self):
        worst = self.__population[self.__param['popSize']-1]
        worst_position=self.__param['popSize']-1
        for i in range(len(self.__population)):
            if(self.__population[i].fitness > worst.fitness):
                worst_position=i
                worst=self.__population[i]
        
        return worst,worst_position
    


    def selection(self):
  
        
        pos=[]
        bestpos=randint(0, self.__param['popSize'] - 1)
        for _ in range (int(self.__param['pc']*self.__param['popSize'])):
            pos.append(randint(0, self.__param['popSize'] - 1))
            
        for i in range (int(self.__param['pc']*self.__param['popSize'])):
            if (self.__population[pos[i]].fitness > self.__population[i].fitness):
                bestpos=pos[i]
        return bestpos
        
        
    def SteadyState(self):
        for i in range(self.__param['popSize']):
            parent1 = self.__population[self.selection()]
            parent2 = self.__population[self.selection()]
            child=parent1.crossover(parent2)
            child.mutation()
            child.fitness = evaluation(child.repres,self.__param['nodes'])
            
            _,worst_position=self.worstChromosome()
            
            self.__population[worst_position]=child
            