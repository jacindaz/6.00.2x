import pdb
import matplotlib.pyplot as plt
import random


# returns # of steps taken to randomly draw a white ball
def LV():
    num_steps = 0
    done = False

    while not done:
        ball_drawn = random.choice(['black', 'white'])
        if ball_drawn == 'black':
            num_steps += 1
        else:
            done = True
            
    return num_steps


def createHistogram():
    histogram = []

    for i in range(1000):
        histogram.append(LV())

    plt.title('Num steps until choose a White Ball')
    plt.hist( histogram )
    plt.show()

createHistogram()
