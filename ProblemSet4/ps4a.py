# 6.00.2x Problem Set 4

import numpy
import random
import pylab
import pdb
from ps3b import *

def simulationDelayedTreatment(numTrials):
    # ORIGINAL VALUES
    # global maxPop = 1000
    # global numViruses = 100
    # global maxBirthProb = .1
    # global clearProb = .05
    # global resistances = {'guttagonol': False}
    # global mutProb = .005

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
    resistances = {'guttagonol': True}
    mutProb = .005

    # simulations returns an array of final virus count, given the timestep (300, 150, ... )
    print "\n=========="
    viruses_300 = simulations(numViruses, maxPop, maxBirthProb, clearProb, resistances, mutProb, numTrials, 300, 150, 'guttagonol')
    print 'Done with viruses 300'
    print "==========\n"

    viruses_150 = simulations(numViruses, maxPop, maxBirthProb, clearProb, resistances, mutProb, numTrials, 150, 150, 'guttagonol')
    print 'Done with viruses 150'

    viruses_75 = simulations(numViruses, maxPop, maxBirthProb, clearProb, resistances, mutProb, numTrials, 75, 150, 'guttagonol')
    print 'Done with viruses 75'

    viruses_0 = simulations(numViruses, maxPop, maxBirthProb, clearProb, resistances, mutProb, numTrials, 0, 150, 'guttagonol')
    print 'Done with viruses 0'

    plots = [viruses_300, viruses_150, viruses_75, viruses_0]
    plotSimulationWithDrug(plots)


def createEmptyList(listLength, list_items = 100):
    initial_viruses_list = []
    for list_item in range(listLength):
        zeroes_list.append(list_items)
    return initial_viruses_list


def simulations(numViruses, maxPop, maxBirthProb, clearProb, resistances, mutProb, numTrials, timestep, resistance_timesteps, newDrug = None):
    final_viruses_counts = []
    for trial in range(numTrials):
        print 'Trial: ', trial, 'Timestep: ', timestep
        viruses = createVirusesList(numViruses, maxBirthProb, clearProb, resistances, mutProb)
        patient = TreatedPatient(viruses, maxPop)

        for time_step in range(timestep):
            num_viruses = patient.update()
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


simulationDelayedTreatment(1000)
