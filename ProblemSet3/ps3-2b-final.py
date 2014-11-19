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
    timestep = 300
    num_viruses_list = createEmptyList(timestep)

    for trial in range(numTrials):
        index = 0
        virus = SimpleVirus(maxBirthProb, clearProb)
        viruses = createVirusesList(numViruses, maxBirthProb, clearProb)

        # create a new Patient
        patient = Patient(viruses, maxPop)

        # update and insert count into list for 300 time steps
        for time_step in range(timestep):
            num_viruses_list[index] += patient.update()
            index += 1

    viruses_average = calcAverage(num_viruses_list, numTrials)
    plotSimulationWithoutDrug(range(1, 301), viruses_average)

def plotSimulationWithoutDrug(x_values, y_values):
    """
    population at time=0 is the population after the first call to update
    X axis: number of elapsed time steps
    Y axis: average size of the virus population in the patient
    returns: a plot!
    """
    pylab.figure(1)
    pylab.plot(x_values, y_values)

    pylab.title('Simulation without Drugs')
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


def createVirusesList(numViruses, maxBirthProb, clearProb):
    viruses = []
    for virus in range(numViruses):
        viruses.append(SimpleVirus(maxBirthProb, clearProb))
    return viruses

def createEmptyList(listLength):
    zeroes_list = []
    for list_item in range(listLength):
        zeroes_list.append(0)
    return zeroes_list
