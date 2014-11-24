import pdb
import matplotlib.pyplot as plt
import random
"""
Suppose method MC is running 1000 times and we plot the number of
times it took 1 step, 2 steps, 3 steps, etc.

    Point to a random location in the list. If the ball in that
    location is white, then return 1.

    If it is black, then examine the next item in the list.
    If it is white, return 2, and if it is black,
    continue with the next item in the list.

    Continue examining the items in the list sequentially
    for at most k tries or until a white ball is found.
    If the end of the list is reached, go to the beginning.

    When a white ball is found, return the number of balls
    examined. If no white ball is found after k tries, return 0.
"""

def ballsList(n):
    white_balls = [ 'white' for i in range(1, n) ]
    black_balls = [ 'black' for i in range(1, n) ]
    all_balls = white_balls + black_balls
    random.shuffle(all_balls)
    return all_balls

def MC(numBalls, numTries):
    print "\n-------------------"
    all_balls = ballsList(numBalls)
    print "\nBalls list: ", all_balls

    # randint includes both the first and last number
    random_number = random.randint(0, numBalls - 1)
    result = all_balls[random_number]
    print "\nRandom number: ", random_number, ', Result in list: ', result

    # if the first ball choosen is white, return 1
    if result == 'white':
        return 1

    # if the first ball choosen is black, choose another ball
    else:
        num_balls_examined = 1

        # continue to examine balls until hit numTries,
        # or until a white ball is found
        while num_balls_examined < numTries:
            print 'Inside while loop'
            print "\nRandom number: ", random_number, ', Result in list: ', result
            print '# of balls examined: ', num_balls_examined

            # pdb.set_trace()

            # if the ball choosen was at the end of the list,
            # loop back to the beginning
            if random_number == (numBalls - 1):
                random_number = 0
            else:
                random_number += 1

            # re-calculate the randomly choosen ball
            result = all_balls[random_number]
            num_balls_examined += 1

            if result == 'white':
                return num_balls_examined

        # if no white ball found after hitting numTries, return 0
        return 0


def createHistogram(numTrials, numTries, numBalls = 1000):
    histogram = []
    print "\n-------------------"
    print 'Empty histogram list: ', histogram
    for i in range(numTrials):
        histogram.append(MC(numBalls, numTries))
        print "\nhistogram: ", histogram

    print 'Final histogram: ', histogram
    print "\n-------------------"
    plt.title('Num steps until choose a White Ball')
    plt.hist( histogram )
    plt.show()

createHistogram(10, 5, 5)
