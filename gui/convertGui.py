# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'convertGui.ui'
#
# Created: Sat Feb  1 20:53:18 2014
#      by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(366, 347)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 270000))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.widget = QtGui.QWidget(self.tab)
        self.widget.setGeometry(QtCore.QRect(9, 9, 321, 61))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(self.widget)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.txtDcm = QtGui.QLineEdit(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtDcm.sizePolicy().hasHeightForWidth())
        self.txtDcm.setSizePolicy(sizePolicy)
        self.txtDcm.setObjectName(_fromUtf8("txtDcm"))
        self.horizontalLayout_2.addWidget(self.txtDcm)
        self.cmdDcm = QtGui.QPushButton(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cmdDcm.sizePolicy().hasHeightForWidth())
        self.cmdDcm.setSizePolicy(sizePolicy)
        self.cmdDcm.setMinimumSize(QtCore.QSize(31, 27))
        self.cmdDcm.setMaximumSize(QtCore.QSize(31, 27))
        self.cmdDcm.setObjectName(_fromUtf8("cmdDcm"))
        self.horizontalLayout_2.addWidget(self.cmdDcm)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.cmdStartConvert = QtGui.QPushButton(self.tab)
        self.cmdStartConvert.setGeometry(QtCore.QRect(10, 200, 85, 31))
        self.cmdStartConvert.setObjectName(_fromUtf8("cmdStartConvert"))
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.widget1 = QtGui.QWidget(self.tab_2)
        self.widget1.setGeometry(QtCore.QRect(9, 9, 321, 62))
        self.widget1.setObjectName(_fromUtf8("widget1"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.widget1)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label_3 = QtGui.QLabel(self.widget1)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout_2.addWidget(self.label_3)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.txtProject = QtGui.QLineEdit(self.widget1)
        self.txtProject.setObjectName(_fromUtf8("txtProject"))
        self.horizontalLayout.addWidget(self.txtProject)
        self.label_4 = QtGui.QLabel(self.widget1)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout.addWidget(self.label_4)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.cmdStartToSave = QtGui.QPushButton(self.tab_2)
        self.cmdStartToSave.setGeometry(QtCore.QRect(10, 200, 81, 31))
        self.cmdStartToSave.setObjectName(_fromUtf8("cmdStartToSave"))
        self.gridLayoutWidget = QtGui.QWidget(self.tab_2)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 80, 321, 51))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.gridLayout_2 = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout_2.setMargin(0)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.label_6 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout_2.addWidget(self.label_6, 0, 0, 1, 1)
        self.spinBox = QtGui.QSpinBox(self.gridLayoutWidget)
        self.spinBox.setObjectName(_fromUtf8("spinBox"))
        self.gridLayout_2.addWidget(self.spinBox, 1, 1, 1, 1)
        self.horizontalSlider = QtGui.QSlider(self.gridLayoutWidget)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName(_fromUtf8("horizontalSlider"))
        self.gridLayout_2.addWidget(self.horizontalSlider, 1, 0, 1, 1)
        self.gridLayoutWidget_2 = QtGui.QWidget(self.tab_2)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(10, 140, 321, 51))
        self.gridLayoutWidget_2.setObjectName(_fromUtf8("gridLayoutWidget_2"))
        self.gridLayout_3 = QtGui.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_3.setMargin(0)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.label_7 = QtGui.QLabel(self.gridLayoutWidget_2)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout_3.addWidget(self.label_7, 0, 0, 1, 1)
        self.spinBox_2 = QtGui.QSpinBox(self.gridLayoutWidget_2)
        self.spinBox_2.setObjectName(_fromUtf8("spinBox_2"))
        self.gridLayout_3.addWidget(self.spinBox_2, 1, 1, 1, 1)
        self.horizontalSlider_2 = QtGui.QSlider(self.gridLayoutWidget_2)
        self.horizontalSlider_2.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_2.setObjectName(_fromUtf8("horizontalSlider_2"))
        self.gridLayout_3.addWidget(self.horizontalSlider_2, 1, 0, 1, 1)
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.cmdStartEditor = QtGui.QPushButton(self.tab_3)
        self.cmdStartEditor.setGeometry(QtCore.QRect(10, 200, 85, 31))
        self.cmdStartEditor.setObjectName(_fromUtf8("cmdStartEditor"))
        self.verticalLayoutWidget = QtGui.QWidget(self.tab_3)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 321, 61))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_3.setMargin(0)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.label_5 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.verticalLayout_3.addWidget(self.label_5)
        self.cmbProjects = QtGui.QComboBox(self.verticalLayoutWidget)
        self.cmbProjects.setObjectName(_fromUtf8("cmbProjects"))
        self.verticalLayout_3.addWidget(self.cmbProjects)
        self.horizontalLayoutWidget = QtGui.QWidget(self.tab_3)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 80, 321, 33))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_4.setMargin(0)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.chkRemoveVoluminas = QtGui.QCheckBox(self.horizontalLayoutWidget)
        self.chkRemoveVoluminas.setObjectName(_fromUtf8("chkRemoveVoluminas"))
        self.horizontalLayout_4.addWidget(self.chkRemoveVoluminas)
        self.nutRemoveVoluminas = QtGui.QSpinBox(self.horizontalLayoutWidget)
        self.nutRemoveVoluminas.setObjectName(_fromUtf8("nutRemoveVoluminas"))
        self.horizontalLayout_4.addWidget(self.nutRemoveVoluminas)
        self.horizontalLayoutWidget_2 = QtGui.QWidget(self.tab_3)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 120, 321, 33))
        self.horizontalLayoutWidget_2.setObjectName(_fromUtf8("horizontalLayoutWidget_2"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_5.setMargin(0)
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.chkFillCavitis = QtGui.QCheckBox(self.horizontalLayoutWidget_2)
        self.chkFillCavitis.setObjectName(_fromUtf8("chkFillCavitis"))
        self.horizontalLayout_5.addWidget(self.chkFillCavitis)
        self.tabWidget.addTab(self.tab_3, _fromUtf8(""))
        self.gridLayout.addWidget(self.tabWidget, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 366, 29))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Convert", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Folder with DICOM files:", None, QtGui.QApplication.UnicodeUTF8))
        self.txtDcm.setText(QtGui.QApplication.translate("MainWindow", "multiImageTest/", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdDcm.setText(QtGui.QApplication.translate("MainWindow", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdStartConvert.setText(QtGui.QApplication.translate("MainWindow", "START", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QtGui.QApplication.translate("MainWindow", "convert DCM", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MainWindow", "Project name:", None, QtGui.QApplication.UnicodeUTF8))
        self.txtProject.setText(QtGui.QApplication.translate("MainWindow", "testImage", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("MainWindow", ".sav", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdStartToSave.setText(QtGui.QApplication.translate("MainWindow", "START", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("MainWindow", "minimum gray value", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("MainWindow", "maximum gray value", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QtGui.QApplication.translate("MainWindow", "generate Project", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdStartEditor.setText(QtGui.QApplication.translate("MainWindow", "START", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("MainWindow", "select project:", None, QtGui.QApplication.UnicodeUTF8))
        self.chkRemoveVoluminas.setText(QtGui.QApplication.translate("MainWindow", "remove voluminas smaller than:", None, QtGui.QApplication.UnicodeUTF8))
        self.chkFillCavitis.setText(QtGui.QApplication.translate("MainWindow", "fill cavitis", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QtGui.QApplication.translate("MainWindow", "start Editor", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

