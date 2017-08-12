# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui\googleknowledgegraph.ui'
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

class Ui_GoogleKnowledgGraph_dockable(object):
    def setupUi(self, GoogleKnowledgGraph_dockable):
        GoogleKnowledgGraph_dockable.setObjectName(_fromUtf8("GoogleKnowledgGraph_dockable"))
        GoogleKnowledgGraph_dockable.resize(349, 391)
        self.dockWidgetContents = QtGui.QWidget()
        self.dockWidgetContents.setObjectName(_fromUtf8("dockWidgetContents"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label = QtGui.QLabel(self.dockWidgetContents)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.searchterm_lineEdit = QtGui.QLineEdit(self.dockWidgetContents)
        self.searchterm_lineEdit.setObjectName(_fromUtf8("searchterm_lineEdit"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.searchterm_lineEdit)
        self.label_2 = QtGui.QLabel(self.dockWidgetContents)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_2)
        self.entries_lineEdit = QtGui.QLineEdit(self.dockWidgetContents)
        self.entries_lineEdit.setObjectName(_fromUtf8("entries_lineEdit"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.entries_lineEdit)
        self.label_3 = QtGui.QLabel(self.dockWidgetContents)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_3)
        self.types_comboBox = QtGui.QComboBox(self.dockWidgetContents)
        self.types_comboBox.setMaxVisibleItems(20)
        self.types_comboBox.setObjectName(_fromUtf8("types_comboBox"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.types_comboBox)
        self.search_pushButton = QtGui.QPushButton(self.dockWidgetContents)
        self.search_pushButton.setObjectName(_fromUtf8("search_pushButton"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.search_pushButton)
        self.results_listWidget = QtGui.QListWidget(self.dockWidgetContents)
        self.results_listWidget.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.results_listWidget.setObjectName(_fromUtf8("results_listWidget"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.results_listWidget)
        self.addtolist_pushButton = QtGui.QPushButton(self.dockWidgetContents)
        self.addtolist_pushButton.setObjectName(_fromUtf8("addtolist_pushButton"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.FieldRole, self.addtolist_pushButton)
        self.verticalLayout.addLayout(self.formLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        GoogleKnowledgGraph_dockable.setWidget(self.dockWidgetContents)

        self.retranslateUi(GoogleKnowledgGraph_dockable)
        QtCore.QMetaObject.connectSlotsByName(GoogleKnowledgGraph_dockable)

    def retranslateUi(self, GoogleKnowledgGraph_dockable):
        GoogleKnowledgGraph_dockable.setWindowTitle(_translate("GoogleKnowledgGraph_dockable", "Google Knowledge Graph", None))
        self.label.setText(_translate("GoogleKnowledgGraph_dockable", "Search Term", None))
        self.label_2.setText(_translate("GoogleKnowledgGraph_dockable", "Entries", None))
        self.label_3.setText(_translate("GoogleKnowledgGraph_dockable", "Type", None))
        self.search_pushButton.setText(_translate("GoogleKnowledgGraph_dockable", "Search", None))
        self.addtolist_pushButton.setText(_translate("GoogleKnowledgGraph_dockable", "Add Selected to Wordlist", None))

