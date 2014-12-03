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
        virus300 = oneSimulation(createEmptyList(300), numViruses, maxPop, maxBirthProb, clearProb, resistances, mutProb, numTrials, 300)
        viruses_300.append(virus300)

        virus150 = oneSimulation(createEmptyList(150), numViruses, maxPop, maxBirthProb, clearProb, resistances, mutProb, numTrials, 150)
        viruses_150.append(virus150)

        virus75 = oneSimulation(createEmptyList(75), numViruses, maxPop, maxBirthProb, clearProb, resistances, mutProb, numTrials, 75)
        viruses_75.append(virus75)

        # virus0 = createEmptyList(numViruses, 1)
        viruses_0.append(100)
        resistances['guttagonol'] = True

        virus_added = oneSimulation(createEmptyList(150), numViruses, maxPop, maxBirthProb, clearProb, resistances, mutProb, numTrials, 150)
        viruses_resistance.append(virus_added)

    plots = [viruses_300, viruses_150, viruses_75, viruses_0, viruses_resistance]

    plotSimulationWithDrug(plots)



def createEmptyList(listLength, list_items = 0):
    zeroes_list = []
    for list_item in range(listLength):
        zeroes_list.append(list_items)
    return zeroes_list



def oneSimulation(viruses_list, numViruses, maxPop, maxBirthProb, clearProb, resistances, mutProb, numTrials, timestep):
    for trial in range(numTrials):
        index = 0
        virus = ResistantVirus(maxBirthProb, clearProb, resistances, mutProb)
        viruses = createVirusesList(numViruses, maxBirthProb, clearProb, resistances, mutProb)

        # create a new Patient
        patient = TreatedPatient(viruses, maxPop)

        # update and insert count into list for 300 time steps
        for time_step in range(timestep):
            viruses_list[index] += patient.update()
            index += 1

    return viruses_list[-1]

def createVirusesList(numViruses, maxBirthProb, clearProb, resistances, mutProb):
    viruses = []
    for virus in range(numViruses):
        viruses.append(ResistantVirus(maxBirthProb, clearProb, resistances, mutProb))
    return viruses

def calcAverage(list_to_average, numTrials):
    averaged_list = []
    for list_item in list_to_average:
        divided_virus = float(list_item / numTrials)
        averaged_list.append(divided_virus)
    return averaged_list


def plotSimulationWithDrug(list_of_lists):
    """
    population at time=0 is the population after the first call to update
    X axis: number of elapsed time steps
    Y axis: average size of the virus population in the patient
    returns: a plot!
    """
    # figure_number = 1
    # for list in list_of_lists:
    #     pylab.figure(figure_number)
    #     pylab.subplot(4, 1, figure_number, sharey = True)
    #     pylab.hist(list)
    #     figure_number += 1
    # end

    pylab.hist(list_of_lists[0])

    pylab.hist(list_of_lists[1])
    # pylab.subplot(5, 2, 1)

    pylab.hist(list_of_lists[2])
    # pylab.subplot(5, 3, 1)

    pylab.hist(list_of_lists[3])
    # pylab.subplot(5, 4, 1)

    pylab.hist(list_of_lists[4])
    # pylab.subplot(5, 5, 1)

    pylab.subplot(5, 1, 1)


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
