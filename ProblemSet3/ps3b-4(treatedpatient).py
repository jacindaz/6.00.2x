# from ps3b_precompiled_27 import *
import pdb
import random

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
        random_reproduce = random.random()

        if random_reproduce > prob_reproduce:
            raise NoChildException
        else:
            return SimpleVirus(self.maxBirthProb, self.clearProb)

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



class ResistantVirus(SimpleVirus):

    def __init__(self, maxBirthProb, clearProb, resistances, mutProb):
        SimpleVirus.__init__(self, maxBirthProb, clearProb)
        self.resistances = resistances
        self.mutProb = mutProb

    def getResistances(self):
        return self.resistances

    def getMutProb(self):
        return self.mutProb

    def isResistantTo(self, drug):
        for key in self.resistances:
            if drug == key:
                if self.resistances[key] == True:
                    return True
        return False


    def reproduce(self, popDensity, activeDrugs):
        drugs_resistance = self.resistantAllDrugs(activeDrugs)
        prob_inherit_resistance = 1 - self.mutProb

        # if resistant to all drugs, is able to reproduce
        if drugs_resistance:
            prob_reproduce = self.maxBirthProb * (1 - popDensity)
            random_reproduce = random.random()

            # will not reproduce
            if random_reproduce > prob_reproduce:
                raise NoChildException

            # will reproduce
            else:
                offspring = ResistantVirus(self.maxBirthProb, self.clearProb, {}, self.mutProb)
                new_resistances = self.newResistances(self.resistances)
                offspring.resistances = new_resistances

                return offspring

        # if not resistant to all drugs, can't reproduce
        else:
            raise NoChildException

    def newResistances(self, current_resistances):
        new_resistances = {}

        for key,value in current_resistances.items():
            prob_inherit_resistance = 1 - self.mutProb
            random_resistance = random.random()

            if prob_inherit_resistance > random_resistance:
                new_resistances[key] = value
            else:
                new_resistances[key] = (not value)

        return new_resistances

    def resistantAllDrugs(self, activeDrugs):
        for activeDrug in activeDrugs:
            if self.isResistantTo(activeDrug) == False:
                return False
        return True



class TreatedPatient(Patient):
    """
    Representation of a patient. The patient is able to take drugs and his/her
    virus population can acquire resistance to the drugs he/she takes.
    """

    def __init__(self, viruses, maxPop):
        """
        Initialization function, saves the viruses and maxPop parameters as
        attributes. Also initializes the list of drugs being administered
        (which should initially include no drugs).

        viruses: The list representing the virus population (a list of
        virus instances)

        maxPop: The  maximum virus population for this patient (an integer)
        """
        Patient.__init__(self, viruses, maxPop)
        self.drugs_list = []


    def addPrescription(self, newDrug):
        """
        Administer a drug to this patient. After a prescription is added, the
        drug acts on the virus population for all subsequent time steps. If the
        newDrug is already prescribed to this patient, the method has no effect.

        newDrug: The name of the drug to administer to the patient (a string).

        postcondition: The list of drugs being administered to a patient is updated
        """
        self.drugs_list.append(newDrug)


    def getPrescriptions(self):
        """
        Returns the drugs that are being administered to this patient.

        returns: The list of drug names (strings) being administered to this
        patient.
        """
        return self.drugs_list


    def getResistPop(self, drugResist):
        """
        Get the population of virus particles resistant to the drugs listed in
        drugResist.

        drugResist: Which drug resistances to include in the population (a list
        of strings - e.g. ['guttagonol'] or ['guttagonol', 'srinol'])

        returns: The population of viruses (an integer) with resistances to all
        drugs in the drugResist list.
        """
        virus_resistance_count = 0
        viruses_copy = self.getViruses()

        # look at list of viruses for this patient
        for virus in viruses_copy:
            resistances_copy = virus.getResistances()
            virus_drug_resistances = False

            print "\nIterating over virus: ", virus
            print 'Virus resistances: ', virus.getResistances()

            # look at list of drugs
            for drug in drugResist:

                # checks if key exists, if not, returns False
                # if yes, returns the value
                drug_resistance = resistances_copy.get(drug, False)
                if drug_resistance:
                    print 'Wohooo! Virus is resistant!'
                    virus_drug_resistances = True
                else:
                    print 'Oops, sorry. Not resistant!'
                    virus_drug_resistances = False
                    break

            # count number of viruses who have resistances for all drugs
            if virus_drug_resistances == True:
                print "\nVirus is resistant! Woot!"
                print 'Old count: ', virus_drug_resistances
                virus_resistance_count += 1
                print 'New count: ', virus_resistance_count

            print "\n================="
            print 'Virus: ', virus
            print 'Virus resistances: ', virus.resistances
            print 'Current virus resistance count: ', virus_resistance_count
            print "=================\n"

        return virus_resistance_count



    def update(self):
        """
        Update the state of the virus population in this patient for a single
        time step. update() should execute these actions in order:

        - Determine whether each virus particle survives and update the list of
          virus particles accordingly

        - The current population density is calculated. This population density
          value is used until the next call to update().

        - Based on this value of population density, determine whether each
          virus particle should reproduce and add offspring virus particles to
          the list of viruses in this patient.

        - The list of drugs being administered should be accounted for in the
          determination of whether each virus particle reproduces.

          The drugs we consider do not directly kill virus particles lacking
          resistance to the drug, but prevent those virus particles from
          reproducing (much like actual drugs used to treat HIV). Virus
          particles with resistance to the drug continue to reproduce normally

        returns: The total virus population at the end of the update (an
        integer)
        """
        viruses_copy = self.getViruses()

        print "\n===================="
        print 'Inside update() TreatedPatient method'
        print 'Current virus list: ', self.getViruses()

        pdb.set_trace()

        survived_viruses = self.getViruses()
        print "\nSurvived viruses: ", survived_viruses
        viruses_offspring = self.getViruses()

        # for viruses that did survive, and need to be reproduced
        for virus in survived_viruses:
            population = self.getTotalPop()
            popDensity = population / float(self.maxPop)

            #if (popDensity < 1) and (virus not in self.drugs_list):
            if (popDensity < 1):
                try:
                    offspring = virus.reproduce(popDensity, self.getPrescriptions())
                    if offspring != None:
                        viruses_offspring.append(offspring)
                        print "\nSuccessfully reproduced!"
                        print 'New viruses list length: ', len(self.viruses)
                except NoChildException:
                    # failed to reproduce, catching error
                    print "\nWas not able to reproduce"
                    continue

        print "\nFinal viruses list: ", self.viruses
        print 'Final viruses list length: ', len(self.viruses)
        return self.getTotalPop()

    def checkAllViruses(self):
        viruses_copy = self.getViruses()
        for virus in viruses_copy:
            if virus.doesClear():
                self.getViruses().remove(virus)


virus1 = ResistantVirus(1.0, 0.0, {"drug1": True}, 0.0)
virus2 = ResistantVirus(1.0, 0.0, {"drug1": False, "drug2": True}, 0.0)
virus3 = ResistantVirus(1.0, 0.0, {"drug1": True, "drug2": True}, 0.0)
patient = TreatedPatient([virus1, virus2, virus3], 100)
# patient.getResistPop(['drug1'])                         # => 2
# patient.getResistPop(['drug2'])                         # => 2
# patient.getResistPop(['drug1','drug2'])                 # => 1
# patient.getResistPop(['drug3'])                         # => 0
# patient.getResistPop(['drug1', 'drug3'])                # => 0
# patient.getResistPop(['drug1','drug2', 'drug3'])        # => 0
#

# v = ResistantVirus(1.0, 0.0, {"drug1": False, "drug2": True}, 1.0)
# p = TreatedPatient([v, v], .2)
#
# print "\n=============="
# print 'New patient created: ', p
# print 'Patient viruses: ', p.viruses
# print 'Patient maxPop: ', p.maxPop
#
# print "\nTreatedPatient object's number of viruses: ", len(p.viruses)
# print 'Virus resistances: ', p.viruses[0].resistances
# print 'Virus clearProb: ', p.viruses[0].clearProb
# print 'Virus mutProb: ', p.viruses[0].mutProb
# print 'Virus maxBirthProb: ', p.viruses[0].maxBirthProb
# print "==============\n"
#
# p.getResistPop(['drug2', 'drug1'])
#
