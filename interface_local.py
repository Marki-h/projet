# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'G:\Hiver2023\PrgrmtionOrienteObjet\Code\Gestion_de_scolatiré\interface_local.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(461, 391)
        self.label_num_local = QtWidgets.QLabel(Dialog)
        self.label_num_local.setGeometry(QtCore.QRect(10, 150, 191, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_num_local.setFont(font)
        self.label_num_local.setObjectName("label_num_local")
        self.lineEdit_num_local = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_num_local.setGeometry(QtCore.QRect(10, 180, 181, 21))
        self.lineEdit_num_local.setObjectName("lineEdit_num_local")
        self.label_dimension_local = QtWidgets.QLabel(Dialog)
        self.label_dimension_local.setGeometry(QtCore.QRect(10, 230, 171, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_dimension_local.setFont(font)
        self.label_dimension_local.setObjectName("label_dimension_local")
        self.lineEdit_dimension_local = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_dimension_local.setGeometry(QtCore.QRect(10, 260, 181, 21))
        self.lineEdit_dimension_local.setObjectName("lineEdit_dimension_local")
        self.label_type = QtWidgets.QLabel(Dialog)
        self.label_type.setGeometry(QtCore.QRect(10, 10, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_type.setFont(font)
        self.label_type.setObjectName("label_type")
        self.comboBox_type = QtWidgets.QComboBox(Dialog)
        self.comboBox_type.setGeometry(QtCore.QRect(10, 40, 181, 22))
        self.comboBox_type.setObjectName("comboBox_type")
        self.label_erreur_numero = QtWidgets.QLabel(Dialog)
        self.label_erreur_numero.setGeometry(QtCore.QRect(10, 210, 181, 21))
        self.label_erreur_numero.setText("")
        self.label_erreur_numero.setObjectName("label_erreur_numero")
        self.label_erreur_dimension = QtWidgets.QLabel(Dialog)
        self.label_erreur_dimension.setGeometry(QtCore.QRect(10, 290, 181, 21))
        self.label_erreur_dimension.setText("")
        self.label_erreur_dimension.setObjectName("label_erreur_dimension")
        self.label_nb_places = QtWidgets.QLabel(Dialog)
        self.label_nb_places.setGeometry(QtCore.QRect(10, 310, 171, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_nb_places.setFont(font)
        self.label_nb_places.setObjectName("label_nb_places")
        self.lineEdit_nb_places = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_nb_places.setGeometry(QtCore.QRect(10, 340, 181, 21))
        self.lineEdit_nb_places.setObjectName("lineEdit_nb_places")
        self.label_erreur_nb_places = QtWidgets.QLabel(Dialog)
        self.label_erreur_nb_places.setGeometry(QtCore.QRect(10, 380, 181, 21))
        self.label_erreur_nb_places.setText("")
        self.label_erreur_nb_places.setObjectName("label_erreur_nb_places")
        self.label_lieu = QtWidgets.QLabel(Dialog)
        self.label_lieu.setGeometry(QtCore.QRect(10, 80, 181, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_lieu.setFont(font)
        self.label_lieu.setObjectName("label_lieu")
        self.comboBox_lieu = QtWidgets.QComboBox(Dialog)
        self.comboBox_lieu.setGeometry(QtCore.QRect(10, 110, 181, 22))
        self.comboBox_lieu.setObjectName("comboBox_lieu")
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(210, 0, 16, 711))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_local_technique = QtWidgets.QLabel(Dialog)
        self.label_local_technique.setGeometry(QtCore.QRect(250, 10, 151, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_local_technique.setFont(font)
        self.label_local_technique.setObjectName("label_local_technique")
        self.label_local_normal = QtWidgets.QLabel(Dialog)
        self.label_local_normal.setGeometry(QtCore.QRect(250, 220, 151, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_local_normal.setFont(font)
        self.label_local_normal.setObjectName("label_local_normal")
        self.label_marque_ordi = QtWidgets.QLabel(Dialog)
        self.label_marque_ordi.setGeometry(QtCore.QRect(250, 40, 181, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_marque_ordi.setFont(font)
        self.label_marque_ordi.setObjectName("label_marque_ordi")
        self.lineEdit_marque_ordinateur = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_marque_ordinateur.setGeometry(QtCore.QRect(250, 60, 181, 20))
        self.lineEdit_marque_ordinateur.setObjectName("lineEdit_marque_ordinateur")
        self.label_nb_ordinateurs = QtWidgets.QLabel(Dialog)
        self.label_nb_ordinateurs.setGeometry(QtCore.QRect(250, 100, 171, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_nb_ordinateurs.setFont(font)
        self.label_nb_ordinateurs.setObjectName("label_nb_ordinateurs")
        self.label_erreur_marque_ordi = QtWidgets.QLabel(Dialog)
        self.label_erreur_marque_ordi.setGeometry(QtCore.QRect(250, 80, 181, 21))
        self.label_erreur_marque_ordi.setText("")
        self.label_erreur_marque_ordi.setObjectName("label_erreur_marque_ordi")
        self.lineEdit_nb_ordi = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_nb_ordi.setGeometry(QtCore.QRect(250, 120, 181, 20))
        self.lineEdit_nb_ordi.setObjectName("lineEdit_nb_ordi")
        self.label_erreur_nb_ordinateurs = QtWidgets.QLabel(Dialog)
        self.label_erreur_nb_ordinateurs.setGeometry(QtCore.QRect(250, 140, 181, 21))
        self.label_erreur_nb_ordinateurs.setText("")
        self.label_erreur_nb_ordinateurs.setObjectName("label_erreur_nb_ordinateurs")
        self.label_nb_places_2 = QtWidgets.QLabel(Dialog)
        self.label_nb_places_2.setGeometry(QtCore.QRect(250, 250, 221, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_nb_places_2.setFont(font)
        self.label_nb_places_2.setObjectName("label_nb_places_2")
        self.comboBox_nb_places = QtWidgets.QComboBox(Dialog)
        self.comboBox_nb_places.setGeometry(QtCore.QRect(250, 270, 181, 22))
        self.comboBox_nb_places.setObjectName("comboBox_nb_places")
        self.label_projecteur = QtWidgets.QLabel(Dialog)
        self.label_projecteur.setGeometry(QtCore.QRect(250, 160, 121, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_projecteur.setFont(font)
        self.label_projecteur.setObjectName("label_projecteur")
        self.comboBox_projecteur = QtWidgets.QComboBox(Dialog)
        self.comboBox_projecteur.setGeometry(QtCore.QRect(250, 180, 181, 22))
        self.comboBox_projecteur.setObjectName("comboBox_projecteur")
        self.pushButton_quitter = QtWidgets.QPushButton(Dialog)
        self.pushButton_quitter.setGeometry(QtCore.QRect(350, 330, 81, 31))
        self.pushButton_quitter.setObjectName("pushButton_quitter")
        self.pushButton_ajouter_local = QtWidgets.QPushButton(Dialog)
        self.pushButton_ajouter_local.setGeometry(QtCore.QRect(250, 330, 81, 31))
        self.pushButton_ajouter_local.setObjectName("pushButton_ajouter_local")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_num_local.setText(_translate("Dialog", "Numéro du local :"))
        self.label_dimension_local.setText(_translate("Dialog", "Dimension du local :"))
        self.label_type.setText(_translate("Dialog", "Type du local :"))
        self.label_nb_places.setText(_translate("Dialog", "Nombre de places : "))
        self.label_lieu.setText(_translate("Dialog", "Lieu du local :"))
        self.label_local_technique.setText(_translate("Dialog", "Local Technique :"))
        self.label_local_normal.setText(_translate("Dialog", "Local Normal :"))
        self.label_marque_ordi.setText(_translate("Dialog", "Marque de l\'ordinateur :"))
        self.label_nb_ordinateurs.setText(_translate("Dialog", "Nombre d\'ordinateurs :"))
        self.label_nb_places_2.setText(_translate("Dialog", "Nombre de places par table :"))
        self.label_projecteur.setText(_translate("Dialog", "Projecteur :"))
        self.pushButton_quitter.setText(_translate("Dialog", "Quitter"))
        self.pushButton_ajouter_local.setText(_translate("Dialog", "Ajouter"))
