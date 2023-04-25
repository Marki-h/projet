from Classe_Étudiant import *
from classLocal import *
from listeview_dialog import *
from local_dialog import *

# importer toutes les interfaces (.py)
import code_interface_scolarité
import ListeView
import interface_local

# importer module sys
import sys

# importer librairie QtWidgets et QtDesigner
from PyQt5 import QtWidgets
from PyQt5.QtGui import QStandardItem, QStandardItemModel

from PyQt5.QtCore import pyqtSlot, QDate

# Création de liste étudiante
ls_etudiant = []


# FONCTIONS
def Clear(object):
    object.lineEdit_numero.clear()
    object.lineEdit_nom.clear()
    object.dateEdit_naissance.setDate(QDate(2000, 1, 1))


def verifier_etudiant_liste(p_numero):
    for elt in ls_etudiant:
        if elt.Numero == p_numero:
            return True
    return False


class MaFenetreAffichage(QtWidgets.QMainWindow, code_interface_scolarité.Ui_MainWindow):

    def __init__(self, parent=None):
        super(MaFenetreAffichage, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Gestion de scolarité")  # Donner un titre à la fenêtre principale

        # Créer les informations dans le comboBox
        self.comboBox_programme.addItem("Techinque Informatique")
        self.comboBox_programme.addItem("Science Naturelle")
        self.comboBox_programme.addItem("Science Humaine")

    @pyqtSlot()
    def on_pushButton_ajouter_clicked(self):
        E1 = Etudiant()
        E1.Numero = self.lineEdit_numero.text().capitalize()
        E1.Nom = self.lineEdit_nom.text()
        E1.Programme = self.comboBox_programme.currentText()
        E1.Naissance = self.dateEdit_naissance.date()
        verifier_etudiant = verifier_etudiant_liste(E1.Numero)

        # Vérifier si le numero de l'étudiant est valide mais existe déjà
        if verifier_etudiant is True and E1.Numero != 0:
            self.lineEdit_numero.clear()
            self.label_erreur_numero.setText("Ce numéro d'étudiant existe déjà!")

        # si le nom est invalide, afficher un message d'erreur
        if E1.Nom == "":
            self.lineEdit_nom.clear()
            self.label_erreur_nom.setText("Le nom n'est pas valide!")

        # Si le numéro d'étudiant est invalide
        if E1.Numero == 0:
            self.lineEdit_numero.clear()
            self.label_erreur_numero.setText("Le numéro d'étudiant est invalide!")

        if E1.Naissance == "":
            Clear(self)
            self.label_erreur_numero.setText("L'étudiant est trop jeune (18+)!")
            self.label_erreur_nom.setText("L'étudiant est trop jeune (18+)!")

        # Si les infos entrées sont valides et l'étudiant n'existe pas dans la liste
        if E1.Numero != 0 and E1.Nom != "" and E1.Naissance != "" and verifier_etudiant is False:
            ls_etudiant.append(E1)
            # Sérialiser l'étudiant

            self.textBrowser_affichage.append(E1.__str__())
            Clear(self)

    @pyqtSlot()
    def on_pushButton_supprimer_clicked(self):
        E1 = Etudiant()
        E1.Numero = self.lineEdit_numero.text().capitalize()
        E1.Nom = self.lineEdit_nom.text()
        E1.Programme = self.comboBox_programme.currentText()
        E1.Naissance = self.dateEdit_naissance.text()
        verifier_etudiant = verifier_etudiant_liste(E1.Numero)

        # Vérifier si le numero de l'étudiant est valide mais existe déjà
        if verifier_etudiant is False and E1.Numero != 0:
            self.lineEdit_numero.clear()
            self.label_erreur_numero.setText("Ce numéro d'étudiant n'existe pas!")

        # si le nom est invalide, afficher un message d'erreur
        if E1.Nom == "":
            self.lineEdit_nom.clear()
            self.label_erreur_nom.setText("Le nom d'étudiant est invalide!")

        # Si le numéro d'étudiant est invalide
        if E1.Numero == 0:
            self.lineEdit_numero.clear()
            self.label_erreur_numero.setText("Le numéro d'étudiant est invalide!")

        # Si les infos entrées sont valides et l'étudiant n'existe pas dans la liste
        if E1.Numero != 0 and E1.Nom != "" and verifier_etudiant is True:
            for elt in ls_etudiant:
                if elt.Numero == E1.Numero:
                    ls_etudiant.remove(elt)
                    self.textBrowser_affichage.clear()
                    for elt in ls_etudiant:
                        self.textBrowser_affichage.append(elt.__str__())
                    Clear(self)
                else:
                    self.label_erreur_nom.setText("Cet étudiant n'existe pas!")
                    self.label_erreur_numero.setText("Cet étudiant n'existe pas!")
                    Clear(self)

    @pyqtSlot()
    def on_pushButton_modifier_clicked(self):
        """
        Modifie un étudiant déjà présent dans la liste
        """
        E1 = Etudiant()
        E1.Numero = self.lineEdit_numero.text().capitalize()
        E1.Nom = self.lineEdit_nom.text()
        E1.Programme = self.comboBox_programme.currentText()
        E1.Naissance = self.dateEdit_naissance.text()
        verifier_etudiant = verifier_etudiant_liste(E1.Numero)

        # Vérifier si le numero de l'étudiant est valide mais existe déjà
        if verifier_etudiant is False and E1.Numero != 0:
            self.lineEdit_numero.clear()
            self.label_erreur_numero.setText("Ce numéro d'étudiant n'existe pas!")
        # si le nom est invalide, afficher un message d'erreur
        if E1.Nom == "":
            self.lineEdit_nom.clear()
            self.label_erreur_nom.setText("Le nom n'est pas valide!")
        # Si le numéro d'étudiant est invalide
        if E1.Numero == 0:
            self.lineEdit_numero.clear()
            self.label_erreur_numero.setText("Le numéro d'étudiant est invalide!")
        # Si les infos entrées sont valides et l'étudiant n'existe pas dans la liste
        if E1.Numero != 0 and E1.Nom != "" and verifier_etudiant is True:
            for elt in ls_etudiant:
                if elt.Numero == E1.Numero:
                    ls_etudiant.remove(elt)
                    ls_etudiant.append(E1)
                    self.textBrowser_affichage.clear()
                    for elt in ls_etudiant:
                        self.textBrowser_affichage.append(elt.__str__())
                    Clear(self)
                else:
                    self.label_erreur_nom.setText("Cet étudiant n'existe pas!")
                    self.label_erreur_numero.setText("Cet étudiant n'existe pas!")
                    Clear(self)

    @pyqtSlot()
    def on_pushButton_listview_clicked(self):
        """
        Ouvre le dialogue pour voir la liste des étudiants
        """
        # Instancier une boite de dialogue
        dialog = Fenetrelistview()
        # Preparer listview
        model = QStandardItemModel()
        dialog.listView_liste.setModel(model)
        for e in ls_etudiant:
            item = QStandardItem(e.Numero+" * "+e.Nom+" * "+e.Programme)
            model.appendRow(item)
        # Afficher la boite de dialogue
        dialog.show()
        dialog.exec_()

    @pyqtSlot()
    def on_pushButton_local_clicked(self):
        """
        Ouvre le dialogue pour les locaux de l'école
        """
        # Instancier la boite de dialog
        dialog = InterfaceLocal()
        # Preparer l'inteface Local
        model = QStandardItemModel()

        # Afficher le dialog
        dialog.show()
        dialog.exec_()


def main():
    mon_app = QtWidgets.QApplication(sys.argv)
    mon_formulaire = MaFenetreAffichage()
    mon_formulaire.show()
    mon_app.exec()


if __name__ == "__main__":
    main()
