from abs.religions import religion
from chapitres.classes import philippe
from abs import situation
from abs.humanite import metier
from abs.univers import temps

class SituationPhilippe(situation.Situation):

    def __init__(self):
        situation.Situation.__init__(self, 435500)

    def AffichageArmee(self):
        # armée de philippe
        str = u""
        val = self.GetValCaracInt(philippe.Philippe.C_MILITAIRE)
        if val < 0:
            str = u"Armée insignifiante"
        elif val <= 2:
            str = u"Armée faible"
        elif val <= 4:
            str = u"Bonne armée"
        elif val <= 7:
            str = u"Armée puissante"
        elif val <= 10:
            str = u"Armée redoutable"
        else:
            str = u"Armée invincible"
        return str
