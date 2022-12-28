from optparse import TitledHelpFormatter
import matplotlib.pyplot as plt 
from matplotlib.animation import FuncAnimation 
import matplotlib as mp 
import numpy as np 
import random 


n=50
list = [random.randint(1,n) for i in range(1, n+1)]       #we create a list from 1 to n+1 (n: length of the list)
random.shuffle(list) 

#Tri par insertion 

def triInsertion(liste):
    """
    The purpose of this function is to sort the list by the Insert Sort method
    arg: the list to sort, type= list
    return: the shorted list, type: list
    """
    for i in range(1,len(liste)):               #we make a loop going through the entire list
        N=liste[i]                              #define the key variable by assigning it the value of the list with index i
        j=i                                     #j is defined as i-1
        while j>0 and liste[j-1]>N:             #we create a loop that reverses 2 values if the value j+1 is smaller than the value j
            liste[j]=liste[j-1]
            j=j-1
        liste[j]=N
    return liste


#Tri par sélection

def triSelection(liste):
    """
    This function allows you to sort a list by the selection method
    arg: the list to sort, type= list
    return: the shorted list, type: list
    """
    for i in range(len(liste)):             #we go through the list entirely
        minimum=i                           #the minimum is defined   
        for j in range(i+1,len(liste)):     #we’re going through the list
            if liste[minimum]>liste[j]:     #if the minimum value is greater than the value j, the minimum shall be changed to i
                minimum=j
        Temp = liste[i]
        liste[i] = liste[minimum]
        liste[minimum] = Temp               #change the values i and minimum
    return liste

#Tri à bulles

def triAbulles(liste):
    """
    This function allows you to sort a list using the bubble sorting method
    arg: the list to sort, type= list
    return: the shorted list, type: list
    """
    for i in range(len(liste)):                 #we go through the list entirely
        for j in range(0, len(liste)-i-1):      #We go through the list of 0 at the end of the list minus i minus 1, that is to say, that at each passage of the loop, it stops 1 notch earlier
            if liste[j]>liste[j+1]:
                Temp=liste[j]
                liste[j]=liste[j+1]
                liste[j+1]=Temp
    return liste

#Tri Fusion
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
        return liste
    else:
        m=n//2
        return fusion(triFusion(liste[:m]),triFusion(liste[m:]))



#Tri Rapide

def triRapide(list):
    """
    The purpose of this function is to sort the list by the quicksort method
    arg: the list to sort, type= list
    return: the shorted list, type: list
    """
    if not list:                #if it is not a list return an empty list
        return []
    else:
        k = list[-1]            #k becomes the pivot
        minimum = [x for x in list if x <  k]            #the list is divided into 2: values below the pivot and values above the pivot        
        maximum = [x for x in list[:-1] if x >= k]
        return triRapide(minimum) + [k] + triRapide(maximum) #we carry out the instruction if on until we have the list sort

print(triInsertion(list))
print(triSelection(list))
print(triAbulles(list))
print(triFusion(list))
print(triRapide(list))