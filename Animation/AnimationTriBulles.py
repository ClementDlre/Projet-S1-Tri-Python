import matplotlib.pyplot as plt 
from matplotlib.animation import FuncAnimation 
import matplotlib as mp 
import numpy as np 
import random 
import time

start=time.time()           #start the stopwatch

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

end=time.time()             #stop the stopwatch

def Animation(n):
    list = [random.randint(1,n) for i in range(1, n+1)]       #we create a list from 1 to n+1 (n: length of the list)
    random.shuffle(list)                    #we mix the list
    generator = triAbulles(list)              #we create the generator variable with the def triInsertion above which is a generator
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

print(Animation(1000))
