# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui\postsamples.ui'
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

class Ui_PostSamples_DockWidget(object):
    def setupUi(self, PostSamples_DockWidget):
        PostSamples_DockWidget.setObjectName(_fromUtf8("PostSamples_DockWidget"))
        PostSamples_DockWidget.resize(445, 476)
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
        self.boundary_comboBox = QtGui.QComboBox(self.dockWidgetContents)
        self.boundary_comboBox.setObjectName(_fromUtf8("boundary_comboBox"))
        self.boundary_comboBox.addItem(_fromUtf8(""))
        self.boundary_comboBox.addItem(_fromUtf8(""))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.boundary_comboBox)
        self.label_2 = QtGui.QLabel(self.dockWidgetContents)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_2)
        self.limit_lineEdit = QtGui.QLineEdit(self.dockWidgetContents)
        self.limit_lineEdit.setObjectName(_fromUtf8("limit_lineEdit"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.limit_lineEdit)
        self.label_3 = QtGui.QLabel(self.dockWidgetContents)
        self.label_3.setText(_fromUtf8(""))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_3)
        self.search_pushButton = QtGui.QPushButton(self.dockWidgetContents)
        self.search_pushButton.setObjectName(_fromUtf8("search_pushButton"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.search_pushButton)
        self.verticalLayout.addLayout(self.formLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.results_listWidget = QtGui.QListWidget(self.dockWidgetContents)
        self.results_listWidget.setObjectName(_fromUtf8("results_listWidget"))
        self.verticalLayout_2.addWidget(self.results_listWidget)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.addToMap_pushButton = QtGui.QPushButton(self.dockWidgetContents)
        self.addToMap_pushButton.setObjectName(_fromUtf8("addToMap_pushButton"))
        self.horizontalLayout.addWidget(self.addToMap_pushButton)
        self.markerColor_comboBox = QtGui.QComboBox(self.dockWidgetContents)
        self.markerColor_comboBox.setObjectName(_fromUtf8("markerColor_comboBox"))
        self.markerColor_comboBox.addItem(_fromUtf8(""))
        self.markerColor_comboBox.addItem(_fromUtf8(""))
        self.markerColor_comboBox.addItem(_fromUtf8(""))
        self.markerColor_comboBox.addItem(_fromUtf8(""))
        self.markerColor_comboBox.addItem(_fromUtf8(""))
        self.markerColor_comboBox.addItem(_fromUtf8(""))
        self.horizontalLayout.addWidget(self.markerColor_comboBox)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.formLayout_2 = QtGui.QFormLayout()
        self.formLayout_2.setObjectName(_fromUtf8("formLayout_2"))
        self.verticalLayout_2.addLayout(self.formLayout_2)
        PostSamples_DockWidget.setWidget(self.dockWidgetContents)

        self.retranslateUi(PostSamples_DockWidget)
        QtCore.QMetaObject.connectSlotsByName(PostSamples_DockWidget)

    def retranslateUi(self, PostSamples_DockWidget):
        PostSamples_DockWidget.setWindowTitle(_translate("PostSamples_DockWidget", "Post Samples", None))
        self.label.setText(_translate("PostSamples_DockWidget", "Spatial Limit", None))
        self.boundary_comboBox.setItemText(0, _translate("PostSamples_DockWidget", "Area Table", None))
        self.boundary_comboBox.setItemText(1, _translate("PostSamples_DockWidget", "None", None))
        self.label_2.setText(_translate("PostSamples_DockWidget", "Max Resutls ", None))
        self.search_pushButton.setText(_translate("PostSamples_DockWidget", "Search", None))
        self.addToMap_pushButton.setText(_translate("PostSamples_DockWidget", "Add selected to Word Map", None))
        self.markerColor_comboBox.setItemText(0, _translate("PostSamples_DockWidget", "Red", None))
        self.markerColor_comboBox.setItemText(1, _translate("PostSamples_DockWidget", "Green", None))
        self.markerColor_comboBox.setItemText(2, _translate("PostSamples_DockWidget", "Blue", None))
        self.markerColor_comboBox.setItemText(3, _translate("PostSamples_DockWidget", "Black", None))
        self.markerColor_comboBox.setItemText(4, _translate("PostSamples_DockWidget", "Yellow", None))
        self.markerColor_comboBox.setItemText(5, _translate("PostSamples_DockWidget", "White", None))

