import os                             # N'enlevez pas ces lignes.
os.chdir(os.path.dirname(__file__))   # Elles permettent de se positionner dans le répertoire de ce script

# Importez csv
import csv

 

# Vous utiliserez encore le fichier "Ex7 Lan Party.csv"
# 
#         Créez une liste des jeux joués dans les différents Lan Party du fichier.
#         N'ajoutez à cette liste chaque jeu qu'une seule fois 
#                         (vérifiez si le jeu est dans la liste avant de l'ajouter
#                          vous pouvez vérifier avec l'instruction 'in'
#         Triez la liste en ordre aphabétique 
#         Finalement, imprimez la liste des différents jeux joués triés en ordre alphabétique


#         Si besoin, des instructions détaillées sont données plus bas























# INSTRUCTIONS DÉTAILLÉES
#      Commencez par créer une liste des différents jeux vide
liste_jeux = ["Valorant","CS:GO","Call of Duty:Modern Warfare","Dota 2","League of Legends",
              "Warzone","Rocket League","Fortnite","Rainbow Six Siege","Among Us"]
#      Ouvrez le fichier 'Ex4 Lan Party.csv' en lecture
fichier_a_lire = os.path.join("csvs","Ex7 Lan Party.csv")
with open(fichier_a_lire,"r",encoding="utf-8") as csv_file: 
#      utilisez csv.reader pour lire le fichier avec le bon delimiter
    lecteur = csv.reader(csv_file, delimiter=";")
#      Sautez la première ligne de l'entête
    en_tete = next(lecteur)
#      Faites une boucle pour passer à travers chacune des lignes 
    for ligne in lecteur:
#      Utilisez le slicing pour garder uniquement les 3 jeux
        new_ligne = ligne[1:3]
        
            
#      Faites une boucle pour passer à travers chacun des jeux
        for jeu in new_ligne:
#      Avec count, obtenez le nombre de fois que le jeu est dans votre liste des différents jeux
            nb_jeu_dans_liste = liste_jeux.count(jeu)
            print(f"Le nombre de fois que le jeu {jeu} est dans ma liste est de {nb_jeu_dans_liste}.")
            
            
#      Si le count est de 0, vous ne l'avez jamais ajouté alors ajoutez le jeu à votre liste
            if nb_jeu_dans_liste == 0:
                liste_jeux.append(jeu)
                print(f"le jeu suivant : {jeu} à été ajouté a la liste {liste_jeux}.")
#      En dehors de toute boucle, utilisez sorted() pour trier la liste et obtenir une nouvelle liste triée
#      Imprimez votre nouvelle liste triée
sorted(liste_jeux)
print(liste_jeux)

