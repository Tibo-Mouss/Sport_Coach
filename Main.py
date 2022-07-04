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
import time
import datetime

class Ui_MainWindow(object):

    # A Ajouter
    coach_sport = sport.Sport_Coach_Generator()
    page_serie = 0
    start_timer = time.time()
    temps_passe = 0

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(471, 353)
        self.tabWidget = QtWidgets.QTabWidget(MainWindow)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 471, 361))
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.tabWidget.setFont(font)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.Label_bienvenue = QtWidgets.QLabel(self.tab)
        self.Label_bienvenue.setGeometry(QtCore.QRect(160, 50, 141, 51))
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
        self.textDisplaySeries = QtWidgets.QTextBrowser(self.tab_2)
        self.textDisplaySeries.setGeometry(QtCore.QRect(10, 10, 441, 281))
        self.textDisplaySeries.setAutoFillBackground(False)
        self.textDisplaySeries.setObjectName("textDisplaySeries")
        self.B_NextSerie = QtWidgets.QPushButton(self.tab_2)
        self.B_NextSerie.setEnabled(True)
        self.B_NextSerie.setGeometry(QtCore.QRect(377, 300, 75, 23))
        self.B_NextSerie.setCheckable(False)
        self.B_NextSerie.setAutoDefault(True)
        self.B_NextSerie.setDefault(False)
        self.B_NextSerie.setFlat(False)
        self.B_NextSerie.setObjectName("B_NextSerie")
        self.B_PreviousSerie = QtWidgets.QPushButton(self.tab_2)
        self.B_PreviousSerie.setGeometry(QtCore.QRect(290, 300, 75, 23))
        self.B_PreviousSerie.setObjectName("B_PreviousSerie")
        self.LCD_Minutes = QtWidgets.QLCDNumber(self.tab_2)
        self.LCD_Minutes.setGeometry(QtCore.QRect(10, 300, 64, 23))
        self.LCD_Minutes.setObjectName("LCD_Minutes")
        self.LCD_Secondes = QtWidgets.QLCDNumber(self.tab_2)
        self.LCD_Secondes.setGeometry(QtCore.QRect(80, 300, 64, 23))
        self.LCD_Secondes.setObjectName("LCD_Secondes")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setEnabled(True)
        self.tab_3.setObjectName("tab_3")
        self.tableHistorique = QtWidgets.QTableWidget(self.tab_3)
        self.tableHistorique.setGeometry(QtCore.QRect(10, 10, 441, 311))
        self.tableHistorique.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableHistorique.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.tableHistorique.setCornerButtonEnabled(False)
        self.tableHistorique.setRowCount(1)
        self.tableHistorique.setColumnCount(3)
        self.tableHistorique.setObjectName("tableHistorique")
        self.tableHistorique.horizontalHeader().setVisible(False)
        self.tableHistorique.horizontalHeader().setCascadingSectionResizes(False)
        self.tableHistorique.horizontalHeader().setDefaultSectionSize(210)
        self.tableHistorique.horizontalHeader().setHighlightSections(True)
        self.tableHistorique.horizontalHeader().setSortIndicatorShown(False)
        self.tableHistorique.horizontalHeader().setStretchLastSection(True)
        self.tableHistorique.verticalHeader().setVisible(False)
        self.tabWidget.addTab(self.tab_3, "")


        # Conectique du timer de la tab Série
        self.timer_du_timer = QTimer()
        self.timer_du_timer.timeout.connect(self.display_timer)
        self.timer_du_timer.start(1000)
        # Initialise le texte du display avec les échauffements
        self.display_serie(0)
        # Pour connecter le bouton previous à son action
        self.B_PreviousSerie.clicked.connect(self.b_previous_clicked)
        # Pour connecter le bouton next à son action
        self.B_NextSerie.clicked.connect(self.b_next_clicked)
        # Pour afficher le contenu du tableau d'historiques
        self.affichage_historique()

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


        

    def affichage_historique(self):
        """
            Affiches l'historique
        """

        memoire = shelve.open('historique')
        seances = list(memoire.values())
        tailleHistorique = len(seances)
        self.tableHistorique.setRowCount(tailleHistorique)
        
        for i in range(tailleHistorique):
            seance = seances[i]

            self.tableHistorique.setItem(i, 1, QtWidgets.QTableWidgetItem(str(seance.jour)))

        memoire.close()


    # Bouton Next pour afficher la série suivante
    def b_next_clicked(self):
        if self.page_serie < len(self.coach_sport.seance.liste_series) - 1: #Si on est avant l'avant dernière série ça autorise de passer a la suivante
            self.page_serie += 1
            self.display_serie(self.page_serie)
        else: #Cad on a finit l'affichage de toute la séance, on appuit sur le bouton "J'ai finit !" --> ça enregistre la séance
            self.coach_sport.save_seance(self.temps_passe)
        
        if self.page_serie == len(self.coach_sport.seance.liste_series) - 1: #Si on est passé à la dernière page
            _translate = QtCore.QCoreApplication.translate
            self.B_NextSerie.setText(_translate("MainWindow", "J'ai fini !"))
    
    
    def b_previous_clicked(self):
        """ Bouton previous pour revenir à la série précédente """
        
        #Si avant c'était sur la dernière page alors on remet le texte du bouton next sur "Next"
        if self.page_serie == len(self.coach_sport.seance.liste_series) - 1:
            _translate = QtCore.QCoreApplication.translate
            self.B_NextSerie.setText(_translate("MainWindow", "Next !"))

        if self.page_serie > 0:
            self.page_serie -= 1
            self.display_serie(self.page_serie)

    def display_serie(self, indice_serie):
        # Clear l'affichage du GUI
        self.textDisplaySeries.clear()
        #Centre le texte, et faut le faire avant de print le texte
        self.textDisplaySeries.setAlignment(QtCore.Qt.AlignCenter)

        # Récupère la série correspondante au n° de la page
        text_list = self.coach_sport.affichage_serie(self.page_serie)
        
        # Affiche la série sur le GUI
        for i in text_list:
            self.textDisplaySeries.insertPlainText(i)

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
