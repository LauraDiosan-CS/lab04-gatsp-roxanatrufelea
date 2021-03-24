
import networkx as nx
from locale import atoi
import math


def euclidian(t1, t2):
        return math.sqrt((t1[0] - t2[0]) ** 2 + (t1[1] - t2[1]) ** 2)
class FileRepository(object):
    def __init__(self,__filename):
        self.__filename=__filename
     
        
    def __loadFromFile(self):
        f=open(self.__filename+".txt","r")
        listCities=[]
        lines = [line.rstrip() for line in f]
        nrCities=atoi(lines[0])
        for nrCity in range(nrCities):
            params=lines[nrCity+1].split(",")
            distances=[]
            for dist in params:
                distances.append(atoi(dist))
            listCities.append(distances)
    
        print("nrCities:",nrCities)
        print("listCities:",listCities)
        return (nrCities,listCities)
    
    def getCities(self):
        return self.read_tsp_file()
                 
    

    def read_tsp_file(self):
        f = open(self.__filename, "r")
        for i in range(3):
            f.readline()
        n = int(f.readline().split(" ")[-1])
        for i in range(2):
            f.readline()
        coord = {}
        for i in range(1, n+1):
            line = f.readline().split(" ")
            coord[float(line[0])] = (float(line[1]), float(line[2]))
        mat = []
        for i in range(n):
            mat.append([0] * n)
        for i in range(n):
            for j in range(n):
                if i<j:
                    e = euclidian(coord[i+1], coord[j+1])
                    mat[i][j] = e
                    mat[j][i] = e
        f.close()
        return (n,mat)
    
    
    