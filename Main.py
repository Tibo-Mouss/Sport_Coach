# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

# Import a ajouter
import shelve
import sport
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer, QTime
from PyQt5.QtWidgets import QListWidgetItem
import time
import datetime

class Ui_MainWindow(object):

    coach_sport = sport.Sport_Coach_Generator()
    page_serie = 0
    start_timer = time.time()
    temps_passe = 0
    nb_series = 0 #Sera initialisé ensuite

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(471, 364)
        self.tabWidget = QtWidgets.QTabWidget(MainWindow)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 471, 361))
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.tabWidget.setFont(font)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.Label_bienvenue = QtWidgets.QLabel(self.tab)
        self.Label_bienvenue.setGeometry(QtCore.QRect(120, 50, 221, 101))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.Label_bienvenue.setFont(font)
        self.Label_bienvenue.setAlignment(QtCore.Qt.AlignCenter)
        self.Label_bienvenue.setObjectName("Label_bienvenue")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.B_NextSerie = QtWidgets.QPushButton(self.tab_2)
        self.B_NextSerie.setEnabled(True)
        self.B_NextSerie.setGeometry(QtCore.QRect(377, 310, 75, 23))
        self.B_NextSerie.setCheckable(False)
        self.B_NextSerie.setAutoDefault(True)
        self.B_NextSerie.setDefault(False)
        self.B_NextSerie.setFlat(False)
        self.B_NextSerie.setObjectName("B_NextSerie")
        self.B_PreviousSerie = QtWidgets.QPushButton(self.tab_2)
        self.B_PreviousSerie.setEnabled(True)
        self.B_PreviousSerie.setGeometry(QtCore.QRect(290, 310, 75, 23))
        self.B_PreviousSerie.setObjectName("B_PreviousSerie")
        self.LCD_Minutes = QtWidgets.QLCDNumber(self.tab_2)
        self.LCD_Minutes.setGeometry(QtCore.QRect(10, 310, 64, 23))
        self.LCD_Minutes.setObjectName("LCD_Minutes")
        self.LCD_Secondes = QtWidgets.QLCDNumber(self.tab_2)
        self.LCD_Secondes.setGeometry(QtCore.QRect(80, 310, 64, 23))
        self.LCD_Secondes.setObjectName("LCD_Secondes")
        self.B_SeriePret = QtWidgets.QPushButton(self.tab_2)
        self.B_SeriePret.setGeometry(QtCore.QRect(200, 160, 75, 23))
        self.B_SeriePret.setObjectName("B_SeriePret")
        self.textDisplaySeries = QtWidgets.QListWidget(self.tab_2)
        self.textDisplaySeries.setGeometry(QtCore.QRect(10, 40, 451, 261))
        self.textDisplaySeries.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textDisplaySeries.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textDisplaySeries.setAutoScroll(False)
        self.textDisplaySeries.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.textDisplaySeries.setDefaultDropAction(QtCore.Qt.IgnoreAction)
        self.textDisplaySeries.setItemAlignment(QtCore.Qt.AlignCenter)
        self.textDisplaySeries.setObjectName("textDisplaySeries")
        self.Label_phase_serie = QtWidgets.QLabel(self.tab_2)
        self.Label_phase_serie.setGeometry(QtCore.QRect(140, 0, 191, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Label_phase_serie.sizePolicy().hasHeightForWidth())
        self.Label_phase_serie.setSizePolicy(sizePolicy)
        self.Label_phase_serie.setAlignment(QtCore.Qt.AlignCenter)
        self.Label_phase_serie.setObjectName("Label_phase_serie")
        self.textDisplaySeries.raise_()
        self.B_NextSerie.raise_()
        self.B_PreviousSerie.raise_()
        self.LCD_Minutes.raise_()
        self.LCD_Secondes.raise_()
        self.B_SeriePret.raise_()
        self.Label_phase_serie.raise_()
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setEnabled(True)
        self.tab_3.setObjectName("tab_3")
        self.tableHistorique = QtWidgets.QTableWidget(self.tab_3)
        self.tableHistorique.setGeometry(QtCore.QRect(10, 10, 441, 311))
        self.tableHistorique.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableHistorique.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tableHistorique.setAutoScroll(False)
        self.tableHistorique.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableHistorique.setDragDropOverwriteMode(False)
        self.tableHistorique.setAlternatingRowColors(True)
        self.tableHistorique.setCornerButtonEnabled(False)
        self.tableHistorique.setRowCount(1)
        self.tableHistorique.setColumnCount(3)
        self.tableHistorique.setObjectName("tableHistorique")
        self.tableHistorique.horizontalHeader().setVisible(True)
        self.tableHistorique.horizontalHeader().setCascadingSectionResizes(False)
        self.tableHistorique.horizontalHeader().setDefaultSectionSize(210)
        self.tableHistorique.horizontalHeader().setHighlightSections(True)
        self.tableHistorique.horizontalHeader().setSortIndicatorShown(False)
        self.tableHistorique.horizontalHeader().setStretchLastSection(True)
        self.tableHistorique.verticalHeader().setVisible(False)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.tabWidget.addTab(self.tab_4, "")


        # Conectique du timer de la tab Série
        self.timer_du_timer = QTimer()
        self.timer_du_timer.timeout.connect(self.display_timer)
        self.timer_du_timer.start(1000)
        # Pour connecter le bouton previous à son action
        self.B_PreviousSerie.clicked.connect(self.b_previous_clicked)
        # Pour connecter le bouton next à son action
        self.B_NextSerie.clicked.connect(self.b_next_clicked)
        #Pour associer les appuis de la tab bar aux affichages
        self.tabWidget.tabBarClicked.connect(self.tab_bar_clicked)

        #Cache les elements la tab Série au débu pour juste afficher un bouton
        self.B_NextSerie.setHidden(True)
        self.B_PreviousSerie.setHidden(True)
        self.LCD_Minutes.setHidden(True)
        self.LCD_Secondes.setHidden(True)
        self.textDisplaySeries.setHidden(True)
        self.Label_phase_serie.setHidden(True)
        # Et on associe au bouton prêt le lancement du timer et l'affichage des elements
        self.B_SeriePret.clicked.connect(self.b_serie_pret)

        #Associe le clic sur le TextdisplaySeries à l'affiche de la vidéo correspondante
        self.textDisplaySeries.itemClicked.connect(self.display_video)
        

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def tab_bar_clicked(self, index : int) :
        if (index == 0): #Page d'acceuil
            pass
        elif (index == 1): #Page de sport
            pass
        elif (index == 2): #Historique
            # Pour afficher le contenu du tableau d'historiques
            self.affichage_historique()
        else:
            print("Euh problème chef pourquoi t'es nul ?")


    def affichage_historique(self):
        """
            Affiches l'historique
        """

        memoire = shelve.open('historique')
        seances = list(memoire.values())
        tailleHistorique = len(seances)
        self.tableHistorique.setRowCount(tailleHistorique)

        self.tableHistorique.setHorizontalHeaderLabels(["Date", "Temps", "Points"])
        header = self.tableHistorique.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
        
        for i in range(tailleHistorique):
            seance = seances[i]

            self.tableHistorique.setItem(i, 2, QtWidgets.QTableWidgetItem(str(seance.points)))
            temps_affiche = str(seance.temps // 60) + "min " + str(seance.temps % 60) + "s"
            self.tableHistorique.setItem(i, 1, QtWidgets.QTableWidgetItem(temps_affiche))
            self.tableHistorique.setItem(i, 0, QtWidgets.QTableWidgetItem(seance.jour))

        memoire.close()

    def affichage_b_pret(self, bp_hidden : bool):
        """ Affiche le bouton prêt et cache le reste (ou l'inverse, selon le booléen d'entrée)
        Si c'est true alors ça cache le bouton, et ça affiche tout le reste """
        self.B_NextSerie.setHidden( not(bp_hidden) )
        self.B_PreviousSerie.setHidden( not(bp_hidden) )
        self.LCD_Minutes.setHidden( not(bp_hidden) )
        self.LCD_Secondes.setHidden( not(bp_hidden) )
        self.textDisplaySeries.setHidden( not(bp_hidden) )
        self.Label_phase_serie.setHidden( not(bp_hidden) )
        self.B_SeriePret.setHidden( bp_hidden )

    def b_serie_pret(self):
        #On re affiche les elements de la tab
        self.affichage_b_pret(True)

        #On reinitialise le timer hop là
        self.start_timer = time.time()
        #Et on affiche 0 sur les deux LCD parce que il peu y avoir un ptit peu de retard
        self.LCD_Minutes.display(0)
        self.LCD_Secondes.display(0)

        #On initialise la série et remet le bon affichage de série
        self.coach_sport.init_seance1()
        #On enregistre en paramètre le nb de série dans cette séance
        self.nb_series = len(self.coach_sport.seance.liste_series)

        # Initialise le texte du display avec les échauffements
        self.display_serie(0)
        self.page_serie = 0



    # Bouton Next pour afficher la série suivante
    def b_next_clicked(self):
        if self.page_serie < self.nb_series - 1: #Si on est avant l'avant dernière série ça autorise de passer a la suivante
            self.page_serie += 1
            self.display_serie(self.page_serie)
        else: #Cad on a finit l'affichage de toute la séance, on appuit sur le bouton "J'ai finit !" --> ça enregistre la séance
            self.coach_sport.save_seance(self.temps_passe)
            #Ca re affiche le bouton pour commencer une nouvelle séance
            self.affichage_b_pret(False)
        
        if self.page_serie == len(self.coach_sport.seance.liste_series) - 1: #Si on est passé à la dernière page
            _translate = QtCore.QCoreApplication.translate
            self.B_NextSerie.setText(_translate("MainWindow", "J'ai fini !"))
    
    
    def b_previous_clicked(self):
        """ Bouton previous pour revenir à la série précédente """
        
        #Si avant c'était sur la dernière page alors on remet le texte du bouton next sur "Next"
        if self.page_serie == self.nb_series - 1:
            _translate = QtCore.QCoreApplication.translate
            self.B_NextSerie.setText(_translate("MainWindow", "Next !"))

        if self.page_serie > 0:
            self.page_serie -= 1
            self.display_serie(self.page_serie)

    def display_serie(self, indice_serie):
        """ Affiche la série de l'indice passé en paramètre """

        if (indice_serie == 0): #cad c'est l'échauffement
            self.Label_phase_serie.setText("ECHAUFFEMENT")
        elif (indice_serie < self.nb_series - 1): #entre l'échauffement et la dernière 
            self.Label_phase_serie.setText("LESSS Goooooo")
        else:
            self.Label_phase_serie.setText("On oublie pas les étirements à la fin !")

        # Clear l'affichage du GUI
        self.textDisplaySeries.clear()
        #Centre le texte, et faut le faire avant de print le texte
        #self.textDisplaySeries.setAlignment(QtCore.Qt.AlignCenter)

        # Récupère la série correspondante au n° de la page
        text_list = self.coach_sport.affichage_serie(self.page_serie)
        
        # Affiche la série sur le GUI
        for i in text_list:
            item = QListWidgetItem(i)
            item.setTextAlignment(QtCore.Qt.AlignCenter)
            #passer par item c'est pour centrer chaque élément
            self.textDisplaySeries.addItem(item)

    def display_video(self, item :QListWidgetItem):
        #print(item.text())
        #print(item.listWidget().indexFromItem(item).row())
        exercice = item.listWidget().indexFromItem(item).row()
        nom_video = self.coach_sport.get_video(self.page_serie, exercice)
        

    def display_timer(self):
        """ Affiche le timer sur la tab Série """
        currentTime = time.time()
        self.temps_passe = int(currentTime - self.start_timer)
        minutes = self.temps_passe // 60
        secondes = self.temps_passe % 60
        self.LCD_Minutes.display(minutes)
        self.LCD_Secondes.display(secondes)
        




    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Sport Coach"))
        self.Label_bienvenue.setText(_translate("MainWindow", "Coach Sport"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Menu"))
        self.B_NextSerie.setText(_translate("MainWindow", "Next !"))
        self.B_PreviousSerie.setText(_translate("MainWindow", "Previous"))
        self.B_SeriePret.setText(_translate("MainWindow", "Je suis Prêt !"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Séries"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Historique"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QDialog()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
