import os                             # N'enlevez pas ces lignes.
os.chdir(os.path.dirname(__file__))   # Elles permettent de se positionner dans le répertoire de ce script

# Importez csv
import csv

 

# Regardez le contenu du fichier "Ex7 Lan Party.csv"
#          Observez que dans ce fichier, la première ligne comprends les en-têtes de colonne 
#                 Lan Party;Top 1;Top 2; Top 3
#          Top 1, Top 2 et Top 3 sont les jeux les plus populaires dans chaque Lan Party
#          
#          Vous aimez jouer à Valorant
#          Imprimez la liste des Lan Party dans lesquels votre jeu préféré est parmi leurs Tops
# 
#          Aucune instruction détaillée n'est donnée plus bas
fichier_a_lire = os.path.join("csvs","Ex7 Lan Party.csv")

with open(fichier_a_lire,"r",encoding="utf-8") as csv_file:
    lecteur = csv.reader(csv_file, delimiter=";")
    en_tete = next(lecteur)
    print(en_tete)
    for ligne in lecteur:
        if ligne[1] == "Valorant" or ligne[2] == "Valorant" or ligne[3] == "Valorant":
            print(ligne)


