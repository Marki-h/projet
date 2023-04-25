from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSlot
import interface_local


class InterfaceLocal(QtWidgets.QDialog, interface_local.Ui_Dialog):
    def __init__(self, parent=None):
        super(InterfaceLocal, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Liste des étudiant.e.s")
        self.comboBox_type.addItem("Technique")
        self.comboBox_type.addItem("Normal")
        self.comboBox_lieu.addItem("A")
        self.comboBox_lieu.addItem("B")
        self.comboBox_lieu.addItem("C")
        self.comboBox_projecteur.addItem("Oui")
        self.comboBox_projecteur.addItem("Non")
        self.comboBox_nb_places.addItem("1")
        self.comboBox_nb_places.addItem("2")


    # Gestionnaire d'évenement du bouton Quitter
    @pyqtSlot()
    def on_pushButton_quitter_clicked(self):
        self.close()
