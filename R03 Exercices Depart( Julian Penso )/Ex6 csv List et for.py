import os                             # N'enlevez pas ces lignes.
os.chdir(os.path.dirname(__file__))   # Elles permettent de se positionner dans le répertoire de ce script

import csv


# Tu as toujours rêvé de travailler un jour pour le CH
# Tu as vu une job en TI, 
#           Analyste, soutien technique réseau

# Le fichier Ex3 Competences.csv contient la liste des compétences qu'ils demandent, 
# #         avec le niveau et le fait que cette compétence est exigée ou plutôt un atout
# Bien que tu n'as pas encore fini tes études tu veux imprimer ici les compétences qui sont exigées 
# afin de bien développer ces compétences pour qu'éventuellement tu puisses entrer dans cette entreprise

#  Si vous êtes à l'aise en programmation allez-y
#  Des instructions détaillées sont données plus bas


fichier_a_lire = os.path.join("csvs","Ex6 Competences.csv")
























# INSTRUCTIONS DÉTAILLÉES
#Ouvrez en lecture le fichier Ex6 Competences.csv
with open(fichier_a_lire,"r",encoding="utf-8") as csv_file:
#avec l'encodage et le delimiter requis
    lecteur = csv.reader(csv_file,delimiter="/")
#Imprimez la première ligne
    print(next(lecteur))
#Faites une boucle pour passer à travers chacune des lignes du fichier
    for ligne in lecteur:
#Si l'exigence est  'Exigé' imprimez cette ligne
        if ligne[2] == "Exigé":
            print(ligne)
