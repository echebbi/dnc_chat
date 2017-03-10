# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.8
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(662, 912)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../img/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 160, 621, 691))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.msg_accueil = QtWidgets.QLabel(self.centralwidget)
        self.msg_accueil.setGeometry(QtCore.QRect(20, 50, 619, 48))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(20)
        self.msg_accueil.setFont(font)
        self.msg_accueil.setScaledContents(True)
        self.msg_accueil.setAlignment(QtCore.Qt.AlignCenter)
        self.msg_accueil.setObjectName("msg_accueil")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 110, 621, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.huge_label = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.huge_label.setContentsMargins(0, 0, 0, 0)
        self.huge_label.setObjectName("huge_label")
        self.sub_msg = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        self.sub_msg.setFont(font)
        self.sub_msg.setAlignment(QtCore.Qt.AlignCenter)
        self.sub_msg.setObjectName("sub_msg")
        self.huge_label.addWidget(self.sub_msg)
        self.sub_lineEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.sub_lineEdit.setObjectName("sub_lineEdit")
        self.huge_label.addWidget(self.sub_lineEdit)
        self.sub_button = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.sub_button.setEnabled(True)
        self.sub_button.setObjectName("sub_button")
        self.huge_label.addWidget(self.sub_button)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 662, 31))
        self.menubar.setObjectName("menubar")
        self.menuMon_compte = QtWidgets.QMenu(self.menubar)
        self.menuMon_compte.setObjectName("menuMon_compte")
        self.menuConversation = QtWidgets.QMenu(self.menubar)
        self.menuConversation.setObjectName("menuConversation")
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        self.actionChanger_de_pseudo = QtWidgets.QAction(MainWindow)
        self.actionChanger_de_pseudo.setEnabled(True)
        self.actionChanger_de_pseudo.setObjectName("actionChanger_de_pseudo")
        self.actionSe_d_connecter = QtWidgets.QAction(MainWindow)
        self.actionSe_d_connecter.setObjectName("actionSe_d_connecter")
        self.actionPasser_en_mode_actif = QtWidgets.QAction(MainWindow)
        self.actionPasser_en_mode_actif.setObjectName("actionPasser_en_mode_actif")
        self.actionPasser_en_mode_inactif = QtWidgets.QAction(MainWindow)
        self.actionPasser_en_mode_inactif.setObjectName("actionPasser_en_mode_inactif")
        self.actionVoir_les_membres_connect_s = QtWidgets.QAction(MainWindow)
        self.actionVoir_les_membres_connect_s.setObjectName("actionVoir_les_membres_connect_s")
        self.actionLancer_une_conversation_priv_e = QtWidgets.QAction(MainWindow)
        self.actionLancer_une_conversation_priv_e.setObjectName("actionLancer_une_conversation_priv_e")
        self.menuMon_compte.addAction(self.actionChanger_de_pseudo)
        self.menuMon_compte.addAction(self.actionSe_d_connecter)
        self.menuConversation.addAction(self.actionPasser_en_mode_actif)
        self.menuConversation.addAction(self.actionPasser_en_mode_inactif)
        self.menuConversation.addSeparator()
        self.menuConversation.addAction(self.actionVoir_les_membres_connect_s)
        self.menuConversation.addAction(self.actionLancer_une_conversation_priv_e)
        self.menubar.addAction(self.menuMon_compte.menuAction())
        self.menubar.addAction(self.menuConversation.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Dog is not a Chat"))
        self.msg_accueil.setText(_translate("MainWindow", "Messagerie instantanée"))
        self.sub_msg.setText(_translate("MainWindow", "Dog is not a Chat"))
        self.sub_button.setText(_translate("MainWindow", "OK"))
        self.menuMon_compte.setTitle(_translate("MainWindow", "Mon compte"))
        self.menuConversation.setTitle(_translate("MainWindow", "Conversation"))
        self.actionChanger_de_pseudo.setText(_translate("MainWindow", "Changer de pseudo"))
        self.actionSe_d_connecter.setText(_translate("MainWindow", "Se déconnecter"))
        self.actionPasser_en_mode_actif.setText(_translate("MainWindow", "Passer en mode actif"))
        self.actionPasser_en_mode_inactif.setText(_translate("MainWindow", "Passer en mode inactif"))
        self.actionVoir_les_membres_connect_s.setText(_translate("MainWindow", "Voir les membres connectés"))
        self.actionLancer_une_conversation_priv_e.setText(_translate("MainWindow", "Lancer une conversation privée"))
