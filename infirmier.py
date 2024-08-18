from personnelMedical import PersonnelMedical


class Infirmier(PersonnelMedical):
    def __init__(self, nom, prenom, age, numEmploye, specialite, service):
        super().__init__(nom, prenom, age, numEmploye, specialite)
        self.service = service

    def __str__(self):
        return "[L'infirmier: " + self.nom + " " + self.prenom + ". service: " + self.service + "]"


