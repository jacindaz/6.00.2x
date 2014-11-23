import random, pdb, pylab

"""
Write a procedure called plotQuizzes() that produces a plot of the distribution
of final scores for all of the trials.

    - Your code should make a call to the function generateScores.
    - You should use the same number of trials as you did in Problem 5-1.
"""
def generateScores(numTrials):
    """
    Runs numTrials trials of score-generation for each of
    three exams (Midterm 1, Midterm 2, and Final Exam).
    Generates uniformly distributed scores for each of
    the three exams, then calculates the final score and
    appends it to a list of scores.

    Returns: A list of numTrials final scores.
    """
    final_scores = []

    # run simulation 10k times
    while numTrials:
        # randomly generate midterm1, midterm2, and final grades
        #
        midterm1 = random.randint(50, 80)
        midterm2 = random.randint(60, 90)
        final_exam = random.randint(55, 95)
        # print "\n================="
        # print 'Midterm1: ', midterm1
        # print 'Midterm2: ', midterm2
        # print 'Final exam: ', final_exam

        # calculate final score, final grade 25% midterms, 50% final
        final_score = (midterm1 * .25) + (midterm2 * .25) + (final_exam * .5)
        # print 'Final score: ', final_score

        final_scores.append(final_score)
        numTrials -= 1

        # print "\nFinal scores list: ", final_scores
        # print "=================\n"

    return final_scores

# generateScores(5)


# Please only use the following Pylab functions:
# show, plot, title, xlabel, ylabel, legend, figure, and hist

def plotQuizzes():

    # generate scores, pass in # of trials
    final_scores = generateScores(10000)

    # plot the thing
    pylab.figure(1)
    pylab.xlabel('Final Score')
    pylab.ylabel('Number of Trials')
    pylab.title('Distribution of Scores')
    pylab.legend(loc = 'best')
    pylab.hist(final_scores, bins = 7)
    pylab.show()

plotQuizzes()
