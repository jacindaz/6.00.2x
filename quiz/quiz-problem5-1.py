import random, pdb

"""
You are taking a class that plans to assign final grades based on two midterm
quizzes and a final exam. The final grade will be based on 25% for each midterm,
and 50% for the final. You are told that the grades on the exams were each
uniformly distributed integers:

    Midterm 1: 50 <= grade <= 80
    Midterm 2: 60 <= grade <= 90
    Final Exam: 55 <= grade <= 95

Write a function called sampleQuizzes() that implements a Monte Carlo simulation
that estimates the probability of a student having a final score >= 70 and <= 75.
Assume that 10,000 trials are sufficient to provide an accurate answer.
"""

def classGrades(numTrials, target_score_min, target_score_max):
    target_final_score_count = 0

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
        # print "=================\n"

        # if the final score is between 70-75, increment the count
        if target_score_min <= final_score <= target_score_max:
            target_final_score_count += 1
            # print "\nNew final score count: ", target_final_score_count

        numTrials -= 1

    return target_final_score_count


def calcProb(sum, N):
    # figure out probability of final score btwn 70 - 75
    return sum / float(N)


def sampleQuizzes():
    N = 9999
    min_score = 70
    max_score = 75
    count_target_score = classGrades(N, min_score, max_score)
    final_probability = calcProb(count_target_score, N)

    print "\nCount for number of times hit the target score: ", count_target_score
    print 'Probability of getting the target score: ', final_probability

    return final_probability


# correct output is 0.2498
sampleQuizzes()
