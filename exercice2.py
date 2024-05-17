"""
exercice2.py

auteur: Cédric Vincent (e1456162)
date de création: < 2024 May 17 Fri >
environnement de développement GNU/Emacs

résumé du programme:
programme qui lit in fichier csv et retourne ses valeurs en tant qu'entrées dans un dictionnaire
"""

def fichierVersDict(fichier:str)->dict:
    #===== Variables de travail =====#
    dictionnaire:dict = {}
    temp:list = []
    #===== Traitement sur le fichier =====#
    with open(fichier, "r") as f:
        lignes:list = f.readlines()
    for chaineCaracteres in lignes:
        temp = (chaineCaracteres.replace("\n","").split(",")) # Conversion chaine de caractères vers liste
        for i in range(1,len(temp)):
            temp[i] = float(temp[i]) # Conversion string vers float des entrées numériques
        dictionnaire.update({temp[0]:temp[1::]}) # Création du dictionnaire {Pokemon:[stats]}
    return dictionnaire

print(fichierVersDict("./pokemons.csv")) #affichage du return de la fonction en tant que test
