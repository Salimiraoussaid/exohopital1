from personnelMedical import PersonnelMedical


class Medecin(PersonnelMedical):
    def __init__(self, nom, prenom, age, numEmploye, specialite):
        super().__init__(nom, prenom, age, numEmploye, specialite)


    def __str__(self):
        return "[le medecin: " + self.nom + " " + self.prenom + " est un " + self.specialite + "]"