# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui\wordlist.ui'
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

class Ui_wordlist_dockable(object):
    def setupUi(self, wordlist_dockable):
        wordlist_dockable.setObjectName(_fromUtf8("wordlist_dockable"))
        wordlist_dockable.resize(400, 585)
        self.dockWidgetContents = QtGui.QWidget()
        self.dockWidgetContents.setObjectName(_fromUtf8("dockWidgetContents"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.file = QtGui.QGroupBox(self.dockWidgetContents)
        self.file.setObjectName(_fromUtf8("file"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.file)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.wordlistload_pushButton = QtGui.QPushButton(self.file)
        self.wordlistload_pushButton.setObjectName(_fromUtf8("wordlistload_pushButton"))
        self.horizontalLayout.addWidget(self.wordlistload_pushButton)
        self.wordlistsave_pushButton = QtGui.QPushButton(self.file)
        self.wordlistsave_pushButton.setObjectName(_fromUtf8("wordlistsave_pushButton"))
        self.horizontalLayout.addWidget(self.wordlistsave_pushButton)
        self.wordlistfile_lineEdit = QtGui.QLineEdit(self.file)
        self.wordlistfile_lineEdit.setObjectName(_fromUtf8("wordlistfile_lineEdit"))
        self.horizontalLayout.addWidget(self.wordlistfile_lineEdit)
        self.verticalLayout.addWidget(self.file)
        self.List = QtGui.QGroupBox(self.dockWidgetContents)
        self.List.setObjectName(_fromUtf8("List"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.List)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.wordlist_tableWidget = QtGui.QTableWidget(self.List)
        self.wordlist_tableWidget.setObjectName(_fromUtf8("wordlist_tableWidget"))
        self.wordlist_tableWidget.setColumnCount(4)
        self.wordlist_tableWidget.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.wordlist_tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.wordlist_tableWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.wordlist_tableWidget.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.wordlist_tableWidget.setHorizontalHeaderItem(3, item)
        self.verticalLayout_3.addWidget(self.wordlist_tableWidget)
        self.AddNew = QtGui.QGroupBox(self.List)
        self.AddNew.setObjectName(_fromUtf8("AddNew"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.AddNew)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.newWord_label = QtGui.QLabel(self.AddNew)
        self.newWord_label.setObjectName(_fromUtf8("newWord_label"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.newWord_label)
        self.NewTags_label = QtGui.QLabel(self.AddNew)
        self.NewTags_label.setObjectName(_fromUtf8("NewTags_label"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.NewTags_label)
        self.NewWord_lineEdit = QtGui.QLineEdit(self.AddNew)
        self.NewWord_lineEdit.setObjectName(_fromUtf8("NewWord_lineEdit"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.NewWord_lineEdit)
        self.NewTags_lineEdit = QtGui.QLineEdit(self.AddNew)
        self.NewTags_lineEdit.setObjectName(_fromUtf8("NewTags_lineEdit"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.NewTags_lineEdit)
        self.verticalLayout_4.addLayout(self.formLayout)
        self.AddNew_pushButton = QtGui.QPushButton(self.AddNew)
        self.AddNew_pushButton.setObjectName(_fromUtf8("AddNew_pushButton"))
        self.verticalLayout_4.addWidget(self.AddNew_pushButton)
        self.verticalLayout_3.addWidget(self.AddNew)
        self.removewords_pushButton = QtGui.QPushButton(self.List)
        self.removewords_pushButton.setObjectName(_fromUtf8("removewords_pushButton"))
        self.verticalLayout_3.addWidget(self.removewords_pushButton)
        self.verticalLayout.addWidget(self.List)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        wordlist_dockable.setWidget(self.dockWidgetContents)

        self.retranslateUi(wordlist_dockable)
        QtCore.QMetaObject.connectSlotsByName(wordlist_dockable)

    def retranslateUi(self, wordlist_dockable):
        wordlist_dockable.setWindowTitle(_translate("wordlist_dockable", "Wordlist", None))
        self.file.setTitle(_translate("wordlist_dockable", "Wordfile", None))
        self.wordlistload_pushButton.setText(_translate("wordlist_dockable", "Load", None))
        self.wordlistsave_pushButton.setText(_translate("wordlist_dockable", "Save", None))
        self.wordlistfile_lineEdit.setText(_translate("wordlist_dockable", "data\\masterlist.json", None))
        self.List.setTitle(_translate("wordlist_dockable", "Wordlist", None))
        item = self.wordlist_tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("wordlist_dockable", "Word", None))
        item = self.wordlist_tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("wordlist_dockable", "Tag 1", None))
        item = self.wordlist_tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("wordlist_dockable", "Tag 2", None))
        item = self.wordlist_tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("wordlist_dockable", "Tag 3", None))
        self.AddNew.setTitle(_translate("wordlist_dockable", "Add New Word", None))
        self.newWord_label.setText(_translate("wordlist_dockable", "Word", None))
        self.NewTags_label.setText(_translate("wordlist_dockable", "Tags", None))
        self.AddNew_pushButton.setText(_translate("wordlist_dockable", "Add", None))
        self.removewords_pushButton.setText(_translate("wordlist_dockable", "Remove Selected Words", None))

