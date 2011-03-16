import networkx as nx

print "###################"
print "##### GRAPHES #####"
print "###################"

""" Creation d'un graphe """
G=nx.Graph() # Graphe vide


""" Ajout de Noeuds """
G.nodes() # Print les noeuds sous forme de liste
#[]

# Ajouter un seul noeud 
# Un noeud peut etre n'importe quel objet python
G.add_node(1) # Va ajouter le noeud 1

print(G.nodes())

G.add_node("spam") # Va ajouter le noeud "spam"
print(G.nodes())

# Ajouter une liste de noeuds
G.add_nodes_from([2,3]) # Ajoute les noeud 2 et 3
print(G.nodes())

G.add_nodes_from("spam") # Ajoute les noeuds 's' 'p' 'a' 'm'


H=nx.Graph()
H.add_nodes_from(range(100,110))# Ajoute les noeuds de 100 a 109


G.add_nodes_from(H) # Ajoute (uniquement) les noeuds de H a G 

# Equivalent a
G.add_nodes_from(H.nodes())
print(G.nodes())

G.add_node(H)
#Ajoute H comme noeud a G 
print(G.nodes())


print "\n##################"
print "##### Aretes #####"
print "##################"

print(G.edges()) # Print les aretes sous forme de liste
#[]


""" Ajouter une arete """
G.add_edge(1,2)
print(G.edges())
# Si les noeuds n'existent pas ils seront crees

e=(2,3)
G.add_edge(*e) # ATTENTION tuple*

print(G.edges())

""" Ajouter une liste d'aretes à partir d'une liste """

G.add_edges_from([(1,2),(1,3)])
print(G.edges())

e = zip(range(0,3),range(1,4))
H.add_edges_from(e)

G.add_edges_from(H.edges())
#Ajoute les aretes de H a G
print(G.edges())

## Ajouter une liste d'aretes ponderees
G.add_weighted_edges_from([(0,1,3.0),(1,2,7.5)])
print(G.edges())

#[(0,1),(1,2)]
#Pour afficher les attributs
print(G.edges(data=True))
#[(0, 1, {'weight': 3.0}), (1, 2, ('weight': 7.5})]


""" Creation d'un graphe a partir d'une liste d'aretes """
edgelist=[(0,1),(1,2),(2,3)]
h=nx.Graph(edgelist)

""" Creation d'une "etoile" """
G1 = nx.Graph()   
G1.add_star([0,1,2,3])
#Le premier noeud indique sera le centre de l'etoile, il sera relie a tous les autres par une arete
print(G1.edges())
#[(0,1),(0,2),(0,3)]

""" Creation d'un chemin """
G2=nx.Graph()  
G2.add_path([0,1,2,3])
#Va cree un chemin du noeud 0 au noeud 3
print (G2.edges())
#[(0,1),(1,2),(2,3)]

""" Creation d'un cycle """
G3=nx.Graph()  
G3.add_cycle([0,1,2,3])
print(G3.edges())
#[(0,1),(0,3),(1,2),(2,3)]


print "\n############################"
print "## Destruction d'un graphe ##"
print "#############################"


""" Retirer un noeud """

G.remove_node(H)
# On retire H en tant que noeud de G (et les aretes associees)
print(G.nodes())
print(G.edges())

G.remove_nodes_from(H)
# Equivalent a
G.remove_nodes_from(H.nodes()) # Retire tous les noeuds de H inclus dans G (ainsi que les aretes lies a ses noeuds)



""" Retirer une arete """
# Remise des aretes pour pouvoir les enlever
G.add_edges_from(H.edges())

G.remove_edge(2,3)
print(G.edges())

G.remove_edges_from(H.edges()) # Retire toutes les aretes de H inclues dans G (mais pas les noeuds)


""" Supprimer tous les noeuds et toutes les aretes """
G.clear() # Supprime tous les noeuds et toutes les aretes du graphe, mais G existe toujours


""" Differentes methodes """
G=nx.Graph()
G.add_weighted_edges_from([(0,1,3.0),(1,2,7.5)])

print "\n####################"
print "##### Attributs #####"
print "#####################"

# On peut ajouter des ponderations, des label, des couleurs ou n'importe quel objet python a un graphe, a des noeuds ou a des aretes


""" Graphes """
# En creant le graphe : 
G1 = nx.Graph(day="Friday")
print(G1.graph)

#Ou plus tard : 
G1.graph['day']='Monday'
print(G1.graph)

""" Noeuds """
# Avec add_node et add_nodes_from
# On ajoute un attribut time aux noeuds

G.add_node(1, time='5pm')
G.add_nodes_from([3], time='2pm')

print(G.node[1])
#{'time': '5pm'}

# Avec [] directement 
G.node[1]['room'] = 714
print(G.nodes(data=True))
# [(0, {}), (1, {'room': 714, 'time': '5pm'}), (2, {}), (3, {'time': '2pm'})]


""" Aretes """
# Pour recuperer les attributs d'une arete (dictionnaire)
G.get_edge_data(0,1)
# {'weight' : 3.0}

# Equivalent
G[1][2]
# {'weight' : 3.0}

# Avec add_ege et add_edges_from

G.add_edge(1, 2, weight=4.7 )
G.add_edges_from([(3,4),(4,5)], color='red')
G.add_edges_from([(1,2,{'color':'blue'}), (2,3,{'weight':8})])
print(G.edges(data=True))

#Avec [][]
G[1][2]['weight'] = 4.7
G.edge[1][2]['weight'] = 4
#Remplace les valeurs deja rentrees
print(G.edges(data=True))

#Remarque : l'attribut weight doit etre numerique


""" Voisins d'un noeud """
# Pour recuperer les noeuds relies a un noeud
G.neighbors(1)
#[0,2]

# Pour recuperer les noeuds relies a un noeud avec leurs attributs
G.__getitem__(1)
# Operateur crochet
G[1]
# {0: {'weight': 3.0}, 2: {'weight': 7.5}}
# Renvoi un dictionnaire avec en cles le deuxieme noeud des aretes commencant par 1 et avec en valeurs les attributs


#Pour recuperer une liste d'adjacence
G.adjacency_list()


""" Iterateurs """
# Renvoie un iterateur des noeuds
G.nodes_iter()

# Iterateur des noeuds
G.__iter__()
#for n in G

# Renvoi un iterateur des aretes 
G.edges_iter()
#exemples
[e for e in G.edges_iter()]
#Retourne la liste des aretes
#[(0, 1), (1, 2)]

list(G.edges_iter(data=True)) 
# Retourne la liste des aretes avec en plus le data, qui est un dictionnaire, vide par defaut {}
# [(0, 1, {'weight':3.0}), (1, 2, {'weight':7.5})]

list(G.edges_iter(0))
# Retourne une liste des aretes dont le premier noeud est 0
# [(0, 1)]

list(G.edges_iter([0,3]))
# Retourne la liste des aretes dont le premier noeud est compris dans la liste [0,3]
# [(0, 1)]

# Renvoie un iterateur des voisins d'un noeud
G.neighbors_iter(1)

# Renvoie un iterateur sur la liste d'adjacence ??
G.adjacency_iter()

""" Boolean """
G.has_node(1)
# Retourne True si le graphe contient le noeud "1"

G.__contains__(1)
# Retourne True si 1 est un noeud, False sinon, s'utilise :
1 in G

G.has_edge(0,1)
# Retourne True si le graphe contient l'arete

""" Nombre de noeuds dans le graphe """
G.order()
# equivalent : 
G.number_of_nodes()
#equivalent
len(G)

""" Degre d'un noeud """
G.degree(1)

G.degree()
# Retourne tous les noeuds et leur degre

# Iterateur associe
G.degree_iter()

G.degree(1,weighted=True)
# Si weighted est True, retourne la somme des ponderation des aretes adjacentes au noeud


""" Nombre d'aretes """
G.size()
# Equivalent :
G.number_of_edges()

G.size(weighted=True)
# Retourne la somme des ponderations des aretes

""" selfloop """
G.nodes_with_selfloops()
#Retourne les noeuds qui ont une selfloop 

G.selfloop_edges()
#Retourne les aretes selfloop

G.number_of_selfloops()
#Retourne le nombre de selfloop

print '\n##############################'
print "##### Copies d'un graphe #####"
print '##############################'

""" Copie simple d'un graphe """
G1=G.copy()

""" Copie d'un digraphe vers un graphe """
G2=G.to_undirected()
# Equivalent a 
G2=nx.Graph(G)

""" Copie d'un graphe vers un digraphe	"""
G3=G.to_directed()	
# Equivalent a
G3=nx.DiGraph(G)

""" Creation d'un sous graphe, avec en argument une liste de noeuds """
G4=G.subgraph([1,2])
# Va copier les noeuds et les aretes entre ces noeuds et les selfloop

""" DESTRUCTION DES GRAPHES """
G.clear()
G1.clear()
G2.clear()
G3.clear()
G4.clear()
H.clear()


print "\n###################"
print "##### Exemple #####"
print "###################"

# Creation d'un graphe
FG=nx.Graph()
# Ponderation
FG.add_weighted_edges_from([(1,2,0.125),(1,3,0.75),(2,4,1.2),(3,4,0.375)])

for n,nbrs in FG.adjacency_iter():
	# print(n) # tous les noeuds
	# print(nbrs) # les dictionnaires associes contenant en cle les noeuds des aretes commencant pat n, en valeur les ponderation
	# print nbrs.items()
	for nbr,eattr in nbrs.items():
		# print(nbr) # les cles
		# print(eattr) # les valeurs
		data=eattr['weight'] #On met les ponderations dans data
		# On print si la ponderation est >0.5
		if data<0.5: print('(%d, %d, %.3f)' % (n,nbr,data))

# Remarque : Pour les graphes non orientes chaque arete sort 2 fois
