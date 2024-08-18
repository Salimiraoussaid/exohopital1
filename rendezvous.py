class Rendezvous:
    def __init__(self, date, heure, patient, medecin, local):
        self.date = date
        self.heure = heure
        self.patient = patient
        self.medecin = medecin
        self.local = local

    def __str__(self):
        return f'Le patient: {self.patient.nom} a un rdv le {self.date} à {self.heure} avec {self.medecin.nom} dans le local {self.local.numero}'

