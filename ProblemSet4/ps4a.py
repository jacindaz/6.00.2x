# 6.00.2x Problem Set 4

import numpy
import random
import pylab
import pdb
from ps3b import *

#
# PROBLEM 1
#
def simulationDelayedTreatment(numTrials):
    """
    Runs simulations and make histograms for problem 1.

    Runs numTrials simulations to show the relationship between delayed
    treatment and patient outcome using a histogram.

    Histograms of final total virus populations are displayed for delays of 300,
    150, 75, 0 timesteps (followed by an additional 150 timesteps of
    simulation).

    numTrials: number of simulation runs to execute (an integer)
    """
    maxPop = 1000
    numViruses = 100
    maxBirthProb = .1
    clearProb = .05
    resistances = {'guttagonol': False}
    mutProb = .005

    viruses_300 = []
    viruses_150 = []
    viruses_75 = []
    viruses_0 = []
    viruses_resistance = []

    for trial in range(numTrials):
        virus300 = oneSimulation(numViruses, maxPop, maxBirthProb, clearProb, resistances, mutProb, numTrials, 300)
        virus150 = oneSimulation(numViruses, maxPop, maxBirthProb, clearProb, resistances, mutProb, numTrials, 150)
        virus75 = oneSimulation(numViruses, maxPop, maxBirthProb, clearProb, resistances, mutProb, numTrials, 75)
        resistances['guttagonol'] = True

        virus_added300 = oneSimulation(virus300, maxPop, maxBirthProb, clearProb, resistances, mutProb, numTrials, 150)
        viruses_300.append(virus_added300)

        virus_added150 = oneSimulation(virus150, maxPop, maxBirthProb, clearProb, resistances, mutProb, numTrials, 150)
        viruses_150.append(virus_added150)

        virus_added75 = oneSimulation(virus75, maxPop, maxBirthProb, clearProb, resistances, mutProb, numTrials, 150)
        viruses_75.append(virus_added75)

        virus_added0 = oneSimulation(numViruses, maxPop, maxBirthProb, clearProb, resistances, mutProb, numTrials, 150)
        viruses_0.append(virus_added0)

        # pdb.set_trace()

    plots = [viruses_300, viruses_150, viruses_75, viruses_0]
    plotSimulationWithDrug(plots)


def createEmptyList(listLength, list_items = 0):
    zeroes_list = []
    for list_item in range(listLength):
        zeroes_list.append(list_items)
    return zeroes_list



def oneSimulation(numViruses, maxPop, maxBirthProb, clearProb, resistances, mutProb, numTrials, timestep):
    for trial in range(numTrials):
        index = 0
        viruses = createVirusesList(numViruses, maxBirthProb, clearProb, resistances, mutProb)

        # create a new Patient
        patient = TreatedPatient(viruses, maxPop)

        # update and insert count into list for 300 time steps
        for time_step in range(timestep):
            num_viruses = patient.update()
            # index += 1

    # pdb.set_trace()
    return num_viruses
    # return viruses_list[-1]

def createVirusesList(numViruses, maxBirthProb, clearProb, resistances, mutProb):
    viruses = []
    for virus in range(numViruses):
        viruses.append(ResistantVirus(maxBirthProb, clearProb, resistances, mutProb))
    return viruses


def plotSimulationWithDrug(final_viruses):
    """
    population at time=0 is the population after the first call to update
    X axis: number of elapsed time steps
    Y axis: average size of the virus population in the patient
    returns: a plot!
    """
    # figure_number = 1
    # for list in final_viruses:
    #     pylab.figure(figure_number)
    #     pylab.subplot(4, 1, figure_number, sharey = True)
    #     pylab.hist(list)
    #     figure_number += 1
    # end

    pdb.set_trace()

    pylab.hist(final_viruses[0])

    # pylab.hist(final_viruses[1])
    # # pylab.subplot(5, 2, 1)
    #
    # pylab.hist(final_viruses[2])
    # # pylab.subplot(5, 3, 1)
    #
    # pylab.hist(final_viruses[3])
    # # pylab.subplot(5, 4, 1)
    #
    # pylab.subplot(4, 1, 1)


    pylab.title('Simulation with Drugs')
    pylab.xlabel('Number of Elapsed Time Steps')
    pylab.ylabel('Average Size of the Virus Population')
    pylab.legend(loc = 'best')
    pylab.show()




simulationDelayedTreatment(5)



#
# PROBLEM 2
#
def simulationTwoDrugsDelayedTreatment(numTrials):
    """
    Runs simulations and make histograms for problem 2.

    Runs numTrials simulations to show the relationship between administration
    of multiple drugs and patient outcome.

    Histograms of final total virus populations are displayed for lag times of
    300, 150, 75, 0 timesteps between adding drugs (followed by an additional
    150 timesteps of simulation).

    numTrials: number of simulation runs to execute (an integer)
    """
    # TODO
