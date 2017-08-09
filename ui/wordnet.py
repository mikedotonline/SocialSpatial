# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui\wordnet.ui'
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

class Ui_wordnet_dockable(object):
    def setupUi(self, wordnet_dockable):
        wordnet_dockable.setObjectName(_fromUtf8("wordnet_dockable"))
        wordnet_dockable.resize(329, 595)
        self.dockWidgetContents = QtGui.QWidget()
        self.dockWidgetContents.setObjectName(_fromUtf8("dockWidgetContents"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.SearchTerm = QtGui.QGroupBox(self.dockWidgetContents)
        self.SearchTerm.setObjectName(_fromUtf8("SearchTerm"))
        self.verticalLayout = QtGui.QVBoxLayout(self.SearchTerm)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.search_lineEdit = QtGui.QLineEdit(self.SearchTerm)
        self.search_lineEdit.setObjectName(_fromUtf8("search_lineEdit"))
        self.horizontalLayout.addWidget(self.search_lineEdit)
        self.search_pushButton = QtGui.QPushButton(self.SearchTerm)
        self.search_pushButton.setObjectName(_fromUtf8("search_pushButton"))
        self.horizontalLayout.addWidget(self.search_pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addWidget(self.SearchTerm)
        self.groupBox = QtGui.QGroupBox(self.dockWidgetContents)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.groupBox)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.groupBox_2 = QtGui.QGroupBox(self.groupBox)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.synonyms_listView = QtGui.QListView(self.groupBox_2)
        self.synonyms_listView.setObjectName(_fromUtf8("synonyms_listView"))
        self.verticalLayout_3.addWidget(self.synonyms_listView)
        self.horizontalLayout_3.addWidget(self.groupBox_2)
        self.groupBox_3 = QtGui.QGroupBox(self.groupBox)
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.hypernyms_listView = QtGui.QListView(self.groupBox_3)
        self.hypernyms_listView.setObjectName(_fromUtf8("hypernyms_listView"))
        self.verticalLayout_4.addWidget(self.hypernyms_listView)
        self.horizontalLayout_3.addWidget(self.groupBox_3)
        self.groupBox_4 = QtGui.QGroupBox(self.groupBox)
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.groupBox_4)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.hyponyms_listView = QtGui.QListView(self.groupBox_4)
        self.hyponyms_listView.setObjectName(_fromUtf8("hyponyms_listView"))
        self.verticalLayout_5.addWidget(self.hyponyms_listView)
        self.horizontalLayout_3.addWidget(self.groupBox_4)
        self.verticalLayout_2.addWidget(self.groupBox)
        self.addtolist_pushButton = QtGui.QPushButton(self.dockWidgetContents)
        self.addtolist_pushButton.setObjectName(_fromUtf8("addtolist_pushButton"))
        self.verticalLayout_2.addWidget(self.addtolist_pushButton)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        wordnet_dockable.setWidget(self.dockWidgetContents)

        self.retranslateUi(wordnet_dockable)
        QtCore.QMetaObject.connectSlotsByName(wordnet_dockable)

    def retranslateUi(self, wordnet_dockable):
        wordnet_dockable.setWindowTitle(_translate("wordnet_dockable", "WordNet", None))
        self.SearchTerm.setTitle(_translate("wordnet_dockable", "Search", None))
        self.search_pushButton.setText(_translate("wordnet_dockable", "Search", None))
        self.groupBox.setTitle(_translate("wordnet_dockable", "Results", None))
        self.groupBox_2.setTitle(_translate("wordnet_dockable", "Synonyms", None))
        self.groupBox_3.setTitle(_translate("wordnet_dockable", "Hypernyms", None))
        self.groupBox_4.setTitle(_translate("wordnet_dockable", "Hyponyms", None))
        self.addtolist_pushButton.setText(_translate("wordnet_dockable", "Add Selected to List", None))

