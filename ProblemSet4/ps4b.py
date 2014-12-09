# 6.00.2x Problem Set 4

import numpy
import random
import pylab
import pdb
from ps3b import *

# 6.00.2x Problem Set 4


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
    global maxPop
    global numViruses
    global maxBirthProb
    global clearProb
    global resistances
    global mutProb

    maxPop = 1000
    numViruses = 100
    maxBirthProb = .1
    clearProb = .05
    resistances = {'guttagonol': False, 'grimpex': False}
    mutProb = .005

    # Run the simulation for 150 time steps
    # administering guttagonol to the patient

    # run the simulation for 300, 150, 75, and 0 time steps
    v_300 = simulations(numViruses, maxPop, maxBirthProb, clearProb, resistances, mutProb, numTrials, 150, 300, 'guttagonol')
    v_150 = simulations(numViruses, maxPop, maxBirthProb, clearProb, resistances, mutProb, numTrials, 150, 150, 'guttagonol')
    v_75 = simulations(numViruses, maxPop, maxBirthProb, clearProb, resistances, mutProb, numTrials, 150, 75, 'guttagonol')
    v_0 = simulations(numViruses, maxPop, maxBirthProb, clearProb, resistances, mutProb, numTrials, 150, 0, 'guttagonol')

    # administer a second drug, grimpex, to the patient
    # run the simulation for an additional 150 time steps
    viruses_300 = simulationsWithViruses(v_300[-1], maxPop, maxBirthProb, clearProb, resistances, mutProb, numTrials, 150, v_300, 'grimpex')
    viruses_150 = simulationsWithViruses(v_150[-1], maxPop, maxBirthProb, clearProb, resistances, mutProb, numTrials, 150, v_150, 'grimpex')
    viruses_75 = simulationsWithViruses(v_75[-1], maxPop, maxBirthProb, clearProb, resistances, mutProb, numTrials, 150, v_75, 'grimpex')
    viruses_0 = simulationsWithViruses(v_0[-1], maxPop, maxBirthProb, clearProb, resistances, mutProb, numTrials, 150, v_0, 'grimpex')


    # simulations returns an array of final virus count, given the timestep (300, 150, ... )
    plots = [viruses_300, viruses_150, viruses_75, viruses_0]
    plotSimulationWithDrug(plots)

def simulationsWithViruses(numViruses, maxPop, maxBirthProb, clearProb, resistances, mutProb, numTrials, resistance_timesteps, virus_list, newDrug = None):
    final_viruses_counts = virus_list
    for trial in range(numTrials):
        viruses = createVirusesList(numViruses, maxBirthProb, clearProb, resistances, mutProb)
        patient = TreatedPatient(viruses, maxPop)

        # introduces new drug as a resistance
        patient.addPrescription(newDrug)

        for time_step in range(resistance_timesteps):
            num_viruses = patient.update()
        final_viruses_counts.append(num_viruses)

    return final_viruses_counts

def simulations(numViruses, maxPop, maxBirthProb, clearProb, resistances, mutProb, numTrials, timestep, resistance_timesteps, newDrug = None):
    final_viruses_counts = []
    for trial in range(numTrials):
        print 'Trial: ', trial, 'Timestep: ', resistance_timesteps
        viruses = createVirusesList(numViruses, maxBirthProb, clearProb, resistances, mutProb)
        patient = TreatedPatient(viruses, maxPop)

        for time_step in range(timestep):
            num_viruses = patient.update()

        # introduces new drug as a resistance
        patient.addPrescription(newDrug)

        for time_step in range(resistance_timesteps):
            num_viruses = patient.update()
        final_viruses_counts.append(num_viruses)

    return final_viruses_counts


def createVirusesList(numViruses, maxBirthProb, clearProb, resistances, mutProb):
    viruses = []
    for virus in range(numViruses):
        viruses.append(ResistantVirus(maxBirthProb, clearProb, resistances, mutProb))
    return viruses

def numCured(viruses_list):
    numCured = 0
    for virus in viruses_list:
        if virus <= 50:
            numCured += 1
    return numCured

def plotSimulationWithDrug(final_viruses):
    # print "\n=========================================="
    # print 'Final viruses lists'
    # print "\n-------------------"
    # print "\tTimestep 300: ", final_viruses[0]
    # print "-------------------\n"
    #
    # print "\n-------------------"
    # print "\tTimestep 150: ", final_viruses[1]
    # print "-------------------\n"
    #
    # print "\n-------------------"
    # print "\tTimestep 75: ", final_viruses[2]
    # print "-------------------\n"
    #
    # print "\n-------------------"
    # print "\tTimestep 0: ", final_viruses[3]
    # print "==========================================\n"

    print "\n============="
    print 'Timestep: 300'
    print 'Num cured: ', numCured(final_viruses[0])
    print "============="

    print "\n============="
    print 'Timestep: 150'
    print 'Num cured: ', numCured(final_viruses[1])
    print "============="

    print "\n============="
    print 'Timestep: 75'
    print 'Num cured: ', numCured(final_viruses[2])
    print "============="

    print "\n============="
    print 'Timestep: 0'
    print 'Num cured: ', numCured(final_viruses[3])
    print "=============\n"

    print "\n=============="
    print 'maxpop: ', maxPop
    print 'numviruses: ', numViruses
    print 'maxBirthProb: ',  maxBirthProb
    print 'clearProb: ', clearProb
    print 'resistances: ', resistances
    print 'muProb: ', mutProb
    print "==============\n"


    # x-axis of the histogram should be:
    ###### the final total virus population values
    ###### (choose x axis increments or "histogram bins" according to the range
    #         of final virus population values you get by running the simulation
    #         multiple times).
    # y-axis of the histogram should be:
    ###### the number of trials belonging to each histogram bin

    # 300 timestep
    pylab.subplot(5, 1, 1)
    pylab.hist(final_viruses[0], range(min(final_viruses[0]), max(final_viruses[0])))
    pylab.title('300 Timestep')

    # 150 Timestep
    pylab.subplot(5, 1, 2)
    pylab.hist(final_viruses[1], range(min(final_viruses[1]), max(final_viruses[1])))
    pylab.title('150 Timestep')

    # 75 timestep
    pylab.subplot(5, 1, 3)
    pylab.hist(final_viruses[2], range(-1, max(final_viruses[2])))
    pylab.title('75 Timestep')

    # pylab.hist(final_viruses[3], range(min(final_viruses[3]), max(final_viruses[3])))

    # 0 timestep
    pylab.subplot(5, 1, 4)
    pylab.hist(final_viruses[3], range(-1, 1))
    pylab.title('0 Timestep')

    pylab.title('Simulation with Drugs')
    pylab.xlabel('Final Virus Population values')
    pylab.ylabel('Number of Trials')
    pylab.legend(loc = 'best')
    pylab.show()


simulationTwoDrugsDelayedTreatment(10)
