from optparse import TitledHelpFormatter
from turtle import color
import matplotlib.pyplot as plt 
from matplotlib.animation import FuncAnimation 
import matplotlib as mp 
import numpy as np 
import random 
import time

#TRI INSERTION

def triInsertion(liste): 
    for i in range(1, len(liste)):               
        key=liste[i]                             
        j=i                                   
        while j>=0 and liste[j-1]>key:            
            liste[j]=liste[j-1]                   
            j-=1                                
        liste[j] =key                          
    return liste

#TRI SELECTION

def triSelection(liste):
    for i in range(len(liste)):
        minimum=i
        for j in range(i+1,len(liste)):
            if liste[minimum]>liste[j]:
                minimum=j
        Temp = liste[i]
        liste[i] = liste[minimum]
        liste[minimum] = Temp
    return liste

#TRI A BULLES

def triAbulles(liste):
    for i in range(len(liste)):
        for j in range(0, len(liste)-i-1):
            if liste[j]>liste[j+1]:
                Temp=liste[j]
                liste[j]=liste[j+1]
                liste[j+1]=Temp
    return liste

#TRI FUSION

def fusion(liste1,liste2):
    i1=0
    i2=0
    n1=len(liste1)
    n2=len(liste2)
    liste=[]
    while i1<n1 and i2<n2:
        if liste1[i1]<liste2[i2]:
            liste.append(liste1[i1])
            i1+=1
        else:
            liste.append(liste2[i2])
            i2+=1
    if i1==n1:
        liste.extend(liste2[i2:])
    else:
        liste.extend(liste1[i1:])
    return liste

def triFusion(liste):
    n=len(liste)
    if n<2:
        yield liste
    else:
        m=n//2
        return fusion(triFusion(liste[:m]),triFusion(liste[m:]))

#TRI RAPIDE

def triRapide(list):
    if not list or len(list)==0:
        return []
    gauche=[]
    droite=[]
    for i in list:                                  
        if i<list[-1]:
            gauche.append(i)
        elif i>= list[-1]:
            droite.append(i)
    return sorted(gauche) + sorted(droite)


#COMPARAISON

listeTemps=[]

def ComparaisonTemps(n,def1,def2,def3,def4,def5):
    list = [random.randint(1,n) for i in range(1, n+1)]       
    random.shuffle(list)
    
    start1=time.time()
    def1(list)
    end1=time.time()
    temps1=end1-start1
    listeTemps.append(temps1)

    start2=time.time()
    def2(list)
    end2=time.time()
    temps2=end2-start2
    listeTemps.append(temps2)

    start3=time.time()
    def3(list)
    end3=time.time()
    temps3=end3-start3
    listeTemps.append(temps3)

    start4=time.time()
    def4(list)
    end4=time.time()
    temps4=end4-start4
    listeTemps.append(temps4)

    start5=time.time()
    def5(list)
    end5=time.time()
    temps5=end5-start5
    listeTemps.append(temps5)

    return listeTemps



def ComparaisonsGraphiquesTempsReels(n):
    fig = plt.figure()
    width = 0.5
    listeCouleurs=['b','r','g','c','m']
    listeAlgorithme=['Tri Insetion', 'Tri Selection', 'Tri A Bulles', 'Tri Fusion', 'Tri Rapide']
    ComparaisonTemps(n,triInsertion,triSelection,triAbulles,triFusion,triRapide)
    for i in range(5):
        plt.bar(listeAlgorithme[i], listeTemps[i], width, color=listeCouleurs[i] )
    plt.show()

print(ComparaisonsGraphiquesTempsReels(1000))




def ComparaisonsGraphiquesJeuDeTests():
    JeuDeTests=[5000,10000,20000,30000,50000,70000,100000]
    listeTempsInsertion=[0.66,2.69,11.32,26.44,80.3,193.2,390.58]
    listeTempsSelection=[0.56,2.50,9.88,22.66,71.87,178.05,405.52]
    listeTempsBulles=[0.77,3.33,13.75,32.12,99.85,282.5,550.69]
    listeTempsFusion=[5.48*(10**-6),5.97*(10**-6),6.32*(10**-6),9.78*(10**-6),5.48*(10**-6),6.68*(10**-6),8.34*(10**-6)]
    listeTempsRapide=[3.58*(10**-6),3.34*(10**-6),3.15*(10**-6),1.90*(10**-6),2.01*(10**-6),2.15*(10**-6),2.48*(10**-6)]
    for i in range(5):
        plt.plot(JeuDeTests[i],listeTempsInsertion[i],'bo')
        plt.plot(JeuDeTests[i],listeTempsSelection[i],'ro')
        plt.plot(JeuDeTests[i],listeTempsBulles[i],'go')
        plt.plot(JeuDeTests[i],listeTempsFusion[i],'co')
        plt.plot(JeuDeTests[i],listeTempsRapide[i],'mo')
    plt.legend()
    plt.xlabel("Valeur de la liste")
    plt.ylabel("Temps en seconde")
    plt.xlim(0,60000)
    plt.ylim(-1,200)
    plt.show()

print(ComparaisonsGraphiquesJeuDeTests())