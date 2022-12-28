import matplotlib.pyplot as plt 
from matplotlib.animation import FuncAnimation 
import matplotlib as mp 
import numpy as np 
import random 
import time

start=time.time()           #start the stopwatch

def Empiler(liste1,f):
    liste1.append(f) #We put the e value in the a list and return the list
    return liste1

def estVide(liste2):
    return len(liste2) == 0 #It returns True if the length of p list is null and False if it's not

def Depiler(liste2):
    if (not  estVide(liste2)): #if the length of p list isn't null, we pop the last value of p list and return the list
        return liste2.pop()
        

def EstSommet(liste2):
    if (not estVide(liste2)): #if the length of p list isn't null, we return the last value of p list
        return liste2[len(liste2)-1] 

def InitPile(): #We initialise a list without value in it
    return []

def triPile(liste1):
    liste3 = [] #We initialise a list without value in it
    liste4 = [] #We initialise a list values in it
    while not(estVide(liste4) and estVide(liste1)): #while a list and c list aren't empty

        if estVide(liste1): #if a is empty
            for i in range(len(liste4)): 
                Empiler(liste1, Depiler(liste4)) #we put every values of c in a
            Empiler(liste3, Depiler(liste1)) #and after we put the last value of a in b
        #or
        elif not estVide(liste1): #if a isn't empty

            if estVide(liste3): #and if b is empty
                Empiler(liste3, Depiler(liste1)) #we put the last value of a in b
            #or
            else: #if b isn't empty

                if EstSommet(liste1)>EstSommet(liste3): #and if the last value of a list is superior to the last value of b list
                    Empiler(liste4, Depiler(liste3)) #we put the last value of b in c
                    Empiler(liste3, Depiler(liste1)) #and we put the last value of a in b
                #or
                else: #if the last value of a list isn't superior to the last value of b
                    Empiler(liste4, Depiler(liste1)) #we put the last value of a in c
        yield liste3 #and we return the b list if the wile condition is finish

end=time.time()             #stop the stopwatch

liste1 = InitPile()
Empiler(liste1, 3)
Empiler(liste1, 2)
Empiler(liste1, 4)
liste3 = triPile(liste1)
while not estVide(liste3):
    print(EstSommet(liste3))
    Depiler(liste3)

def Animation(n):
    f = [random.randint(1,n) for i in range(1, n+1)]       #we create a list from 1 to n+1 (n: length of the list)
    random.shuffle(list)                    #we mix the list
    generator = triPile(list)              #we create the generator variable with the def triInsertion above which is a generator
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

    print(end-start)
    plt.show() 

print(Animation(100))