import os                             # N'enlevez pas ces lignes.
os.chdir(os.path.dirname(__file__))   # Elles permettent de se positionner dans le répertoire de ce script

# Importez csv
import csv

 

# Vous utiliserez encore le fichier "Ex7 Lan Party.csv"
# 
#         Vous voulez créer un dossier par Lan Party
#         Et pour chaque Lan Party, créez des sous-dossier pour chaque jeu
#                   (On y mettra éventuellement la liste des participants du Lan qui veulent jouer à ce jeu)
#         ATTENTION: Pour le nom de chaque jeu: changez le ':' pour un '_' et gardez juste les 20 premiers caractères

#         Si besoin, des instructions détaillées sont données plus bas























# INSTRUCTIONS DÉTAILLÉES
#      Commencez par créer une liste des différents jeux vide
liste_jeux = []
#      Ouvrez le fichier 'Ex4 Lan Party.csv' en lecture
fichier_a_lire = os.path.join("csvs","Ex7 Lan Party.csv")
with open(fichier_a_lire,"r",encoding="utf-8") as csv_file: 
#      utilisez csv.reader pour lire le fichier avec le bon delimiter
    lecteur = csv.reader(csv_file, delimiter=";")

#      Sautez la première ligne de l'entête
    en_tete = next(lecteur)
#      Faites une boucle pour passer à travers chacune des lignes 
    for ligne in lecteur:
#      Créez un dossier pour le nom du Lan Party
        os.mkdir(f"{ligne[0]}")
#      Déplacez vous dans ce dossier
        os.chdir(f"{ligne[0]}")
#      Utilisez le slicing pour garder uniquement les 3 jeux
        nouvelle_ligne = ligne[1:3]
#      Faites une boucle pour passer à travers chacun des jeux
        for jeu in nouvelle_ligne:
#      Pour le nom de chaque jeu: changez le ':' pour un '_' et gardez juste les 20 premiers caractères
            new_name = jeu.replace(":","_")[0:20]


#      Créez un dossier pour le jeu avec le nouveau nom de jeu
        if new_name not in nouvelle_ligne:
            os.mkdir(new_name)
#      Revenez au dossier parent
            os.chdir("C:\\Users\\6288022\\Documents\\GitHub\\H25-2N6-DemoGit-Julian-Andres-Penso-Rodriguez\\R03 Exercices Depart( Julian Penso )")
            


