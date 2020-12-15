# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 10:06:51 2020

@author: monnetf
"""
import numpy as np
import math
class Ville:
    #On initialise aucune destination
    def __init__(self):
        self.destination=[]
    
    def getDestination(self):
        return self.destination
    
    def setDestination(self,Xa,Ya):
        self.destination=np.append(self.destination,[[Xa,Ya]])
    
    def aleatoire(self,n):
        #On parcoure notre boucle grace au nombre fournis par l'utilisateur
        for i in range(n):
            self.destination=np.append(self.destination, [[np.random.randint(50),np.random.randint(50)]],axis = 0)
    def nb_trajet(self):
        #On recupere le nombre de valeurs dans destination puis on divise par 2 pour avoir le nombre de destination
        n = self.destination.size/2
        #On retourne (n-1)!/2
        return math.factorial(n-1)/2
    def distance(self,i,j):
        #On retourne la distance manathan comme dans m'énoncé
        return abs(i[1]-i[0])+abs(j[1]-j[0])
#On créé une ville avec 4 destinations            
ville=Ville()
ville.aleatoire(4)
print(ville.distance([4,2],(1,1)))
#On affiche le nombre de trajet de la ville
print(ville.nb_trajet())
print(ville.getDestination())
