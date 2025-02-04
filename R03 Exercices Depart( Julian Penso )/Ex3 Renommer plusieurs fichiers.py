# importez os
import os
# # allez dans le dossier Ex3 Videos
os.chdir("C:\\Users\\6288022\\Desktop\\R03 Exercices Depart\\Ex3 Videos\\")
# # avec la boucle for, passez à travers chacun des dossiers de os.listdir()
for liseur in os.listdir():
    print(liseur)
# #     utilisez os.path.splitext pour obtenir le filename et l'extension
    filename_extension = os.path.splitext(liseur)
    print(os.path.splitext(liseur))

# #     utilisez split sur le filename pour obtenir le titre, le cours et le numéro du cours
    filename_separe = filename_extension[0].split('_')
    print(filename_separe[0], filename_separe[1], filename_separe[2])
# #     utilisez strip pour enlever les espaces qui pourraient rester pour le titre et le numéro
    
    filename_separe[0] = filename_separe[0].strip()

# #     en plus utilisez zfill pour remplir le numéro de sorte que 1 deviendra 01
    filename_separe[2] = filename_separe[2].zfill(1)
# #     recréez le nouveau nom de fichier#   utliser os.rename pour renommer le fichier
os.chdir("C:\\Users\\6288022\\Desktop\\R03 Exercices Depart\\")
os.rename("Ex3 Videos", "Videos")
