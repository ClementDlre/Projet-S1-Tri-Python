import matplotlib.pyplot as plt 
from matplotlib.animation import FuncAnimation 
import matplotlib as mp 
import numpy as np 
import random 
import time

######  Tri Insertion  ######

def triInsertion(list): 
    """
    The purpose of this function is to sort the list by the Insert Sort method
    arg: the list to sort, type= list
    return: the shorted list, type: list
    """
    for i in range(1, len(list)):               #we make a loop going through the entire list
        key=list[i]                             #define the key variable by assigning it the value of the list with index i
        j=i-1                                   #j is defined as i-1
        while(j>=0 and list[j]>key):            #we create a loop that reverses 2 values if the value j+1 is smaller than the value j
            list[j+1]=list[j]                   
            j-=1                                
        list[j+1] =key                          
        yield list                              

###### Tri Selection ######

def triSelection(liste):
    """
    This function allows you to sort a list by the selection method
    arg: the list to sort, type= list
    return: the shorted list, type: list
    """
    for i in range(len(liste)):                                 #we go through the list entirely
        minimum=i                                               #the minimum is defined     
        for j in range(i+1,len(liste)):                         #we’re going through the list
            if liste[minimum]>liste[j]:                         #if the minimum value is greater than the value j, the minimum shall be changed to i
                minimum=j
        liste[i], liste[minimum] = liste[minimum],liste[i]      #change the values i and minimum
        yield liste

###### Tri A Bulles ######

def triAbulles(liste):
    """
    This function allows you to sort a list using the bubble sorting method
    arg: the list to sort, type= list
    return: the shorted list, type: list
    """
    for i in range(len(liste)):                         #we go through the list entirely
        for j in range(0, len(liste)-i-1):              #We go through the list of 0 at the end of the list minus i minus 1, that is to say, that at each passage of the loop, it stops 1 notch earlier
            if liste[j]>liste[j+1]:
                Temp=liste[j]
                liste[j]=liste[j+1]
                liste[j+1]=Temp
        yield liste

###### Tri Rapide ######

def triRapide(list):
    """
    The purpose of this function is to sort the list by the quicksort method
    arg: the list to sort, type= list
    return: the shorted list, type: list
    """
    if not list or len(list)==0:
        return []
    gauche=[]
    droite=[]
    for i in list:                                  #we analyze the list from the middle and separate the elements into two groups that we merge at the end
        if i<list[-1]:
            gauche.append(i)
        elif i>= list[-1]:
            droite.append(i)
    yield sorted(gauche) + sorted(droite)


###### Animation ######

def Animation(n,tri):
    list = [random.randint(1,n) for i in range(1, n+1)]       #we create a list from 1 to n+1 (n: length of the list)
    random.shuffle(list)                    #we mix the list
    generator = tri(list)              #we create the generator variable with the def triInsertion above which is a generator
    fig, ax = plt.subplots()                #we collect figures and objects
    rects = ax.bar(range(len(list)), list, align="edge")    #we define bars that will be displayed next to each other, aligned. In addition, there will be as many bars as the size of the list and also each bar assigned to a number will have as size this number      #
    ax.set_xlim(0, len(list)) 
    ax.set_ylim(0, int(1.1*len(list))) 
    text = ax.text(0.01, 0.95, "", transform=ax.transAxes)      #we put the graduation on the axes
    iteration = [0]             #we set the iteration variable to 0 and it will allow us to count the number of iterations

    def animate(A, rects, iteration):             #this definition allows us to animate the program
        for rect, val in zip(rects, A): 
            rect.set_height(val)                  #change the height of the bars
        iteration[0] += 1                         #the counter is increased by 1 each time the animation changes
        text.set_text("iterations : {}".format(iteration[0]))               #the iteration counter is displayed

    anim = FuncAnimation(fig, func=animate, fargs=(rects, iteration), frames=generator, interval=50, repeat=False) #animation start

    plt.show() 

print(Animation(100,triInsertion))
print(Animation(100,triSelection))
print(Animation(100,triAbulles))
print(Animation(100,triRapide))