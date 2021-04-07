from tsp.ga import GA
from tsp.chromosome import Chromosome
from tsp.repo import FileRepository


class Service:
    def __init__(self,__repo):
        self.__repo=__repo

    
    def main(self):
        
        nrNodes,nodes=self.__repo.getCities()
        
        parameters= {'popSize' : 100, 'noGen' : 500, 'pc' : 0.4,'noNodes' : nrNodes, 'nodes':nodes}
        
        ga = GA(parameters)
        ga.initialisation()
        ga.evaluation()
        
        f=open("out.txt","a")
        
        for g in range(parameters['noGen']):
           
            ga.SteadyState()
            
            chrom= ga.bestChromosome()
            f.write(str(chrom.fitness)+"\n")
            
            
repo=FileRepository("in.txt")
service=Service(repo)
service.main()
           
            
      