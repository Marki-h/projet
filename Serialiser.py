from Classe_Étudiant import *

# sérialiser l'objet instancié
etud = Etudiant("1234567", "Hasna", "Informatique")
etud.serialiser("FichierSerialiser1.json")

# Désérialisation
etud1 = Etudiant()

etud1.deserialiser("FichierSerialiser1.json")

print(etud1)
