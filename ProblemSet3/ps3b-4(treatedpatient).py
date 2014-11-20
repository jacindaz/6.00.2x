from ps3b_precompiled_27 import *
import pdb
import random

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
            resistant = self.resistances[activeDrug]
            if not resistant:
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
                if resistances_copy[drug] == True:
                    print 'Wohooo! Virus is resistant!'
                    virus_drug_resistances = True
                else:
                    print 'Oops, sorry. Not resistant!'
                    virus_drug_resistances = False

            # for resistance in virus.resistances:
            #     if (virus.resistances[resistance] == True):
            #         virus_drug_resistances = True
            #     else:
            #         print 'Oops, sorry. Not resistant!'
            #         virus_drug_resistances = False

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
        viruses_copy = self.viruses

        print "\n===================="
        print 'Inside update() TreatedPatient method'
        print 'Current virus list: ', self.getViruses()

        for virus in viruses_copy:
            cleared = virus.doesClear()
            if cleared:
                self.getViruses().remove(virus)

        print "\nSurvived viruses: ", self.getViruses()

        survived_viruses = self.getViruses()
        # for viruses that did survive, and need to be reproduced
        for virus in survived_viruses:
            population = self.getTotalPop()
            popDensity = population / float(self.maxPop)

            #if (popDensity < 1) and (virus not in self.drugs_list):
            if (popDensity < 1):
                try:
                    offspring = virus.reproduce(popDensity, self.drugs_list)
                    if offspring != None:
                        self.getViruses().append(offspring)
                        print "\nSuccessfully reproduced!"
                        print 'New viruses list length: ', len(self.viruses)
                except NoChildException:
                    # failed to reproduce, catching error
                    print "\nWas not able to reproduce"
                    continue

        print "\nFinal viruses list: ", self.viruses
        print 'Final viruses list length: ', len(self.viruses)
        return self.getTotalPop()


# virus = ResistantVirus(1.0, 0.0, {}, 0.0)
virus = ResistantVirus(1.0, 0.0, {"drug1": False, "drug2": True}, 1.0)
patient = TreatedPatient([virus], 100)
# patient.update()

patient.getResistPop(['drug1'])


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
