from random import randint, seed
import random

def permutation(n):
    permutation = []
    for i in range (0,n):
        permutation.append(i)
    pos1 = randint(0, n - 1)
    pos2 = randint(0, n - 1)
    permutation[pos1], permutation[pos2] = permutation[pos2], permutation[pos1]
    return permutation




def createRoute(cityList):
    cityList=[i for i in range(len(cityList))]
    route = random.sample(cityList, len(cityList))
    return route


class Chromosome:
    def __init__(self, param):
        self.__param = param 
        self.__repres =permutation(self.__param['noNodes'])
    
    @property
    def repres(self):
        return self.__repres 
    
    @property
    def fitness(self):
        return self.__fitness 
    
    @repres.setter
    def repres(self, l = []):
        self.__repres = l 
    
    @fitness.setter 
    def fitness(self, fit ):
        self.__fitness = fit 
    
    def crossover(self, c):
        
        child = []
        childP1 = []
        childP2 = []
    
        geneA = int(random.random() *  self.__param['noNodes'])
        geneB = int(random.random() *  self.__param['noNodes'])
    
        startGene = min(geneA, geneB)
        endGene = max(geneA, geneB)

        for i in range(startGene, endGene):
            childP1.append(self.repres[i])
        
        childP2 = [item for item in c.repres if item not in childP1]

        child = childP1 + childP2
       
    
    
        off=Chromosome(self.__param)
        off.repres=child
        print(off.repres)
        return off
    
    def mutation(self):
        pos1 = randint(0, self.__param['noNodes'] - 1)
        pos2 = randint(0, self.__param['noNodes'] - 1)
        print(pos1,pos2)
        if (pos2 < pos1):
            pos1, pos2 = pos2, pos1
        el = self.__repres[pos2]
        del self.__repres[pos2]
        self.__repres.insert(pos1 + 1, el)
        
    