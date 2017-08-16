# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui\mainwindow.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1065, 860)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../favico_2.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1065, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuTools = QtGui.QMenu(self.menubar)
        self.menuTools.setObjectName(_fromUtf8("menuTools"))
        self.menuView = QtGui.QMenu(self.menubar)
        self.menuView.setObjectName(_fromUtf8("menuView"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionFile = QtGui.QAction(MainWindow)
        self.actionFile.setObjectName(_fromUtf8("actionFile"))
        self.actionSave = QtGui.QAction(MainWindow)
        self.actionSave.setObjectName(_fromUtf8("actionSave"))
        self.actionExport = QtGui.QAction(MainWindow)
        self.actionExport.setObjectName(_fromUtf8("actionExport"))
        self.actionGoogle_Knowledge_Graph = QtGui.QAction(MainWindow)
        self.actionGoogle_Knowledge_Graph.setShortcutContext(QtCore.Qt.WidgetShortcut)
        self.actionGoogle_Knowledge_Graph.setObjectName(_fromUtf8("actionGoogle_Knowledge_Graph"))
        self.actionWordnet = QtGui.QAction(MainWindow)
        self.actionWordnet.setObjectName(_fromUtf8("actionWordnet"))
        self.actionWord_Map = QtGui.QAction(MainWindow)
        self.actionWord_Map.setObjectName(_fromUtf8("actionWord_Map"))
        self.actionTopic_Modelling = QtGui.QAction(MainWindow)
        self.actionTopic_Modelling.setObjectName(_fromUtf8("actionTopic_Modelling"))
        self.actionSentiment_Modelling = QtGui.QAction(MainWindow)
        self.actionSentiment_Modelling.setObjectName(_fromUtf8("actionSentiment_Modelling"))
        self.actionWordle_Map = QtGui.QAction(MainWindow)
        self.actionWordle_Map.setObjectName(_fromUtf8("actionWordle_Map"))
        self.actionDatabase_Connection = QtGui.QAction(MainWindow)
        self.actionDatabase_Connection.setObjectName(_fromUtf8("actionDatabase_Connection"))
        self.actionWord_List = QtGui.QAction(MainWindow)
        self.actionWord_List.setObjectName(_fromUtf8("actionWord_List"))
        self.actionPost_Samples = QtGui.QAction(MainWindow)
        self.actionPost_Samples.setObjectName(_fromUtf8("actionPost_Samples"))
        self.menuFile.addAction(self.actionFile)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionExport)
        self.menuTools.addAction(self.actionGoogle_Knowledge_Graph)
        self.menuTools.addAction(self.actionWordnet)
        self.menuTools.addSeparator()
        self.menuTools.addAction(self.actionTopic_Modelling)
        self.menuTools.addAction(self.actionSentiment_Modelling)
        self.menuTools.addSeparator()
        self.menuTools.addAction(self.actionWordle_Map)
        self.menuView.addAction(self.actionDatabase_Connection)
        self.menuView.addAction(self.actionWord_List)
        self.menuView.addSeparator()
        self.menuView.addAction(self.actionPost_Samples)
        self.menuView.addAction(self.actionWord_Map)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuTools.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Social Spatial Explorer", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.menuTools.setTitle(_translate("MainWindow", "Tools", None))
        self.menuView.setTitle(_translate("MainWindow", "View", None))
        self.actionFile.setText(_translate("MainWindow", "Open", None))
        self.actionSave.setText(_translate("MainWindow", "Save", None))
        self.actionExport.setText(_translate("MainWindow", "Export", None))
        self.actionGoogle_Knowledge_Graph.setText(_translate("MainWindow", "Google Knowledge Graph", None))
        self.actionWordnet.setText(_translate("MainWindow", "Wordnet", None))
        self.actionWord_Map.setText(_translate("MainWindow", "Word Map", None))
        self.actionTopic_Modelling.setText(_translate("MainWindow", "Topic Modelling", None))
        self.actionSentiment_Modelling.setText(_translate("MainWindow", "Sentiment Modelling", None))
        self.actionWordle_Map.setText(_translate("MainWindow", "Wordle Map", None))
        self.actionDatabase_Connection.setText(_translate("MainWindow", "Database Connection", None))
        self.actionWord_List.setText(_translate("MainWindow", "Word List", None))
        self.actionPost_Samples.setText(_translate("MainWindow", "Post Samples", None))

