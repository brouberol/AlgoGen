import networkx as nx
from numpy import *
import matplotlib.pyplot as plt

class CGraph:

    """ Initialisation du graph """
    def __init__(self,nbNodes):
        self.nbNodes = nbNodes
        
        ThDegres = range(1,self.nbNodes) # Distribution theorique
        ThDegres.reverse()
        ThDistrib = []
        
        for deg in ThDegres:
            ThDistrib.append(self.nbNodes*deg**(-2.2))

        ''' On prend les degres dans le sens decroissant et on calcul l'effectif theorique 
        correspondant a ce degre. Ensuite, on attribut a chaque noeuds un degre theorique (biais scale_free) '''
        N=0
        res=[-1]*self.nbNodes
        while N<self.nbNodes:
            i=0
            while (i<self.nbNodes-2 and abs(ThDistrib[i]-1)>abs(ThDistrib[i+1])):
                i+=1
            res[N]=ThDegres[i]
            ThDistrib = [t-1 for t in ThDistrib]
            N+=1          
        distri = res

        """ Creation du genome """ 
        self.genome = []
        for i in (range(self.nbNodes)):
            li=[0]*(self.nbNodes-i-1)
            if i != self.nbNodes-1:
                for k in range(distri[i]):
                    li[k]=1
            random.shuffle(li)
            li.insert(0,0)
            self.genome += li



    def fit2distri(self):
        """ Calcul du coefficient de correlation entre distribution theorique et experimentale 
    Compris entre 0 et 1 """

        ThDistrib = [] # Distribution theorique
        
        for x in self.graph.degree().keys():
            if x!=0:
                ThDistrib.append(self.nbNodes*x**(-2.2))
        res = 0      
        for i in range(len(ThDistrib)):
            d = abs(self.graph.degree(i+1) - ThDistrib[i])
            res += d/(d+ThDistrib[i])            

        # TMP
        Deg = self.graph.degree().keys()
        Val = self.graph.degree().values()
        plt.figure()
        plt.plot(Deg[1:],Val[1:],'ro-') #in-degree
        plt.xlabel('Degree')
        plt.ylabel('Number of nodes')
        plt.title('Degree distribution')

        for x in Deg:
                if x!=0:
                        plt.scatter(x,self.nbNodes*x**(-2.2),c="blue")

        plt.savefig('DegreeDistrib.png')
        plt.close()

        # ATTENTION : lorsqu'on converge vers un scale-free: queue de distrib
        # tendant vers 0 : avg_res tend vers 1 !
        return res/self.nbNodes
    



    def clustering(self):
        """ Renvoie le coeff de clustering moyen """
        return nx.average_clustering(self.graph)

    def smallWorld(self):
        """ Renvoie le plus court chemin moyen entre deux noeuds """
        # On vise une valeur de 2.5
        return abs((nx.average_shortest_path_length(self.graph)-2.5)/(nx.average_shortest_path_length(self.graph)))
                                                                  
    def fitness(self,a,b,c):
        return (a*self.fit2distrib() + b*self.clustering() + c*self.smallWorld())/(a+b+c)

    def genome2adj(self):
         """ Remplissage et creation de la matrice d'adjacence """
         Adj = zeros(shape=(self.nbNodes,self.nbNodes))
         i = 0
         N = self.nbNodes

         while i < len(self.genome):
             for j in range(N):
                 Adj[self.nbNodes - N, self.nbNodes - N +j] = Adj[self.nbNodes - N +j,self.nbNodes-N] = self.genome[i+j]
             i+=N
             N-=1

         return Adj

    def drawGraph(self): 
        """ Creation du graphe a partir de la matrice d'adjacence """	
        self.graph = nx.Graph()
        Adj = self.genome2adj()

        for i in range (self.nbNodes):
            self.graph.add_node(i)		# Ajout de tous les noeuds
            for j in range(self.nbNodes):
                if i<j :		# Pour n'ajouter que la partie superieure de la matrice
                    if Adj[i,j]==1:	
                        self.graph.add_edge(i,j)	# Ajout des aretes

        nx.draw(self.graph)
        plt.savefig("Graph.png")


        


G = CGraph(50)
G.drawGraph()
G.fit2distri()
G.clustering()
