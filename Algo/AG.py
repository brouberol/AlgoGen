# -*- coding: utf-8 -*-
from numpy import *
from math import *


#Classe Test
class pyRW :
    
    def __init__(self,T,gen=None):

        if gen is not None:
            self.genome = gen[:]
            self.T = len(gen)
            #print self.genome
        else:
            self.T = T
            self.genome = random.randint(0,2,WALKTIME) #Sup value exluded

    def Fitness(self,t,r):
    #Renvoie la fitness d'un individu
        Fit, X = 0, 0
        for i in self.genome[t:]:
            X += 2*i-1
            if abs(X) > r:
                Fit += 1
        return Fit

#Veritable algorithme génétique            
class pyAG :
    
    def __init__(self,N,Mut,Cross,T,r,t):
        self.N = N
        self.MutRate = Mut
        self.CrossOver = Cross
        self.T = T
        self.r = r
        self.t = t

    def CreatePop(self):
        #Crée une population d'individus pyRW
        self.Pop = []
        for i in range(self.N):
            self.Pop.append(pyRW(self.T))
        return self.Pop

    def CalcFitness(self):
        #Renvoie une liste (triée par fitness) des fitness des individus de la population
        self.Fit = []
        for individu in self.Pop:
            self.Fit.append((individu.Fitness(self.r, self.t),self.Pop.index(individu)))
        self.Fit.sort()
        return self.Fit
    
    def FitMin(self):
        self.FitMin = self.Fit[0][0]
        return self.FitMin
    
    def FitMean(self):
        S = 0
        for i in self.Fit:
            S += i[0]
        self.FitMean = S/len(self.Fit)
        return self.FitMean
    
    def Rank(self, p):
        i,s = 0, 0
        while s < p:
            s+= self.N-i
            i += 1
        #retourne le rang de l'individu à la position p
        return i

    def Newpop(self):
        self.newpop = []
        Fit = self.CalcFitness()
        for i in range(self.N):
            p = random.randint(0,(self.N*(self.N+1))/2)
            i = self.Rank(p)
            s = self.Pop[Fit[i][1]].genome
            self.newpop.append(pyRW(self.T,gen=s))
        
    def Mutation(self):
        for indiv in self.newpop:
            gen = indiv.genome
            for i in range(len(gen)):
                if random.random() < self.MutRate:
                    gen[i] = 1 - gen[i] #Mutation : si 1 -> 1 -1 = 0, si O-> 1-0 = 1
                
    def CrossingOver(self):
        for i in self.newpop:
            if random.random() < self.CrossOver:
                gen = i.genome
                target = self.newpop[random.randint(0,self.N-1)].genome
                lim = random.randint(1,len(gen)-1)
                if random.random() < 0.5:
                    #Quelle partie du génome a partir de la limite ?
                    gen[0:lim] = target[0:lim]
                else:
                    gen[lim:] = target[lim:]
                i.genome = gen
                    
    def Update(self):
        self.Pop = self.newpop[:]

    def Loop(self):
	self.CalcFitness()
	self.Newpop()
	self.Mutation()
	self.CrossingOver()
	self.Update()
        self.FitMean()
        self.FitMin()
        print "Minimal Fitness : {0}\nMean Fitness    : {1}".format(self.FitMin, self.FitMean)
        
                                 
#MAIN
WALKTIME = 30 #Longueur du génome
#param de fenetres
t0 = 2
r0 = 3

#taux
Mut = 0.3
CrossOver = 0.4

#----------#

Test = pyAG(2,Mut,CrossOver,WALKTIME,r0,t0)
Test.CreatePop()
Test.Loop()

#Il faut maintenant utiliser l'algo sur plusieurs generations
