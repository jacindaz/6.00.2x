class ResistantVirus(SimpleVirus):

    def __init__(self, maxBirthProb, clearProb, resistances, mutProb):
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
        for key in self.resistances:
            if drug == key:
                if self.resistances[key] == True:
                    return True

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
        drugs_resistance = self.resistantAllDrugs(activeDrugs)

        # if resistant to all drugs, is able to reproduce
        if drugs_resistance:
            prob_reproduce = random.random() * self.maxBirthProb * (1 - popDensity)

            # will reproduce: if prob of birth is 1 (guaranteed)
            #                 or if random_reproduce >= .5
            if (self.maxBirthProb == 1) or (prob_reproduce >= .5):
                offspring = ResistantVirus(self.maxBirthProb, self.clearProb, {}, self.mutProb)

                # if mutProb is 0
                if (self.mutProb == 0) or (prob_inherit_resistance >= .5):
                    # inherits parent resistances, doesn't mutate
                    offspring.resistances = self.resistances
                    return offspring

                # does not inherit parent resistances, does mutate
                elif (self.mutProb == 1) or (prob_inherit_resistance < .5):
                    new_resistances = newResistances(self.resistances, self.mutProb)
                    offspring.resistances = new_resistances
                    return offspring

            # if not resistant to all drugs, will not reproduce
            elif (self.maxBirthProb == 0) or (random_reproduce < .5):
                raise NoChildException

    def newResistances(self, current_resistances, mutProb):
        new_resistances = {}
        prob_inherit_resistance = random.random() * (1 - self.mutProb)

        for key,value in current_resistances:
            if (self.mutProb == 1) or (prob_inherit_resistance >= .5):
                new_resistances[key] = (not value)

            elif (self.mutProb == 0) or (prob_inherit_resistance < .5):
                new_resistances[key] = value

        return new_resistances


    def resistantAllDrugs(self, activeDrugs):
        for key, value in activeDrugs:
            if value == False:
                return False
        return True
