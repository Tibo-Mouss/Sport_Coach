import csv
import os
from random import randint
import string
import time
import shelve

from Classes_Exos import Exercice, Seance, Serie

class Sport_Coach_Generator():

    liste_exercices = []
    """ Liste des exercices disponibles avec leur pts du style : [ [str : Exercice, str : points] ] """
    types_exercices = []
    """ Liste les parties du corps sur lesquelles les exercices peuvent se focus """

    # ----- Système d'initialisation avec points -----
    points_depenses = 1500
    """ Points dépensés pendant une séance (+/-) """
    max_pts_exercice = 200
    """ Borne supérieure de l'intervalle de pts qu'un exercice peut prendre """
    min_pts_exercice = 100
    """ Borne inférieure de l'intervalle de pts qu'un exercice peut prendre """
    iterations_activite_max = 50
    """ Limite d'itérations d'un exercice """
    pts_pour_pause = 500
    """ Limite de pts pour déclencher une pause """
    

    # ----- Système d'initialisation sans points apparents -----
    exercices_par_serie = 4
    nombre_series = 3

    
    
    seance = Seance()
    """ Seance en cours de création """
    cle_bdd = 0
    """ Clé de la séance pour la récuprérer dans la bdd (jsp si ce sera utile)"""
    

    def __init__(self):
        self.extraction_donnes_csv()
        print(self.types_exercices)

    def extraction_donnes_csv(self):
        """ Extrait toutes les données du fichier csv """
        dirname = os.path.dirname(__file__)
        filename = os.path.join(dirname, 'sportcsv.csv')

        with open(filename) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                self.liste_exercices += [row]
                
                #On créée la liste des types d'exos qui existent
                liste_types = row[3:]
                for i in liste_types:
                    if (i == ""):
                        pass
                    elif not (i in self.types_exercices) :
                        self.types_exercices.append(i)



    def init_seance1(self):
        """
            Initialise des séries d'exercices à faire
        """

        #Ajout de l'échauffement à la séance
        serie = Serie()
        serie.add(
            Exercice("Jumping Jacks", 50),
            Exercice("Levers de genous", 50),
            Exercice("Crunchies", 20)
        )
        self.seance.add(serie)

        points = self.points_depenses
        compteur_pour_faire_une_pause = 0
        serie = Serie()  #Utile pour ajouter a la var seance
        while points > 0:
            exercice_choisi = self.liste_exercices[randint(0,len(self.liste_exercices)-1)]
            points_a_enlever = randint(self.min_pts_exercice, self.max_pts_exercice)
            iterations_activite = points_a_enlever//int(exercice_choisi[1])
            if iterations_activite > self.iterations_activite_max:
                iterations_activite = self.iterations_activite_max
                points_a_enlever = iterations_activite * int(exercice_choisi[1])
            points -= points_a_enlever
            
            serie.add(Exercice(exercice_choisi[0], str(iterations_activite)))  #On ajoute l'exercice sélectionné a la série en création

            compteur_pour_faire_une_pause += points_a_enlever
            if compteur_pour_faire_une_pause > self.pts_pour_pause:

                self.seance.liste_series.append(serie.copy()) #On ajoute la série créée à la séance
                serie.clear()

                compteur_pour_faire_une_pause = 0

    
    def init_seance2(self):
        """
            Deuxieme version d'initialisation
        """

        #Ajout de l'échauffement à la séance
        serie = Serie()
        serie.add(
            Exercice("Jumping Jacks", 50),
            Exercice("Levers de genous", 50),
            Exercice("Crunchies", 20)
        )
        self.seance.add(serie)

        serie = Serie()  #Utile pour ajouter a la var seance
        for i in range(self.nombre_series):
            for i in range(self.exercices_par_serie):
                exercice_choisi = self.liste_exercices[randint(0,len(self.liste_exercices)-1)]

                points_a_enlever = randint(self.min_pts_exercice, self.max_pts_exercice)
                iterations_activite = points_a_enlever//int(exercice_choisi[1])
                if iterations_activite > self.iterations_activite_max:
                    iterations_activite = self.iterations_activite_max
                    points_a_enlever = iterations_activite * int(exercice_choisi[1])

                serie.add(Exercice(exercice_choisi[0], str(iterations_activite)))  #On ajoute l'exercice sélectionné a la série en création

            self.seance.liste_series.append(serie.copy()) #On ajoute la série créée à la séance
            serie.clear()


    def affichage_serie(self, serie : int):
        """
            Retourne a partir de l'id d'une série son affichage ligne par ligne
        """
        bloc_texte = []

        if (serie == 0):  #Cad si c'est l'échauffement
            bloc_texte = ["Jumping Jacks : 50 \n","Levers de genous : 50 \n","Crunchies : 20 \n"]
        else:
            for exercice in self.seance.liste_series[serie].liste_exos: #On rajoute ligne par ligne les exercices contenus dans la série
                bloc_texte.append(exercice.type_exo + " : " + str(exercice.iterations) + " \n")
            if (serie == len(self.seance.liste_series) - 1):  #Cad si c'est la dernière série
                bloc_texte.append("  \n ------------------------------------- \n FIN, place aux étirements ! \n")
            else:
                bloc_texte.append("Pause d'une minute ! \n  \n")
        return bloc_texte

    
    def get_video(self, serie: int, exercice : int):
        """ return le nom de la vidéo correspondant à l'exercice pointé """
        nom_exercice = self.seance.liste_series[serie].liste_exos[exercice].type_exo
        liste_noms_exercices = [i[0] for i in self.liste_exercices]
        index_exo = liste_noms_exercices.index(nom_exercice)
        return self.liste_exercices[index_exo][2]


    def save_seance(self,temps : int):
        """
            Sauvegarde la séance dans la base de données.
            Les clés utilisees dans la bdd sont juste des entiers qui augmentent au fur et a mesure.
        """
        memoire = shelve.open('historique')

        liste_cles_str = memoire.keys()
        print(liste_cles_str)
        liste_cles_int = [int(x) for x in liste_cles_str]

        try:
            nouvelle_cle = max(liste_cles_int) + 1
        except:
            nouvelle_cle = 1

        self.cle_bdd = nouvelle_cle

        self.seance.temps = temps
        self.seance.points = self.points_depenses
        memoire[str(nouvelle_cle)] = self.seance #Sauvegarde dans la BdD

        memoire.close()


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
