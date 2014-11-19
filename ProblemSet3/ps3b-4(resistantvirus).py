from ps3b_precompiled_27 import *
import pdb
import random

#
# PROBLEM 4
#
class ResistantVirus(SimpleVirus):
    """
    Representation of a virus which can have drug resistance.
    """

    def __init__(self, maxBirthProb, clearProb, resistances, mutProb):
        """
        Initialize a ResistantVirus instance, saves all parameters as attributes
        of the instance.

        maxBirthProb: Maximum reproduction probability (a float between 0-1)

        clearProb: Maximum clearance probability (a float between 0-1).

        resistances: A dictionary of drug names (strings) mapping to the state
        of this virus particle's resistance (either True or False) to each drug.
        e.g. {'guttagonol':False, 'srinol':False}, means that this virus
        particle is resistant to neither guttagonol nor srinol.

        mutProb: Mutation probability for this virus particle (a float). This is
        the probability of the offspring acquiring or losing resistance to a drug.

        The __init__ method of ResistantVirus should directly call the
        __init__ method of SimpleVirus via the line:
           SimpleVirus.__init__(self, <appropriate parameters>)
        """
        SimpleVirus.__init__(self, maxBirthProb, clearProb)
        self.resistances = resistances
        self.mutProb = mutProb

    def getResistances(self):
        """
        Returns the resistances for this virus.
        """
        return self.resistances

    def getMutProb(self):
        """
        Returns the mutation probability for this virus.
        """
        return self.mutProb

    def isResistantTo(self, drug):
        """
        Get the state of this virus particle's resistance to a drug. This method
        is called by getResistPop() in TreatedPatient to determine how many virus
        particles have resistance to a drug.

        drug: The drug (a string)

        returns: True if this virus instance is resistant to the drug, False
        otherwise.
        """

        # loop through self.resistances
        # is drug in this dictionary?
        # if drug in the dictionary....
        #    True   => resistant to drug
        #    False  => not resistance to drug
        for key in self.resistances:
            if drug == key:
                if self.resistances[key] == True:
                    return True

        print 'Sorry, that drug does not exist'
        return False


    def reproduce(self, popDensity, activeDrugs):
        """
        Stochastically determines whether this virus particle reproduces at a
        time step. Called by the update() method in the TreatedPatient class.

        A virus particle will only reproduce if it is resistant to ALL the drugs
        in the activeDrugs list. For example, if there are 2 drugs in the
        activeDrugs list, and the virus particle is resistant to 1 or no drugs,
        then it will NOT reproduce.

        Hence, if the virus is resistant to all drugs
        in activeDrugs, then the virus reproduces with probability:

        self.maxBirthProb * (1 - popDensity).

        If this virus particle reproduces, then reproduce() creates and returns
        the instance of the offspring ResistantVirus (which has the same
        maxBirthProb and clearProb values as its parent). The offspring virus
        will have the same maxBirthProb, clearProb, and mutProb as the parent.

        For each drug resistance trait of the virus (i.e. each key of
        self.resistances), the offspring has probability 1-mutProb of
        inheriting that resistance trait from the parent, and probability
        mutProb of switching that resistance trait in the offspring.

        For example, if a virus particle is resistant to guttagonol but not
        srinol, and self.mutProb is 0.1, then there is a 10% chance that
        that the offspring will lose resistance to guttagonol and a 90%
        chance that the offspring will be resistant to guttagonol.
        There is also a 10% chance that the offspring will gain resistance to
        srinol and a 90% chance that the offspring will not be resistant to
        srinol.

        popDensity: the population density (a float), defined as the current
        virus population divided by the maximum population

        activeDrugs: a list of the drug names acting on this virus particle
        (a list of strings).

        returns: a new instance of the ResistantVirus class representing the
        offspring of this virus particle. The child should have the same
        maxBirthProb and clearProb values as this virus. Raises a
        NoChildException if this virus particle does not reproduce.
        """

        # A virus particle will only reproduce if it is resistant
        #   to ALL the drugs in the activeDrugs list
        drugs_resistance = self.resistantAllDrugs(activeDrugs)
        prob_inherit_resistance = 1 - self.mutProb

        # if resistant to all drugs, is able to reproduce
        if drugs_resistance:
            print 'Congrats, this virus is resistant to all drugs'

        # (stochastic) virus reproduces with probability:
            # self.maxBirthProb * (1 - popDensity)
            prob_reproduce = self.maxBirthProb * (1 - popDensity)
            random_reproduce = random.random()
            print 'Probability of it reproducing: ', prob_reproduce

            # will not reproduce
            if random_reproduce > prob_reproduce:
                print 'Boo boo. The virus will not reproduce.'
                raise NoChildException

            # will reproduce
            else:
                print 'Shwet. The virus will reproduce!'

                #ResistantVirus(maxBirthProb, clearProb, resistances, mutProb)
                #placeholder ResistantVirus object, will fill in resistances based on
                #    if the offspring mutates or not
                offspring = ResistantVirus(self.maxBirthProb, self.clearProb, {}, self.mutProb)

                # For each drug resistance trait of the virus, the offspring has probability 1-mutProb of
                # inheriting that resistance trait from the parent, and probability
                # mutProb of switching that resistance trait in the offspring.

                new_resistances = self.newResistances(self.resistances)
                offspring.resistances = new_resistances
                pdb.set_trace()
                return offspring

                # if (self.mutProb == 0) or (prob_inherit_resistance >= .5):
                #     print "\nThe virus will not mutate"
                #     print "This is the prob_inherit_resistance: ", prob_inherit_resistance
                #     # inherits parent resistances, doesn't mutate
                #     offspring.resistances = self.resistances
                #     return offspring
                #
                # # does not inherit parent resistances, does mutate
                # elif (self.mutProb == 1) or (prob_inherit_resistance > .5):
                #     print "\nThe virus will mutate"
                #     print "This is the prob_inherit_resistance: ", prob_inherit_resistance
                #     new_resistances = self.newResistances(self.resistances, prob_inherit_resistance)
                #     offspring.resistances = new_resistances
                #     return offspring

        # if not resistant to all drugs, can't reproduce
        else:
            print 'Sorry, not resistance to all activeDrugs. Will not reproduce.'

    def newResistances(self, current_resistances):
        new_resistances = {}

        for key,value in current_resistances.items():
            prob_inherit_resistance = 1 - self.mutProb
            random_resistance = random.random()
            print "\nThis is the prob_inherit_resistance: ", prob_inherit_resistance
            print 'random resistance: ', random_resistance

            if random_resistance <= prob_inherit_resistance:
                print 'The drug will mutate to change resistance'
                new_resistances[key] = (not value)

            elif random_resistance > prob_inherit_resistance:
                print 'The drug will not mutate, will keep the same resistance'
                new_resistances[key] = value

        print "\nThese are the new resistances: ", new_resistances
        return new_resistances

    # A virus particle will only reproduce if it is resistant to
    # ALL the drugs in the activeDrugs list
    def resistantAllDrugs(self, activeDrugs):
        print "These are all the activeDrugs: \n", activeDrugs

        for activeDrug in activeDrugs:
            # if False in the self.resistances dictionary
            resistant = self.resistances[activeDrug]
            if not resistant:
                print "Ooopa! Found a drug that virus is not resistant to.\
                        \nReturn False"
                return False
        return True


# CLASS/METHOD INFORMATION ---------------------------------------
# reproduce(self, popDensity, activeDrugs)
# ResistantVirus(SimpleVirus)
# ResistantVirus(self, maxBirthProb, clearProb, resistances, mutProb)

# TEST CASES ---------------------------------------

# Create a ResistantVirus that is never cleared and never reproduces
# v = ResistantVirus(0.0, 0.0, {}, 0.0)

# Create a ResistantVirus that is never cleared and always reproduces.
# v = ResistantVirus(1.0, 0.0, {}, 0.0)

# Create a ResistantVirus that is always cleared and never reproduces.
# v = ResistantVirus(0.0, 1.0, {}, 0.0)

# Check that mutProb is applied correctly in the reproduce step.
# v = ResistantVirus(1.0, 0.0, {'drug1':True, 'drug2': True, 'drug3': True, 'drug4': True, 'drug5': True, 'drug6': True}, 0.5)

# v = ResistantVirus(1.0, 0.0, {"drug2": True}, 1.0)

v = ResistantVirus(1.0, 0.0, {'drug1':True, 'drug2': True, 'drug3': True, 'drug4': True, 'drug5': True, 'drug6': True}, 0.5)
v.reproduce(0, [])
# Reproducing 10 times by calling v.reproduce(0, [])
# Checking the resistances of the children to each of the 6 prescriptions.
# Since mutProb = 0.5 and the parent virus was resistant to all 6 drugs,
#   we expect each child to be resistant to, on average, half of the six drugs.

print "\n================="
print "Created a new virus: \n", v
print "\nmaxBirthProb: ", v.maxBirthProb
print 'clearProb: ', v.clearProb
print 'mutProb: ', v.mutProb
print 'Dictionary of resistances: ', v.resistances
print "\n================="

# pdb.set_trace()
# Reproducing 10 times by calling v.reproduce(0, [])

# v.reproduce(popDensity, v.resistances)
# pdb.set_trace()
