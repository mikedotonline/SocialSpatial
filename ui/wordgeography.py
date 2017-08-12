# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui\wordgeography.ui'
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

class Ui_WordGeography_DockWidget(object):
    def setupUi(self, WordGeography_DockWidget):
        WordGeography_DockWidget.setObjectName(_fromUtf8("WordGeography_DockWidget"))
        WordGeography_DockWidget.resize(1083, 698)
        self.dockWidgetContents = QtGui.QWidget()
        self.dockWidgetContents.setObjectName(_fromUtf8("dockWidgetContents"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.info_label = QtGui.QLabel(self.dockWidgetContents)
        self.info_label.setObjectName(_fromUtf8("info_label"))
        self.verticalLayout.addWidget(self.info_label)
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label = QtGui.QLabel(self.dockWidgetContents)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label)
        self.limit_lineEdit = QtGui.QLineEdit(self.dockWidgetContents)
        self.limit_lineEdit.setObjectName(_fromUtf8("limit_lineEdit"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.limit_lineEdit)
        self.label_2 = QtGui.QLabel(self.dockWidgetContents)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_2)
        self.boundary_comboBox = QtGui.QComboBox(self.dockWidgetContents)
        self.boundary_comboBox.setObjectName(_fromUtf8("boundary_comboBox"))
        self.boundary_comboBox.addItem(_fromUtf8(""))
        self.boundary_comboBox.addItem(_fromUtf8(""))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.boundary_comboBox)
        self.search_pushButton = QtGui.QPushButton(self.dockWidgetContents)
        self.search_pushButton.setObjectName(_fromUtf8("search_pushButton"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.search_pushButton)
        self.verticalLayout.addLayout(self.formLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.groupBox = QtGui.QGroupBox(self.dockWidgetContents)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.map_webView = QtWebKit.QWebView(self.groupBox)
        self.map_webView.setUrl(QtCore.QUrl(_fromUtf8("about:blank")))
        self.map_webView.setObjectName(_fromUtf8("map_webView"))
        self.verticalLayout_3.addWidget(self.map_webView)
        self.verticalLayout_2.addWidget(self.groupBox)
        WordGeography_DockWidget.setWidget(self.dockWidgetContents)

        self.retranslateUi(WordGeography_DockWidget)
        QtCore.QMetaObject.connectSlotsByName(WordGeography_DockWidget)

    def retranslateUi(self, WordGeography_DockWidget):
        WordGeography_DockWidget.setWindowTitle(_translate("WordGeography_DockWidget", "Word Geography", None))
        self.info_label.setText(_translate("WordGeography_DockWidget", "Using the currently Selected Words, see how they are laid out in Geographic Space", None))
        self.label.setText(_translate("WordGeography_DockWidget", "Limit Number of posts to", None))
        self.label_2.setText(_translate("WordGeography_DockWidget", "Search Within", None))
        self.boundary_comboBox.setItemText(0, _translate("WordGeography_DockWidget", "Boundary Table", None))
        self.boundary_comboBox.setItemText(1, _translate("WordGeography_DockWidget", "Current Map Extent", None))
        self.search_pushButton.setText(_translate("WordGeography_DockWidget", "Search for Matches", None))
        self.groupBox.setTitle(_translate("WordGeography_DockWidget", "Map", None))

from PyQt4 import QtWebKit
