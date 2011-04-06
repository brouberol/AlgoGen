# -*- coding: utf-8 -*-

from random import *
import networkx as nx
from CGraph import *


class pyAG:
    def __init__(self,N,prod,nodes,txMut,txCross,fita,fitb,fitc):
	self.N=N # Nombre d'individus par population
        self.nodes = nodes
	self.txMut=txMut # Taux de mutation
	self.txCross=txCross # Taux de crossover
	self.prod = prod # individu (graphe)
	self.pop = [prod(nodes) for i in range(N)] # generation
	self.gen = 0 # 
        self.newpop = None
        self.fita=fita # 
        self.fitb=fitb # Parametres pour la somme de fitness
        self.fitc=fitc #
        self.fitness=[]

	
    def new_pop(self):
        #if self.newpop is not None:
            #for i in range(len(self.newpop)):
                # self.newpop[i].clear() # Destruction des graphe de la generation precedente
        self.newpop=[]
        
	for i in range(self.N):
	    r = randint(0,(self.N+1)*(self.N)/2)
	    x = Index(self.N,r)
	    # print x,self.fitness[x][0]
	    self.newpop.append(self.prod(self.nodes,self.pop[self.fitness[x][1]].genome)) 


    def mutation(self):
	for graph in self.newpop:
	    gen = graph.genome
	    for i in range(len(gen)):
		if random.random()<self.txMut:
		    gen[i]=1-gen[i]
	    graph.genome=gen

    def cross(self):
	for x in self.newpop:
	    if random.random() < self.txCross:
		g = x.genome
		r1= self.pop[randint(0,self.N-1)].genome
		z= random.randint(0,len(g)-1)
		if random.random() < 0.5:
		    g[0:z]=r1[0:z]
		else:
		    g[z:]=r1[z:]
		x.genome=g

    def update(self):
	self.pop=self.newpop[:]

    def calc_fitness(self):
        self.fitness = []
        for i in range(self.N):
            self.fitness.append((self.pop[i].fitness(self.fita,self.fitb,self.fitc),i))
            self.fitness.sort()
        #print self.fitness


    def fitmin(self):
        return self.fitness[0][0]

    def fitmax(self):
        return self.fitness[self.N-1][0]

    def fitmean(self):
        S = 0
        for i in self.fitness:
            S += i[0]
        res = S/len(self.fitness)
        return res
        
    def genloop(self):
	self.calc_fitness()
        #for i in self.fitness:
            #print i
        #print ""
	self.new_pop()
	self.mutation()
	self.cross()
	self.update()
	self.gen += 1
	print "Generation {3},  FitMin = {0:4}, FitMean = {1:4}, FitMax = {2:4}".format(self.fitmin(),self.fitmean(),self.fitmax(),self.gen) 

def Index(N,x):
    ind = 0
    j=0
    while x>ind:
        ind += N-j
        j+=1
    return j-1


# MAIN----------------------

seed(14)



# A ADAPTER A VOS BESOINS !
nbGraph = 50
nbNodes = 100

txMut = 0.2
txCrossOver = 0.2

# parametres de ponderation de fitness
a = 0.5
b = 0.2
c = 0.1


AlgoGen = pyAG(nbGraph,CGraph,nbNodes,txMut,txCrossOver,a,b,c)
#AlgoGen.calc_fitness()

for i in range(100):
    AlgoGen.genloop()


# r=0
# f=open("btr2.dat","w")
# for x in ga.pop[ga.f[0][1]].genome:
#     r+=2*x-1
#     f.write("%d\n"%r)
# f.close()


