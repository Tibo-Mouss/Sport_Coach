import csv
import os
from random import randint
import string
import time

class Sport_Coach_Generator():

    liste_widgets = []

    points = 1500
    liste = []
    max_pts_exercice = 200
    min_pts_exercice = 100
    iterations_activite_max = 50
    pts_pour_pause = 500
    liste_affichage = []

    def __init__(self):
        self.init_series()

    # Initialise des séries d'exercices à faire
    def init_series(self):
        with open('D:/Documents/Sport/sportcsv.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                #print (row)
                self.liste += [row]

        self.liste_affichage.append(["ECHAUFFEMENT \n \n","Jumping Jacks : 50 \n","Levers de genous : 50 \n","Crunchies : 20 \n","------------------------------------- \n","LA CA VA CHIER \n"])


        compteur_pour_faire_une_pause = 0
        bloc_text = []
        while self.points > 0:
            x = self.liste[randint(0,len(self.liste)-1)]
            points_a_enlever = randint(self.min_pts_exercice, self.max_pts_exercice)
            iterations_activite = points_a_enlever//int(x[1])
            if iterations_activite > self.iterations_activite_max:
                iterations_activite = self.iterations_activite_max
                points_a_enlever = iterations_activite * int(x[1])
            self.points -= points_a_enlever
            texte = x[0] + " : " + str(iterations_activite) + " \n"
            bloc_text.append(texte)

            compteur_pour_faire_une_pause += points_a_enlever
            if compteur_pour_faire_une_pause > self.pts_pour_pause:
                bloc_text.append("Pause d'une minute ! \n  \n")

                self.liste_affichage.append(bloc_text)
                bloc_text = []
                compteur_pour_faire_une_pause = 0

        self.liste_affichage.append("  \n ------------------------------------- \n FIN, place aux étirements ! \n")
    
    def output_txt(self):
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
