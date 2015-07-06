"""
Ashe.py - A class containing the basic statistics of an Ashe
"""

BASE_AD = 51.088
BASE_AS = .658
AD_LEVEL = 2.85
AS_LEVEL = .0333

Q_BASE = 18
W_BASE = 12
W_LEVEL = 2

MAX_RANKS = {"Q" : 5, "W" : 5, "E" : 5, "R" : 3}

#Masteries are a list of tuples containing the value of the rune and the stat it affects
BASIC_GLYPHS = [0, 0, 0, 0, 0, 0, 0, 0, 0]
BASIC_MARKS = [0, 0, 0, 0, 0, 0, 0, 0, 0]
BASIC_SEALS = [0, 0, 0, 0, 0, 0, 0, 0, 0]
BASIC_QUINTS = [0, 0, 0]
BASIC_MASTERIES = None

class Ashe:
    """A class representation of the champion Ashe for DPS simulation."""

    def __init__(self, level = 18, ranks = MAX_RANKS, cdr = 0, crit = 0.00, crit_damage = 1.00):
        self.level = level
        self.ranks = ranks

        #Gets the cooldown data.
        self.cd_mod = 1 - cdr / 100
        self.q_cd = Q_BASE * self.cd_mod
        self.w_cd = (W_BASE - W_LEVEL * self.ranks["W"]) * self.cd_mod

        self.crit = crit
        self.crit_damage = crit_damage

    def ashe_calculator(self, duration):
        """Calculates the expected output of the Ashe.
        *Currently expects Ashe to open with a volley.
        *Currently expects Frost Shot to always be active.
        *Does not account for armor penetration yet."""
        pass

    def update(self):
        """Increments the simulator by 0.01 seconds and checks cooldowns to see if any action can be taken."""
        pass

    def rangers_focus(self, rank):
        """Returns the damage modifier of Ranger's Focus.
        Advanced math to determine the Attack Speed component's effect.
        *Fuck that, for now."""

        #Ashe has a cooldown between attack periods.
        #When gaining a new attack speed, figure out the time (in hundredths of seconds)
        #between attacks, subtract the already elapsed time, and set that to the new attack cooldown. 
        #If attack CD is negative, trigger an attack and reset the CD timer
        pass

    def volley(self, rank, targets_hit):
        """Returns the damage done by a given Ashe's Volleys."""
        return (5 + 15 * rank + self.get_ad()) * targets_hit

    def get_ad(self):
        """Returns Ashe's total Attack Damage."""
        return BASE_AD + AD_LEVEL * (self.level - 1)

    def get_as(self):
        """Returns Ashe's current Attack Speed in attacks per second."""
        return (1 + AS_LEVEL * (self.level - 1)) * BASE_AS

    def get_crit(self):
        """Returns Ashe's current critrate as a float."""
        return self.crit

    def get_crit_damage(self):
        """Reutrns Ashe's current critical damage modifier as a float."""
        return self.crit_damage

    def get_cdr(self):
        """Returns Ashe's current cooldown reduction modifier as a float."""
        return 1 - self.cd_mod

if __name__ == "__main__":
    print "Run Tracker.py to generate a new Ashe. Feature to call directly will come later."
