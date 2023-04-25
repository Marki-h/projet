from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSlot
import ListeView


class Fenetrelistview(QtWidgets.QDialog, ListeView.Ui_ListeView):
    def __init__(self, parent=None):
        super(Fenetrelistview, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Liste des étudiant.e.s")

    # Gestionnaire d'évenement du bouton Quitter
    @pyqtSlot()
    def on_pushButton_quitter_clicked(self):
        self.close()
