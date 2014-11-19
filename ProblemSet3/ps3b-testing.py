# Problem Set 3: Simulating the Spread of Disease and Virus Population Dynamics

import numpy
import random
import pylab
import pdb

'''
Begin helper code
'''

class NoChildException(Exception):
    """
    NoChildException is raised by the reproduce() method in the SimpleVirus
    and ResistantVirus classes to indicate that a virus particle does not
    reproduce. You can use NoChildException as is, you do not need to
    modify/add any code.
    """
    print 'Inside nochildexception exception'

'''
End helper code
'''

#
# PROBLEM 2

class SimpleVirus(object):

    """
    Representation of a simple virus (does not model drug effects/resistance).
    """
    def __init__(self, maxBirthProb, clearProb):
        """
        Initialize a SimpleVirus instance, saves all parameters as attributes
        of the instance.
        maxBirthProb: Maximum reproduction probability (a float between 0-1)
        clearProb: Maximum clearance probability (a float between 0-1).
        """
        self.maxBirthProb = maxBirthProb
        self.clearProb = clearProb

    def getMaxBirthProb(self):
        """
        Returns the max birth probability.
        """
        return self.maxBirthProb

    def getClearProb(self):
        """
        Returns the clear probability.
        """
        return self.clearProb

    def doesClear(self):
        """ Stochastically determines whether this virus particle is cleared from the
        patient's body at a time step.
        returns: True with probability self.getClearProb and otherwise returns
        False.
        """
        if self.clearProb == 0:
            return False
        elif (self.clearProb == 1):
            return True
        else:
            return random.choice([True, False])


    def reproduce(self, popDensity):
        """
        Stochastically determines whether this virus particle reproduces at a
        time step. Called by the update() method in the Patient and
        TreatedPatient classes. The virus particle reproduces with probability
        self.maxBirthProb * (1 - popDensity).

        If this virus particle reproduces, then reproduce() creates and returns
        the instance of the offspring SimpleVirus (which has the same
        maxBirthProb and clearProb values as its parent).

        popDensity: the population density (a float), defined as the current
        virus population divided by the maximum population.

        returns: a new instance of the SimpleVirus class representing the
        offspring of this virus particle. The child should have the same
        maxBirthProb and clearProb values as this virus. Raises a
        NoChildException if this virus particle does not reproduce.
        """
        # does particle need to reproduce?
        prob_reproduce = self.maxBirthProb * (1 - popDensity)
        random_reproduce = random.random() * prob_reproduce

        if (self.maxBirthProb == 1) or (random_reproduce >= .5):
            return SimpleVirus(self.maxBirthProb, self.clearProb)
        elif (self.maxBirthProb == 0) or (random_reproduce < .5):
            raise NoChildException


class Patient(object):
    """
    Representation of a simplified patient. The patient does not take any drugs
    and his/her virus populations have no drug resistance.
    """

    def __init__(self, viruses, maxPop):
        """
        Initialization function, saves the viruses and maxPop parameters as
        attributes.

        viruses: the list representing the virus population (a list of
        SimpleVirus instances)

        maxPop: the maximum virus population for this patient (an integer)
        """

        self.viruses = viruses
        self.maxPop = maxPop

    def getViruses(self):
        """
        Returns the viruses in this Patient.
        """
        return self.viruses


    def getMaxPop(self):
        """
        Returns the max population.
        """
        return self.maxPop


    def getTotalPop(self):
        """
        Gets the size of the current total virus population.
        returns: The total virus population (an integer)
        """

        return len(self.viruses)


    def update(self):
        """
        Update the state of the virus population in this patient for a single
        time step. update() should execute the following steps in this order:

        - Determine whether each virus particle survives and updates the list
        of virus particles accordingly.

        - The current population density is calculated. This population density
          value is used until the next call to update()

        - Based on this value of population density, determine whether each
          virus particle should reproduce and add offspring virus particles to
          the list of viruses in this patient.

        returns: The total virus population at the end of the update (an
        integer)
        """

        viruses_copy = self.viruses
        for virus in viruses_copy:
            cleared = virus.doesClear()
            print 'Running virus.doesClear() ', cleared
            if cleared:
                self.viruses.remove(virus)

        # for viruses that did survive, and need to be reproduced
        for virus in self.viruses:
            population = self.getTotalPop()
            popDensity = population / float(self.maxPop)
            if popDensity < 1:
                try:
                    offspring = virus.reproduce(popDensity)
                    if offspring != None:
                        self.viruses.append(offspring)
                except NoChildException:
                    # failed to reproduce, catching error
                    pass

        return self.getTotalPop()


v1 = SimpleVirus(0.99, 0.55)
popDensity = .02
prob_reproduce = v1.maxBirthProb * (1 - popDensity)
print 'Prob reproduce: ', prob_reproduce

v1.reproduce(popDensity)

# virus = SimpleVirus(.75, 1.0)
# print 'Created a new SimpleVirus(maxBirthProb, clearProb): ', virus
#
# p = Patient([virus], 100)
# print 'Created a new Patient(viruses, maxPop): ', p
# print 'Current population: ', p.viruses
# print 'Current virus population: ', p.getTotalPop()
