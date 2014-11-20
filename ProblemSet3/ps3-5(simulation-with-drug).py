from ps3b_precompiled_27 import *
import pdb
import random


def simulationWithDrug(numViruses, maxPop, maxBirthProb, clearProb, resistances,
                       mutProb, numTrials):
    """
    Runs simulations and plots graphs for problem 5.

    For each of numTrials trials, instantiates a patient, runs a simulation for
    150 timesteps, adds guttagonol, and runs the simulation for an additional
    150 timesteps.  At the end plots the average virus population size
    (for both the total virus population and the guttagonol-resistant virus
    population) as a function of time.

    numViruses: number of ResistantVirus to create for patient (an integer)
    maxPop: maximum virus population for patient (an integer)
    maxBirthProb: Maximum reproduction probability (a float between 0-1)
    clearProb: maximum clearance probability (a float between 0-1)
    resistances: a dictionary of drugs that each ResistantVirus is resistant to
                 (e.g., {'guttagonol': False})
    mutProb: mutation probability for each ResistantVirus particle
             (a float between 0-1).
    numTrials: number of simulation runs to execute (an integer)

    """
    timestep = 150
    viruses_average1 = oneSimulation(createEmptyList(timestep), numViruses, maxPop, maxBirthProb, clearProb, resistances, mutProb, numTrials)

    # adding guttagnol to resistance
    resistances['guttagonol'] = True
    viruses_average2 = oneSimulation(createEmptyList(timestep), numViruses, maxPop, maxBirthProb, clearProb, resistances, mutProb, numTrials)

    plotSimulationWithDrug(viruses_average1, viruses_average2)


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


def plotSimulationWithDrug(x_values1, x_values2):
    """
    population at time=0 is the population after the first call to update
    X axis: number of elapsed time steps
    Y axis: average size of the virus population in the patient
    returns: a plot!
    """
    pylab.figure(1)
    pylab.plot(x_values1)

    pylab.figure(1)
    pylab.plot(x_values2)

    pylab.title('Simulation with Drugs')
    pylab.xlabel('Number of Elapsed Time Steps')
    pylab.ylabel('Average Size of the Virus Population')
    pylab.figure(1)
    pylab.legend(loc = 'best')
    pylab.show()

def calcAverage(list_to_average, numTrials):
    averaged_list = []
    for list_item in list_to_average:
        divided_virus = float(list_item / numTrials)
        averaged_list.append(divided_virus)
    return averaged_list


def createVirusesList(numViruses, maxBirthProb, clearProb, resistances, mutProb):
    viruses = []
    for virus in range(numViruses):
        viruses.append(ResistantVirus(maxBirthProb, clearProb, resistances, mutProb))
    return viruses

def createEmptyList(listLength):
    zeroes_list = []
    for list_item in range(listLength):
        zeroes_list.append(0)
    return zeroes_list
