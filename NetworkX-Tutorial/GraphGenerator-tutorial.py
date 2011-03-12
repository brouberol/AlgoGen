import networkx as nx

##############################################################
#####Generateurs de graphe et operations sur les graphes #####
##############################################################

G=nx.Graph()
G.add_path([1,2,3,4])
H=nx.Graph()
H.add_path(["a","b","c","d"])

##### Operateurs #####

""" Union de graphes """
GH=nx.union(G,H)
GH.nodes()
# ['a', 1, 2, 3, 4, 'd', 'c', 'b']
GH.edges()
# [('a', 'b'), (1, 2), (2, 3), (3, 4), ('d', 'c'), ('c', 'b')]

""" Union disjointe de graphes """
#Change les labels en entiers
GH1=nx.disjoint_union(G,H)
GH1.nodes()
GH1.edges()

""" Composition de graphes """
GH2=nx.compose(G,H)
GH2.nodes()
#['a', 1, 'c', 'b', 4, 'd', 2, 3]
GH2.edges()
#[('a', 'b'), (1, 2), ('c', 'b'), ('c', 'd'), (4, 3), (2, 3)]

""" Produit cartesien """
GH3=nx.cartesian_product(G,H)
GH3.nodes()
#[(1, 'c'), (3, 'c'), (1, 'b'), (3, 'b'), (2, 'a'), (3, 'a'), (4, 'd'), (1, 'd'), (2, 'b'), (4, 'b'), (2, 'c'), (4, 'c'), (1, 'a'), (4, 'a'), (2, 'd'), (3, 'd')]
GH3.edges()
#[((1, 'c'), (1, 'd')), ((1, 'c'), (1, 'b')), ((1, 'c'), (2, 'c')), ((3, 'c'), (4, 'c')), ((3, 'c'), (2, 'c')), ((3, 'c'), (3, 'b')), ((3, 'c'), (3, 'd')), ((1,'b'), (1, 'a')), ((1, 'b'), (2, 'b')), ((3, 'b'), (3, 'a')), ((3, 'b'), (2, 'b')), ((3, 'b'), (4, 'b')), ((2, 'a'), (3, 'a')), ((2, 'a'), (1, 'a')), ((2, 'a'),(2, 'b')), ((3, 'a'), (4, 'a')), ((4, 'd'), (4, 'c')), ((4, 'd'), (3, 'd')), ((1, 'd'), (2, 'd')), ((2, 'b'), (2, 'c')), ((4, 'b'), (4, 'c')), ((4, 'b'), (4, 'a')), ((2, 'c'), (2, 'd')), ((2, 'd'), (3, 'd'))]

""" Complement """
#Graphe complementaire
G1=nx.complement(G)
G1.nodes()
G1.edges()

""" Intersection de graphes """
# Les noeuds de H et G doivent etre les memes
H.clear()
H.add_nodes_from([1,2,3,4])
H.add_edge(1,2)
GH4=nx.intersection(G,H)
GH4.nodes()
#[1,2,3,4]
GH4.edges()
#[(1,2)]

""" Difference de graphes """
# Les noeuds de H et G doivent etre les memes
GH5=nx.difference(G,H)
GH5.nodes()
# [1,2,3,4]
GH5.edges()
# [((2,3),(3,4)]
# Retourne un graphe avec des aretes qui existent dans G mais pas dans H

""" Difference symetrique de graphes """
# Les noeuds de H et G doivent etre les memes
GH6=nx.symmetric_difference(G,H)
GH6.nodes()
# [1,2,3,4]
GH6.edges()
# [((2,3),(3,4)]
# Retourne un graphe avec des aretes qui sont soit dans G soit dans H mais pas les deux


##### Graphes classiques #####

petersen=nx.petersen_graph()
petersen.nodes()
#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
petersen.edges()
#[(0, 1), (0, 4), (0, 5), (1, 2), (1, 6), (2, 3), (2, 7), (3, 8), (3, 4), (4, 9), (5, 8), (5, 7), (6, 8), (6, 9), (7, 9)]


tutte=nx.tutte_graph()
tutte.nodes()
tutte.edges()

maze=nx.sedgewick_maze_graph()
maze.nodes()
maze.edges()

tet=nx.tetrahedral_graph()
tet.nodes()
#[0, 1, 2, 3]
tet.edges()
#[(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]

#Remarque : il existe de nombreux generateurs de graphes
