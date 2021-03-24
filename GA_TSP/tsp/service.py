from tsp.ga import GA
from tsp.chromosome import Chromosome
class Service:
    def __init__(self,__repo):
        self.__repo=__repo
   
    def evalFc(self,repres,cities):
        fitness=0
        for i in range(len(repres)):
            if(i==len(repres)-1):
                fitness+=cities[0][repres[i]]
            else:
                fitness+=cities[repres[i]][repres[i+1]]
        return fitness
    
    def gaTsp(self):
        
        
      
        gaParam = {'popSize' : 200, 'noGen' : 500, 'pc' : 0.4}
       
       
        
        nrCities=self.__repo.getCities()[0];
        listCities=self.__repo.getCities()[1];
        problParam = {'function' : self.evalFc, 'noNodes' : nrCities, 'cities':listCities}
           
        
          
        ga = GA(gaParam,problParam)
        ga.initialisation()
        ga.evaluation()
            
        bestOverAll=Chromosome(problParam)
        bestOverAll.fitness=100000
        
        f=open("out.txt","a")
        for g in range(gaParam['noGen']):
           
            ga.oneGenerationSteadyState()
            
            bestChromo = ga.bestChromosome()
            
            if(bestChromo.fitness<bestOverAll.fitness):
                bestOverAll.fitness=bestChromo.fitness
                bestOverAll.repres=bestChromo.repres
            
            print('Best solution in generation '+ ' f(x) = ' + str(bestChromo.fitness))
            f.write(str(bestChromo.fitness)+"\n")
            print(bestChromo.repres)
            
        print("Best fitness over all:",bestOverAll.fitness)
        print("Best generation:",bestOverAll.repres)