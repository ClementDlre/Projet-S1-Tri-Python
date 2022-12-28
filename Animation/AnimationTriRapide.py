import matplotlib.pyplot as plt 
from matplotlib.animation import FuncAnimation 
import matplotlib as mp 
import numpy as np 
import random 
import time

start=time.time()           #start the stopwatch

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

end=time.time()             #stop the stopwatch

def Animation(n):
    list = [random.randint(1,n) for i in range(1, n+1)]       #we create a list from 1 to n+1 (n: length of the list)
    random.shuffle(list)                    #we mix the list
    generator = triRapide(list)              #we create the generator variable with the def triInsertion above which is a generator
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

print(Animation(10000))

