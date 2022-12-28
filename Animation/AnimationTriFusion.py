import matplotlib.pyplot as plt 
from matplotlib.animation import FuncAnimation 
import matplotlib as mp 
import numpy as np 
import random 
import time

plt.style.use('fivethirtyeight') 

n = int(input("Longueur de la liste: ")) 
liste = [i for i in range(1, n+1)] 
random.shuffle(liste) 

debut=time.time()

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

def tri(liste):
    n=len(liste)
    if n<2:
        yield liste
    else:
        m=n//2
        liste=fusion(tri(liste[:m]),tri(liste[m:]))
        yield liste

fin=time.time()


