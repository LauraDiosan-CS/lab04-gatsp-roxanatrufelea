from random import randint
from tsp.chromosome import Chromosome


class GA:
    def __init__(self, __param, __problParam ):
        self.__param = __param
        self.__problParam = __problParam
        self.__population = []
        
    @property
    def population(self):
        return self.__population
    
    def initialisation(self):
        for _ in range(0, self.__param['popSize']):
            c = Chromosome(self.__problParam)
            self.__firstNode(c)
            self.__population.append(c)
    
    def evaluation(self):
        for c in self.__population:
            c.fitness = self.__problParam['function'](c.repres,self.__problParam['cities'])
            
    def bestChromosome(self):
        best = self.__population[0]
        for c in self.__population:
            if (c.fitness < best.fitness):
                best = c
        return best
        
    def worstChromosome(self):
        worst = self.__population[0]
        poz=0
        for i in range(len(self.__population)):
            if(self.__population[i].fitness > worst.fitness):
                poz=i
                worst=self.__population[i]
        
        return (worst,poz)
    
    def __firstNode(self,c):
        if(c.repres[0]==0):
            return 
        for i in range(len(c.repres)):
            if(c.repres[i]==0):
                break
        c.repres[i],c.repres[0]=c.repres[0],c.repres[i]

    def selection(self):
            
        pos=[]
        bestpos=randint(0, self.__param['popSize'] - 1)
        for _ in range (int(self.__param['pc']*self.__param['popSize'])):
            pos.append(randint(0, self.__param['popSize'] - 1))
            
        for i in range (int(self.__param['pc']*self.__param['popSize'])):
            if (self.__population[pos[i]].fitness > self.__population[i].fitness):
                bestpos=pos[i]
        return bestpos
        
        
    def oneGenerationSteadyState(self):
        for _ in range(self.__param['popSize']):
            p1 = self.__population[self.selection()]
            p2 = self.__population[self.selection()]
            off1=p1.crossover(p2)
            off2=p1.crossover(p2)
            off1.mutation()
            off2.mutation()
            self.__firstNode(off1)
            self.__firstNode(off2)
            off1.fitness = self.__problParam['function'](off1.repres,self.__problParam['cities'])
            off2.fitness= self.__problParam['function'](off2.repres,self.__problParam['cities'])
            
            poz=self.worstChromosome()[1]
            if(off1.fitness<off2.fitness):
                self.__population[poz]=off1
            else:
                self.__population[poz]=off2