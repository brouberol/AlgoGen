import networkx as nx

print "#####################"
print "##### DIGRAPHES #####"
print "#####################"
# Graphes orientes
print(H.nodes())
print(H.edges())

# Un digraphe possede les memes attributs et methode que les graphes.
# Il existe des methodes speciales pour les graphes orientes

""" Creation du digraphe """
DG=nx.DiGraph()

""" Ajout d'aretes et de noeuds """
DG.add_weighted_edges_from([(1,2,0.5), (3,1,0.75)])

""" Aretes """
DG.out_edges(1)
# Retourne les aretes sortantes

DG.in_edges(1)
# Retourne les aretes entrantes

# Les iterateurs correspondants existent 
DG.out_edges_iter()
DG.in_edges_iter()


"""Nombre d'aretes partant d'un noeud """
DG.out_degree(1)
# 1
# Marche avec plusieurs noeuds
DG.out_degree([1,2])
# {1: 1, 2: 0}

DG.out_degree(1,weighted=True)
# 0.5
# Donne la somme des ponderations des aretes partant d'un noeud

""" Nombre d'aretes pointant sur un noeud """
DG.in_degree(1)
# 1
DG.in_degree([1,2])
# {1: 1, 2: 1}
list(DG.in_degree([1,2]).values())
# [1, 1]

DG.in_degree(1,weighted=True)
# 0.75
# Donne la somme des ponderations des aretes pointant sur un noeud


##### Noeuds #####

""" Noeuds relies par une arete partant d'un noeud """
DG.predecessors(1)
# [3]

""" Noeuds relies par une arete pointant sur un noeud""" 
DG.successors(1)
# [2]
# Equivalent a 
DG.neighbors(1)

# Les iterateurs correspondants existent
DG.predecessors_iter(1)
DG.successors_iter(1)


##### Copies #####

#En plus des methodes de copies pour les graphes, il existe : 
GD=DG.reverse()
