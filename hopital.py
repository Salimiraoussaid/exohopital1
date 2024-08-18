class Hopital:
    def __init__(self, nom):
        self.nom = nom
        self.listePatients = []
        self.listePersonnel = []
        self.listeLocaux = []
        self.listeRendezVous = []

    # Méthode pour Ajouter un patient
    def ajouterPatient(self, patient):
        self.listePatients.append(patient)

    # Méthode pour Ajouter un personnel medical
    def ajouterPersonnel(self, personnelMedical):
        self.listePersonnel.append(personnelMedical)

    # Méthode pour Ajouter un local
    def ajouterLocal(self, local):
        self.listeLocaux.append(local)

    # Méthode pour Ajouter un rendez-vous
    def ajouterRendezVous(self, rendezVous):
        self.listeRendezVous.append(rendezVous)


    # Méthode pour supprimer un rendez-vous
    def supprimerRendezvous(self, index):
        if 0 <= index < len(self.listeRendezVous):
            del self.listeRendezVous[index]
        else:
            print("Rendez-vous non trouvé.")

    # Méthode pour modifier un rendez-vous
    def modifierRendezvous(self, index, nouvelleDate=None, nouvelleHeure=None, nouveauClient=None, nouveauMedecin=None,
                           nouveauLocal=None):
        if 0 <= index < len(self.listeRendezVous):
            rdv = self.listeRendezVous[index]
            if nouvelleDate:
                rdv.date = nouvelleDate
            if nouvelleHeure:
                rdv.heure = nouvelleHeure
            if nouveauClient:
                rdv.client = nouveauClient
            if nouveauMedecin:
                rdv.medecin = nouveauMedecin
            if nouveauLocal:
                rdv.local = nouveauLocal
        else:
            print("Rendez-vous non trouvé.")

    # Méthode pour rechercher un rendez-vous
    def rechercherRendezvous(self, critere):
        resultats = [rdv for rdv in self.listeRendezVous if
                     critere in (rdv.date, rdv.heure, rdv.patient.nom, rdv.medecin.nom)]
        if resultats:
            for rdv in resultats:
                print(rdv)
        else:
            print("Aucun rendez-vous trouvé pour ce critère.")
        # Méthode pour lister les rendez-vous d'un médecin spécifique

    def listerRendezvous_par_medecin(self, nomMedecin):
        rdvsMedecin = [rdv for rdv in self.listeRendezVous if rdv.medecin.nom == nomMedecin]
        if rdvsMedecin:
            for rdv in rdvsMedecin:
                print(rdv)
        else:
            print(f"Aucun rendez-vous trouvé pour le médecin {nomMedecin}.")

    # Méthode pour Afficher la liste des patients
    def afficherPatient(self):
        for patient in self.listePatients:
            print(patient)

    # Méthode pour Afficher la liste de personnel medical
    def afficherPersonnel(self):
        for personnel in self.listePersonnel:
            print(personnel)

    # Méthode pour Afficher la liste des locaux
    def afficherLocal(self):
        for local in self.listeLocaux:
            print(local)

    # Méthode pour Afficher la liste des rendez-vous
    def afficherRendezvous(self):
        for rendezVous in self.listeRendezVous:
            print(rendezVous)

    def listerRendezvous_par_Patient(self, nomPatient):
        rdvsPatient = [rdv for rdv in self.listeRendezVous if rdv.patient.nom == nomPatient]
        if rdvsPatient:
            for rdv in rdvsPatient:
                print(rdv)
        else:
            print(f"Aucun rendez-vous trouvé pour le client {nomPatient}.")

    def __str__(self):
        return f"Hopital: {self.nom}, Nombre de patients: {len(self.listePatients)}, Personnel: {len(self.listePersonnel)}, Locaux: {len(self.listeLocaux)}, Rendez-vous: {len(self.listeRendezVous)}"







