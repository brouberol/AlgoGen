from random import *
import networkx as nx
import CGraph


# class te:
#     def __init__(self,ge=None):
# 	if ge is None :
# 	    self.genome=[randint(0,1) for x in range(2000)]
# 	else:
# 	    self.genome=ge[:]
#     def fitness(self):
# 	r=0
# 	g = 0
# 	for i,x in enumerate(self.genome):
# 	    r+= 2*x-1
# 	    if i>1000:
# 		if r>4 or r<-4:
# 		    g+=1
# 	return g





class pyAG:
    def __init__(self,N,prod,txMut,txCross,fita,fitb,fitc):
	self.N=N # Nombre d'individus par population
	self.txMut=txMut # Taux de mutation
	self.txCross=txCross # Taux de crossover
	self.prod = prod # individu (graphe)
	self.pop = [prod() for i in range(N)] # generation
	self.gen = 0 # 
        self.newpop = None
        self.fita=fita # 
        self.fitb=fitb # Parametres pour la somme de fitness
        self.fitc=fitc #
        self.fitness=[-1]*self.N

    def index(N,x):
    ind = 0
    j=0
    while x>ind:
	ind += N-j
	j+=1
    return j-1
	
    def new_pop(self):
        if self.newpop is not None:
            for i in range(len(self.newpop)):
                # self.newpop[i].clear() # Destruction des graphe de la generation precedente

	self.newpop=[]
        
	for i in range(self.N):
	    r = randint(0,(self.N+1)*(self.N)/2)
	    x = index(self.N,r)
	    ## print x,self.fitness[x][0]
	    self.newpop.append(self.prod(self.pop[self.fitness[x][1]].genome)) 

    def mutation(self):
	for graph in self.newpop:
	    gen = graph.genome
	    for i in range(len(gen)):
		if random()<self.txMut:
		    gen[i]=1-gen[i]
	    graph.genome=gen

    def cross(self):
	for x in self.newpop:
	    if random()<self.txCross:
		g = x.genome
		r1= self.pop[randint(0,self.N-1)].genome
		z= randint(0,len(g)-1)
		if random()<0.5:
		    g[0:z]=r1[0:z]
		else:
		    g[z:]=r1[z:]
		x.genome=g

    def update(self):
	self.pop=self.newpop[:]
        # Attention a l'operateur de copie
        # Delete dans newpop
        # Il faudra supprimer chaque elt de pop et copier

    def calc_fitness(self):
        for i in range(self.N):
            self.fitness[i]=self.pop[i].fitness(self.fita,self.fitb,self.fitc)

    def genloop(self):
	ga.calc_fitness()
	self.new_pop()
	self.mutation()
	self.cross()
	self.update()
	self.gen += 1
	print self.fitm,self.fim # Fitness max - Fitness min ? A VERIFIER

seed(11)

ga=pyAG(100,te,0.0001,0.5)
ga.calc_fitness()

for i in range(1000):
    ga.genloop()

r=0
f=open("btr2.dat","w")
for x in ga.pop[ga.f[0][1]].genome:
    r+=2*x-1
    f.write("%d\n"%r)
f.close()


# BOUCLE 
