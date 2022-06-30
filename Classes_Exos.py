"""
    Définit les classes utiles pour représenter une séance de sport
"""



from enum import Enum


class Exercice:

    iterations = 0
    type_exo = ""

    def __init__(self, type_ex : str, it : int):
        self.iterations = it
        self.type_exo = type_ex


class Serie:
    """
        C'est une liste d'exercices
    """

    liste_exos = []

    def __init__(self, *liste) -> None:
        for i in liste:
            self.liste_exos.append(i)

    def __init__(self) -> None:
        pass

    def add(self, *exos):
        for i in exos:
            self.liste_exos.append(i)

    def copy(self):
        serie = Serie()
        serie.add(self.liste_exos)
        return serie
        


class Seance:
    """
        C'est une liste de series, comprenant l'intro mais pas l'outro, qui sera seulement apparente à l'affichage
    """

    liste_series = []
    temps = 0

    def __init__(self, liste, temps_pris : int) -> None:
        self.liste_series = liste
        self.temps = temps_pris

    def __init__(self) -> None:
        liste_series = []
        temps = 0

    def add(self, *seances):
        for i in seances:
            self.liste_series.append(i)

