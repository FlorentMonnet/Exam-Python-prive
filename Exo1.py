# -*- coding: utf-8 -*-
#On définie f donct il faudra calculer l'intégrale
def f(x):
    return x
#On définit integ_rumberg, je n'ai pas uitilisé epsilon mais le nombre d'intervalle
def  integ_romberg(f, a, b,nbInter=30):
    #On a donc h =(b-a)/nbInter
    h=(b-a)/nbInter
    #result h * f(a)+f(ab)/2
    result=h*(f(a)+f(b))/2
    somme=0
    #somme de 1 à nbInter, qui ajoute f(a+i*h)
    for i in range(nbInter):
        somme+=f(a+i*h)
    #resultat final = h * f(a)+f(ab)/2 + la somme précédente * h
    return result +somme*h
#Pn affiche le résultat de l'intégrale de f de 0 à 1
print(integ_romberg(f,0,1))
