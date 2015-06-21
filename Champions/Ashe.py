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

class Ashe:
    """A class representation of the champion Ashe for DPS simulation."""

    def __init__(self, level):
        self.level = level
        self.ranks = {"Q" : 5, "W" : 5, "E" : 5, "R" : 3}

        #Gets the cooldown data.
        self.cd_mod = 1
        self.q_cd = Q_BASE * self.cd_mod
        self.w_cd = (W_BASE - W_LEVEL * self.ranks["W"]) * self.cd_mod

        self.crit = 0.00
        self.crit_damage = 1.00

    def ashe_calculator(self, duration):
        """Calculates the expected output of the Ashe.
        *Currently expects Ashe to open with a volley.
        *Currently expects Frost Shot to always be active."""
        pass

    def rangers_focus(self, rank):
        """Returns the damage modifier of Ranger's Focus.
        Advanced math to determine the Attack Speed component's effect.
        *Fuck that, for now."""
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
