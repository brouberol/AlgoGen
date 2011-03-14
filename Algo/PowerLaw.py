from numpy import *
import pylab as p

"""
The goal is to plot the extreme power laws for biological networks
defined by 2 <= gamma <= 3.
Encountered power laws should be plotted within the area determined 
by the 2 curves.
"""

# Constants
NB_POINTS = 30
MIN = 1
MAX = 10
X = linspace(MIN,MAX,NB_POINTS) # x from MIN to MAX with NB_POINTS points
LAW_COLOR=["orange","green","red"]


# Functions 
def PowerLaw(gamma):
    """ Generates a power law distribution """
    return [10*x**(-gamma) for x in X]# coeff : deg max ?


def GammaRange():
    """ Range from 2 to 3. 
    Corresponds to biological networks """
    return arange(2,3.1,1)

def Legend(gamma):
    """ Generates the legend string with the gamma values """
    s=[]
    for g in gamma:
        s.append("gamma = "+str(g))
    return s

def PlotLimitPowerLaw(Degree):
    """ Plots power laws for all gammas in GammaRange() """
    col = 0
    
    for g in GammaRange():
        Law = PowerLaw(g)
        if len(Law) == len(X):
            p.plot(X,Law,'--',c=LAW_COLOR[col])
        else:
            print 'Size incoherency'
        col+=1
    
    # Basic plot features
    p.title("Extreme power laws for biological networks")
    p.xlabel("x")
    p.ylabel("Power law : x**-gamma")
    p.grid()
    
    # Add the node degree distribution
    AddDegreeLaw(Degree,col)
    
    # Final plot features
    l = Legend(GammaRange())
    p.legend((l[0],l[1],"Degree distribution"),'upper right')
    p.savefig("Plot.png")
    p.close()

def AddDegreeLaw(DegreeDistrib,col):
    """ Add the node degree distribution on the power laws plot """
    # DegreeDistrib = [(NbNodes, deg),(...)]
    x = [DegreeDistrib[i][0] for i in range(len(DegreeDistrib))]
    y = [DegreeDistrib[i][1] for i in range(len(DegreeDistrib))]
    p.scatter(x,y,c=LAW_COLOR[col])

    
# MAIN

Deg = [(1,10),(2,2),(3,1),(4,1)] # artificial list of degrees and nb of nodes
PlotLimitPowerLaw(Deg)
