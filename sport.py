import csv
import os
from random import randint
import string
import time

from Classes_Exos import Exercice, Seance, Serie

class Sport_Coach_Generator():

    liste_widgets = []

    points = 1500
    liste_activites = []
    max_pts_exercice = 200
    min_pts_exercice = 100
    iterations_activite_max = 50
    pts_pour_pause = 500
    Seance_creation = Seance()  #Seance en cours de création
    

    def __init__(self):
        self.init_series()

    # Initialise des séries d'exercices à faire
    def init_series(self):
        with open('D:/Documents/Sport/sportcsv.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                #print (row)
                self.liste_activites += [row]

        serie = Serie()
        serie.add(
            Exercice("Jumping Jacks", 50),
            Exercice("Levers de genous", 50),
            Exercice("Crunchies", 20)
        )
        self.Seance_creation.add(serie)

        compteur_pour_faire_une_pause = 0
        serie = Serie()  #Utile pour ajouter a la var seance
        while self.points > 0:
            x = self.liste_activites[randint(0,len(self.liste_activites)-1)]
            points_a_enlever = randint(self.min_pts_exercice, self.max_pts_exercice)
            iterations_activite = points_a_enlever//int(x[1])
            if iterations_activite > self.iterations_activite_max:
                iterations_activite = self.iterations_activite_max
                points_a_enlever = iterations_activite * int(x[1])
            self.points -= points_a_enlever
            
            serie.add(Exercice(x[0], str(iterations_activite)))  #On ajoute l'exercice sélectionné a la série en création

            compteur_pour_faire_une_pause += points_a_enlever
            if compteur_pour_faire_une_pause > self.pts_pour_pause:

                self.Seance_creation.add(serie.copy()) #On ajoute la série créée à la séance
                serie = Serie()

                compteur_pour_faire_une_pause = 0

    def affichage_serie(self, serie : int):
        """
            Retourne a partir de l'id d'une série son affichage ligne par ligne
        """
        bloc_texte = []

        if (serie == 0):  #Cad si c'est l'échauffement
            bloc_texte.append(["ECHAUFFEMENT \n \n","Jumping Jacks : 50 \n","Levers de genous : 50 \n","Crunchies : 20 \n","------------------------------------- \n","LA CA VA CHIER \n"])
        else:
            for exercice in self.Seance_creation.liste_series[serie].liste_exos: #On rajoute ligne par ligne les exercices contenus dans la série
                print(exercice)
                bloc_texte.append(exercice.type_exo + " : " + str(exercice.iterations) + " \n")
            if (serie == len(self.Seance_creation.liste_series) - 1):  #Cad si c'est la dernière série
                bloc_texte.append("  \n ------------------------------------- \n FIN, place aux étirements ! \n")
            else:
                bloc_texte.append("Pause d'une minute ! \n  \n")
        return bloc_texte


    def output_txt(self):
        """
            Retourne la séance de sport en fichier txt
        """
        f = open("D:/Documents/Sport/output.txt", "w")

        f.write("ECHAUFFEMENT \n \n")
        f.write("Jumping Jacks : 50 \n")
        f.write("Levers de genous : 50 \n")
        f.write("Crunchies : 20 \n")
        f.write("  \n")
        f.write("------------------------------------- \n")
        f.write("LA CA VA CHIER \n")
        f.write("------------------------------------- \n")

        f.write("Pause d'une minute ! \n  \n")

        for bloc_serie in self.liste_affichage:
            for i in bloc_serie:
                f.write(i)
        
        f.write("  \n")
        f.write("------------------------------------- \n")
        f.write("FIN, place aux étirements ! \n")

        f.close()

    def open_output_file_notepad(self):
        osCommandString = "notepad.exe D:/Documents/Sport/output.txt"
        os.system(osCommandString)
