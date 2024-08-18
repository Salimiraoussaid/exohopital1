from personne import Personne


class PersonnelMedical(Personne):
    def __init__(self, nom, prenom, age, numEmploye, specialite):
        super().__init__(nom, prenom, age)
        self.numEmploye = numEmploye
        self.specialite = specialite

    def __str__(self):
        return "[" + self.nom + " "+ self.prenom + " " + str(self.numEmploye) + " "+ self.specialite + "]"

