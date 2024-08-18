class Personne:
    def __init__(self, nom, prenom, age):
        self.nom = nom
        self.prenom = prenom
        self.age = age

    def __str__(self):
        return "[" + self.nom + " " + self.prenom + " " + str(self.age) + "]"
