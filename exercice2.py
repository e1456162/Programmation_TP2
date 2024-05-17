"""
exercice2.py

auteur: Cédric Vincent (e1456162)
date de création: < 2024 May 17 Fri >
environnement de développement GNU/Emacs

résumé du programme:
programme qui lit in fichier csv et retourne ses valeurs en tant qu'entrées dans un dictionnaire
"""

def lectureFichier(fichier:str)->dict:
    dictionnaire:dict = {}
    temp:list = []
    with open(fichier, "r") as f:
        lignes:list = f.readlines()
    for item in lignes:
        temp = (item.replace("\n","").split(","))
        dictionnaire.update({temp[0]:temp[1::]})
        print(dictionnaire)

lectureFichier("./pokemons.csv")
