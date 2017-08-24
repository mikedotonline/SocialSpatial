# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui\cartogram.ui'
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

class Ui_Cartogram_dock(object):
    def setupUi(self, Cartogram_dock):
        Cartogram_dock.setObjectName(_fromUtf8("Cartogram_dock"))
        Cartogram_dock.resize(277, 608)
        self.dockWidgetContents = QtGui.QWidget()
        self.dockWidgetContents.setObjectName(_fromUtf8("dockWidgetContents"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.verticalGroupBox = QtGui.QGroupBox(self.dockWidgetContents)
        self.verticalGroupBox.setObjectName(_fromUtf8("verticalGroupBox"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalGroupBox)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label = QtGui.QLabel(self.verticalGroupBox)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label)
        self.label_2 = QtGui.QLabel(self.verticalGroupBox)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_2)
        self.label_3 = QtGui.QLabel(self.verticalGroupBox)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_3)
        self.label_4 = QtGui.QLabel(self.verticalGroupBox)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_4)
        self.font_lineEdit = QtGui.QLineEdit(self.verticalGroupBox)
        self.font_lineEdit.setObjectName(_fromUtf8("font_lineEdit"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.font_lineEdit)
        self.size_lineEdit = QtGui.QLineEdit(self.verticalGroupBox)
        self.size_lineEdit.setMaxLength(6)
        self.size_lineEdit.setObjectName(_fromUtf8("size_lineEdit"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.size_lineEdit)
        self.shp_lineEdit = QtGui.QLineEdit(self.verticalGroupBox)
        self.shp_lineEdit.setObjectName(_fromUtf8("shp_lineEdit"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.shp_lineEdit)
        self.output_lineEdit = QtGui.QLineEdit(self.verticalGroupBox)
        self.output_lineEdit.setObjectName(_fromUtf8("output_lineEdit"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.output_lineEdit)
        self.verticalLayout.addLayout(self.formLayout)
        self.verticalGroupBox1 = QtGui.QGroupBox(self.verticalGroupBox)
        self.verticalGroupBox1.setObjectName(_fromUtf8("verticalGroupBox1"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.verticalGroupBox1)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.run_pushButton = QtGui.QPushButton(self.verticalGroupBox1)
        self.run_pushButton.setObjectName(_fromUtf8("run_pushButton"))
        self.horizontalLayout.addWidget(self.run_pushButton)
        self.progressBar = QtGui.QProgressBar(self.verticalGroupBox1)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.horizontalLayout.addWidget(self.progressBar)
        self.verticalLayout_5.addLayout(self.horizontalLayout)
        self.verticalLayout.addWidget(self.verticalGroupBox1)
        self.verticalGroupBox_2 = QtGui.QGroupBox(self.verticalGroupBox)
        self.verticalGroupBox_2.setObjectName(_fromUtf8("verticalGroupBox_2"))
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.verticalGroupBox_2)
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.preview_label = QtGui.QLabel(self.verticalGroupBox_2)
        self.preview_label.setMaximumSize(QtCore.QSize(400, 400))
        self.preview_label.setText(_fromUtf8(""))
        self.preview_label.setObjectName(_fromUtf8("preview_label"))
        self.verticalLayout_6.addWidget(self.preview_label)
        self.verticalLayout.addWidget(self.verticalGroupBox_2)
        self.verticalLayout_2.addWidget(self.verticalGroupBox)
        Cartogram_dock.setWidget(self.dockWidgetContents)

        self.retranslateUi(Cartogram_dock)
        QtCore.QMetaObject.connectSlotsByName(Cartogram_dock)

    def retranslateUi(self, Cartogram_dock):
        Cartogram_dock.setWindowTitle(_translate("Cartogram_dock", "Topic / Word Cartogram", None))
        self.verticalGroupBox.setTitle(_translate("Cartogram_dock", "Parameters", None))
        self.label.setText(_translate("Cartogram_dock", "Input Shp", None))
        self.label_2.setText(_translate("Cartogram_dock", "Image Size (px^2)", None))
        self.label_3.setText(_translate("Cartogram_dock", "Font", None))
        self.label_4.setText(_translate("Cartogram_dock", "Output file", None))
        self.size_lineEdit.setText(_translate("Cartogram_dock", "5000", None))
        self.shp_lineEdit.setText(_translate("Cartogram_dock", "data\\van_nhoods\\van_nhoods.shp", None))
        self.output_lineEdit.setText(_translate("Cartogram_dock", "data\\cartogram.png", None))
        self.verticalGroupBox1.setTitle(_translate("Cartogram_dock", "Control", None))
        self.run_pushButton.setText(_translate("Cartogram_dock", "Run", None))
        self.verticalGroupBox_2.setTitle(_translate("Cartogram_dock", "Preview", None))

