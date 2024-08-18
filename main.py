from patient import Patient
from hopital import Hopital
from medecin import Medecin
from personne import Personne
from personnelMedical import PersonnelMedical
from infirmier import Infirmier
from local import Local
from rendezvous import Rendezvous

# Création de l'hôpital
hopital = Hopital("Saint-justine")

# Création des patients
patient1 = Patient("ami", "ami", "12", 2658)
patient2 = Patient("amira", "akli", "18", 2656)
patient3 = Patient("dino", "akl", "6", 5621)


# Ajout des patients
hopital.ajouterPatient(patient1)
hopital.ajouterPatient(patient2)
hopital.ajouterPatient(patient3)

# Affichage des patients
print("\nListe des patients:")
hopital.afficherPatient()

#creation du personnel medical
infirmier1 = Infirmier("amira", "akli", "30", "365", "infirmiere", "les urgences " )
infirmier2 = Infirmier("maya", "hag", "35", "3125", "infirmiere", "cardio " )
medecin1 = Medecin("sam", "ali", 45, 5882, "cardiologue")
medecin2 = Medecin("faf", "miam", 65, 322, "neurologue")

# Ajout du personnel médical
hopital.ajouterPersonnel(infirmier1)
hopital.ajouterPersonnel(infirmier2)
hopital.ajouterPersonnel(medecin1)
hopital.ajouterPersonnel(medecin2)

# Affichage du personnel médical
print("\nListe du personnel médical:")
hopital.afficherPersonnel()

# Création des locaux
local1 = Local(101, "Consultation")
local2 = Local(202, "Chirurgie")

# Ajout des locaux
hopital.ajouterLocal(local1)
hopital.ajouterLocal(local2)

# Affichage des locaux
print("\nListe des locaux:")
hopital.afficherLocal()

# Création des rendez-vous
rdv1 = Rendezvous("2024-08-20", "10:00", patient1, medecin1, local1)
rdv2 = Rendezvous("2024-08-22", "14:00", patient2, medecin1, local2)
rdv3 = Rendezvous("2024-12-22", "4:00", patient2, medecin1, local2)
rdv4 = Rendezvous("2024-12-22", "4:00", patient1, medecin2, local1)

# Ajout des rendez-vous
hopital.ajouterRendezVous(rdv1)
hopital.ajouterRendezVous(rdv2)
hopital.ajouterRendezVous(rdv3)
hopital.ajouterRendezVous(rdv4)

# Affichage des rendez-vous
print("\nListe des rendez-vous:")
hopital.afficherRendezvous()

# Modifier un rendez-vous
hopital.modifierRendezvous(0, nouvelleDate="2024-08-21", nouvelleHeure="11:00")

# Afficher les rendez-vous après modification
print("\nListe des rendez-vous après modification:")
hopital.afficherRendezvous()

# Supprimer un rendez-vous
hopital.supprimerRendezvous(1)

# Afficher les rendez-vous après suppression
print("\nListe des rendez-vous après suppression:")
hopital.afficherRendezvous()

# Rechercher un rendez-vous par critère
print("\nRecherche de rendez-vous par date (2024-08-21):")
hopital.rechercherRendezvous("2024-08-21")

# Lister les rendez-vous d'un médecin spécifique
print("\nListe des rendez-vous du médecin sam :")
hopital.listerRendezvous_par_medecin("sam")

# Lister les rendez-vous d'un client spécifique
print("\nListe des rendez-vous du ptient ami:")
hopital.listerRendezvous_par_Patient("ami")

print(hopital)

