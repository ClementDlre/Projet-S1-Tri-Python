import matplotlib.pyplot as plt 
from matplotlib.animation import FuncAnimation 
import matplotlib as mp 
import numpy as np 
import random 
import time

start=time.time()           #start the stopwatch

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

end=time.time()             #stop the stopwatch

def Animation(n):
    list = [random.randint(1,n) for i in range(1, n+1)]       #we create a list from 1 to n+1 (n: length of the list)
    random.shuffle(list)                    #we mix the list
    generator = triSelection(list)              #we create the generator variable with the def triSelection above which is a generator
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
print(end-start)

print(Animation(100))