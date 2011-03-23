import networkx as nx
from numpy import *
import matplotlib.pyplot as plt


size=10

""" Creation de la matrice de la matrice d'adjacence"""
A = zeros(shape=(size,size))

""" Remplissage """
for i in (range(size)):
	for j in range(size):
		if i==j : 	#Pour mettre 0 sur la diag
			A[i,j]=0
		else :	A[i,j] = A[j,i] = random.randint(0,2)

""" Creation du graphe a partir de la matrice d'adjacence """	
G=nx.Graph()

for i in range (size):
	G.add_node(i)		#Ajout de tous les noeuds
	for j in range(size):
		if i<j :		#Pour n'ajouter que la partie superieure de la matrice
			if A[i,j]==1:	
				G.add_edge(i,j)	#Ajout des aretes
	
nx.draw(G)
plt.savefig("Graph.png")

""" Calcul des parametres du reseau """
Val = G.degree().values()
Deg = [x[0] for x in G.degree_iter()]

plt.figure()
plt.plot(Deg,Val,'ro-') # in-degree
plt.xlabel('Degree')
plt.ylabel('Number of nodes')
plt.title('Degree distribution')
plt.savefig('DegreeDistrib.png')
plt.close()


