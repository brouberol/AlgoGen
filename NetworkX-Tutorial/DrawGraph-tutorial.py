import networkx as nx
import matplotlib.pyplot as plt
# La librarie matplotlib est incluse dans la librarie pylab
# Pour linux : sudo apt-get install python-pylab
# Pour windows : telecharger les sources depuis http://sourceforge.net/projects/matplotlib/files/matplotlib/matplotlib-1.0.1/

 
G=nx.Graph()
G.add_nodes_from(range(1,10))

# plt.show() # ATTENTION : Ne fonctionne qu'en interactif (mode console)

nx.draw(G)
plt.savefig("path.png")
