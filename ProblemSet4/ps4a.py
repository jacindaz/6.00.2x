# 6.00.2x Problem Set 4

import numpy
import random
import pylab
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
    
    # run simulation 300 timesteps
	viruses_average1 = oneSimulation(createEmptyList(timestep), numViruses, maxPop, maxBirthProb, clearProb, resistances, mutProb, numTrials)	

    # run simulation 150 timesteps


    # run simulation 75 timesteps


    # run simulation 0 timesteps


    # administer guttagonol
    resistances['guttagonol'] = True

    # run simulation another 150 timesteps
    # for each of the other simulations (300, 150, 75, 0)



def createEmptyList(listLength):
    zeroes_list = []
    for list_item in range(listLength):
        zeroes_list.append(0)
    return zeroes_list



def oneSimulation(viruses_list, numViruses, maxPop, maxBirthProb, clearProb, resistances, mutProb, numTrials):
    timestep = 150

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

    viruses_average = calcAverage(viruses_list, numTrials)
    return viruses_average




def plotSimulationWithDrug(x_values1, x_values2, x_values3, x_values4):
    """
    population at time=0 is the population after the first call to update
    X axis: number of elapsed time steps
    Y axis: average size of the virus population in the patient
    returns: a plot!
    """
    pylab.figure(1)
	pylab.subplot(4, 1, 1, sharey = True)
    pylab.plot(x_values1)

    pylab.figure(2)
	pylab.subplot(4, 1, 2, sharey = True)
    pylab.plot(x_values2)

    pylab.title('Simulation with Drugs')
    pylab.xlabel('Number of Elapsed Time Steps')
    pylab.ylabel('Average Size of the Virus Population')
    pylab.figure(1)
    pylab.legend(loc = 'best')
    pylab.show()








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
