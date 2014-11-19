import numpy
import random
import pylab
import pdb
from ps3b_precompiled_27 import *

# PROBLEM 3
#
def simulationWithoutDrug(numViruses, maxPop, maxBirthProb, clearProb,
                          numTrials):
    """
    Run the simulation and plot the graph for problem 3 (no drugs are used,
    viruses do not have any drug resistance).
    For each of numTrials trial, instantiates a patient, runs a simulation
    for 300 timesteps, and plots the average virus population size as a
    function of time.

    numViruses: number of SimpleVirus to create for patient (an integer)
    maxPop: maximum virus population for patient (an integer)
    maxBirthProb: Maximum reproduction probability (a float between 0-1)
    clearProb: Maximum clearance probability (a float between 0-1)
    numTrials: number of simulation runs to execute (an integer)
    """
    print 'Num trials: ', numTrials
    num_viruses_list = createEmptyList(300)
    print "\nList of zeroes for virus count: ", num_viruses_list

    for trial in range(numTrials):
        index = 0
        #print "\n========================="
        print 'Trial:', trial

        # list of viruses, SimpleVirus(maxBirthProb, clearProb)
        virus = SimpleVirus(maxBirthProb, clearProb)
        viruses = createVirusesList(numViruses, maxBirthProb, clearProb)

        # create a new Patient
        patient = Patient(viruses, maxPop)
        #print 'New patient created: ', patient

        # update and insert count into list for 300 time steps
        for time_step in range(300):
            # print "Trial: ", trial, "timestep: ", time_step

            # pdb.set_trace()
            num_viruses_list[index] += patient.update()
            index += 1

    viruses_average = num_viruses_list
    final_averages = []
    for virus in num_viruses_list:
        # pdb.set_trace()
        # print 'Virus: ', virus
        final_averages.append(float(virus) / float(300))
        # print 'New viruses list: ', final_averages

    print "\nNew virus averages list: ", final_averages

    # FOR THE GRAPH:
    # population at time=0 is the population after the first call to update
    # X axis: number of elapsed time steps
    # Y axis: average size of the virus population in the patient

    # plot graph - pylab.plot('list of x values', 'list of y values')
    pylab.figure(1)
    pylab.plot(range(1, 301), viruses_average)
    # pylab.yAxis = [0.0] * 300

    pylab.title('Simulation without Drugs')
    pylab.xlabel('Number of Elapsed Time Steps')
    pylab.ylabel('Average Size of the Virus Population')
    pylab.legend(loc = 'best')
    pylab.show()

def createVirusesList(numViruses, maxBirthProb, clearProb):
    viruses = []
    for virus in range(numViruses):
        viruses.append(SimpleVirus(maxBirthProb, clearProb))
    return viruses

def createEmptyList(listLength):
    list = []
    for list_item in range(listLength):
        list.append(0)
    return list


#def simulationWithoutDrug(numViruses, maxPop, maxBirthProb, clearProb, numTrials)
simulationWithoutDrug(1, 10, 1.0, 0.0, 1)
#simulationWithoutDrug(100, 200, 0.2, 0.8, 1)

# numViruses = 100
# maxPop = 1000
# maxBirthProb = .99
# clearProb = .05
# numTrials = 300
#
# num_viruses_list = createEmptyList(numTrials)
# print "\nList of zeroes for virus count: ", num_viruses_list
#
# virus = SimpleVirus(maxBirthProb, clearProb)
# viruses = createVirusesList(numViruses, maxBirthProb, clearProb)
#
# patient = Patient(viruses, maxPop)
# print 'New patient created: ', patient
