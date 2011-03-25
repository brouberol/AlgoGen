import networkx as nx
from numpy import *
import matplotlib.pyplot as plt

""" 
On teste ici la distribution experimentale d'un scale-free
cree avec networx
""" 

NBPOINTS = 75

""" Scale free network generating """
G = nx.scale_free_graph(NBPOINTS)
D =  G.degree()
D.pop(0) # On retire les points de degre 0 pour le plot
Val = D.values()
Deg = D.keys()

""" Experimental degree distribution plot"""
plt.figure()
plt.grid()
plt.plot(Deg,Val,'ro-')
plt.xlabel('Degree')
plt.ylabel('Number of nodes')
plt.title('Degree distribution of a scale free network\n Gamma = 2.2')

""" Theoretical degree distribution plot """
for x in Deg:
	plt.scatter(x,NBPOINTS*x**(-2.2),c="blue")

""" Plot features """
plt.legend(["Experimental","Theoretical"])
plt.savefig('DegreeDistrib.png')
plt.close()
