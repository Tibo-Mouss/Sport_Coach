import csv
from random import randint
import time

points = 1500
liste = []

with open('D:/Documents/Sport/sportcsv.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        #print (row)
        liste += [row]

f = open("D:/Documents/Sport/output.txt", "w")


f.write("ECHAUFFEMENT \n \n")
f.write("Jumping Jacks : 50 \n")
f.write("Levers de genous : 50 \n")
f.write("Crunchies : 20 \n")
f.write("  \n")
f.write("------------------------------------- \n")
f.write("LA CA VA CHIER \n")
f.write("------------------------------------- \n")
compteur_pour_faire_une_pause = 0
while points >0:
    x = liste[randint(0,len(liste)-1)]
    points_a_enlever = randint(100,200)
    iterations_activite = points_a_enlever//int(x[1])
    if iterations_activite > 50:
        iterations_activite = 50
        points_a_enlever = iterations_activite * int(x[1])
    points -= points_a_enlever
    texte = x[0] + " : " + str(iterations_activite) + " \n"
    f.write(texte)

    compteur_pour_faire_une_pause += points_a_enlever
    if compteur_pour_faire_une_pause > 500:
        f.write("Pause d'une minute ! \n  \n")
        compteur_pour_faire_une_pause = 0

f.write("  \n")
f.write("------------------------------------- \n")
f.write("FIN, place aux étirements ! \n")

f.close()
print("C'est fait chef !")
time.sleep(2)
