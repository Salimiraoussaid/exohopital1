from personne import Personne

class Patient(Personne):
    def __init__(self, nom, prenom, age, numPatient):
        super().__init__(nom, prenom, age)
        self.numPatient = numPatient

    def __str__(self):
        return "[" + self.nom + " " + self.prenom + " " + str(self.numPatient) + "]"
