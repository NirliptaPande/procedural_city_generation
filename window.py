# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from GUI import matplotlibWidget
from PyQt5 import QtCore, QtGui, QtWidgets

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
        return QtWidgets.QApplication.translate(context, text, disambig)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1059, 766)
        self.Centralwidget = QtWidgets.QWidget(MainWindow)
        self.Centralwidget.setObjectName(_fromUtf8("Centralwidget"))
        self.gridLayout = QtWidgets.QGridLayout(self.Centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.console = QtWidgets.QPlainTextEdit(self.Centralwidget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,
                         QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,
                         QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,
                         QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,
                         QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(159, 158, 158))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,
                         QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(159, 158, 158))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(159, 158, 158))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,
                         QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.console.setPalette(palette)
        self.console.setObjectName(_fromUtf8("console"))
        self.gridLayout.addWidget(self.console, 4, 0, 1, 1)
        self.console_header = QtWidgets.QGroupBox(self.Centralwidget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(189, 189, 189))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(180, 180, 180))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(189, 189, 189))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(180, 180, 180))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(189, 189, 189))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.console_header.setPalette(palette)
        self.console_header.setObjectName(_fromUtf8("console_header"))
        self.gridLayout.addWidget(self.console_header, 3, 0, 1, 1)
        self.tabWidget = QtWidgets.QTabWidget(self.Centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(3)
        sizePolicy.setHeightForWidth(
            self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setMinimumSize(QtCore.QSize(981, 0))
        self.tabWidget.setIconSize(QtCore.QSize(16, 16))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.roadmap_tab = QtWidgets.QWidget()
        self.roadmap_tab.setObjectName(_fromUtf8("roadmap_tab"))
        self.gridLayout_2 = QtWidgets.QGridLayout(self.roadmap_tab)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.roadmap_splitter = QtWidgets.QSplitter(self.roadmap_tab)
        self.roadmap_splitter.setOrientation(QtCore.Qt.Horizontal)
        self.roadmap_splitter.setChildrenCollapsible(False)
        self.roadmap_splitter.setObjectName(_fromUtf8("roadmap_splitter"))
        self.roadmap_group = QtWidgets.QGroupBox(self.roadmap_splitter)
        self.roadmap_group.setObjectName(_fromUtf8("roadmap_group"))
        self.roadmap_Options = QtWidgets.QPushButton(self.roadmap_group)
        self.roadmap_Options.setGeometry(QtCore.QRect(10, 30, 81, 27))
        self.roadmap_Options.setObjectName(_fromUtf8("roadmap_Options"))
        self.roadmap_Run = QtWidgets.QPushButton(self.roadmap_group)
        self.roadmap_Run.setGeometry(QtCore.QRect(10, 60, 81, 27))
        self.roadmap_Run.setObjectName(_fromUtf8("roadmap_Run"))
        self.roadmap_frame = QtWidgets.QFrame(self.roadmap_splitter)
        self.roadmap_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.roadmap_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.roadmap_frame.setObjectName(_fromUtf8("roadmap_frame"))
        self.gridLayout_7 = QtWidgets.QGridLayout(self.roadmap_frame)
        self.gridLayout_7.setObjectName(_fromUtf8("gridLayout_7"))
        self.roadmap_widget = matplotlibWidget(self.roadmap_frame)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.roadmap_widget.sizePolicy().hasHeightForWidth())
        self.roadmap_widget.setSizePolicy(sizePolicy)
        self.roadmap_widget.setObjectName(_fromUtf8("roadmap_widget"))
        self.gridLayout_7.addWidget(self.roadmap_widget, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.roadmap_splitter, 0, 0, 1, 1)
        self.tabWidget.addTab(self.roadmap_tab, _fromUtf8(""))
        self.polygons_tab = QtWidgets.QWidget()
        self.polygons_tab.setObjectName(_fromUtf8("polygons_tab"))
        self.gridLayout_3 = QtWidgets.QGridLayout(self.polygons_tab)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.polygons_splitter = QtWidgets.QSplitter(self.polygons_tab)
        self.polygons_splitter.setOrientation(QtCore.Qt.Horizontal)
        self.polygons_splitter.setChildrenCollapsible(False)
        self.polygons_splitter.setObjectName(_fromUtf8("polygons_splitter"))
        self.polygons_group = QtWidgets.QGroupBox(self.polygons_splitter)
        self.polygons_group.setObjectName(_fromUtf8("polygons_group"))
        self.polygons_Options = QtWidgets.QPushButton(self.polygons_group)
        self.polygons_Options.setGeometry(QtCore.QRect(10, 30, 81, 27))
        self.polygons_Options.setObjectName(_fromUtf8("polygons_Options"))
        self.polygons_Run = QtWidgets.QPushButton(self.polygons_group)
        self.polygons_Run.setGeometry(QtCore.QRect(10, 60, 81, 27))
        self.polygons_Run.setObjectName(_fromUtf8("polygons_Run"))
        self.polygons_frame = QtWidgets.QFrame(self.polygons_splitter)
        self.polygons_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.polygons_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.polygons_frame.setObjectName(_fromUtf8("polygons_frame"))
        self.gridLayout_8 = QtWidgets.QGridLayout(self.polygons_frame)
        self.gridLayout_8.setObjectName(_fromUtf8("gridLayout_8"))
        self.polygons_widget = matplotlibWidget(self.polygons_frame)
        self.polygons_widget.setObjectName(_fromUtf8("polygons_widget"))
        self.gridLayout_8.addWidget(self.polygons_widget, 0, 0, 1, 1)
        self.gridLayout_3.addWidget(self.polygons_splitter, 0, 0, 1, 1)
        self.tabWidget.addTab(self.polygons_tab, _fromUtf8(""))
        self.building_generation_tab = QtWidgets.QWidget()
        self.building_generation_tab.setObjectName(
            _fromUtf8("building_generation_tab"))
        self.gridLayout_4 = QtWidgets.QGridLayout(self.building_generation_tab)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.building_generation_splitter = QtWidgets.QSplitter(
            self.building_generation_tab)
        self.building_generation_splitter.setOrientation(QtCore.Qt.Horizontal)
        self.building_generation_splitter.setChildrenCollapsible(False)
        self.building_generation_splitter.setObjectName(
            _fromUtf8("building_generation_splitter"))
        self.building_generation_group = QtWidgets.QGroupBox(
            self.building_generation_splitter)
        self.building_generation_group.setObjectName(
            _fromUtf8("building_generation_group"))
        self.building_generation_Options = QtWidgets.QPushButton(
            self.building_generation_group)
        self.building_generation_Options.setGeometry(
            QtCore.QRect(10, 30, 81, 27))
        self.building_generation_Options.setObjectName(
            _fromUtf8("building_generation_Options"))
        self.building_generation_Run = QtWidgets.QPushButton(
            self.building_generation_group)
        self.building_generation_Run.setGeometry(QtCore.QRect(10, 60, 81, 27))
        self.building_generation_Run.setObjectName(
            _fromUtf8("building_generation_Run"))
        self.building_generation_frame = QtWidgets.QFrame(
            self.building_generation_splitter)
        self.building_generation_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.building_generation_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.building_generation_frame.setObjectName(
            _fromUtf8("building_generation_frame"))
        self.gridLayout_9 = QtWidgets.QGridLayout(
            self.building_generation_frame)
        self.gridLayout_9.setObjectName(_fromUtf8("gridLayout_9"))
        self.building_generation_widget = matplotlibWidget(
            self.building_generation_frame)
        self.building_generation_widget.setObjectName(
            _fromUtf8("building_generation_widget"))
        self.gridLayout_9.addWidget(
            self.building_generation_widget, 0, 0, 1, 1)
        self.gridLayout_4.addWidget(
            self.building_generation_splitter, 0, 0, 1, 1)
        # self.tabWidget.addTab(self.building_generation_tab, _fromUtf8(""))
        self.visualization_tab = QtWidgets.QWidget()
        self.visualization_tab.setObjectName(_fromUtf8("visualization_tab"))
        self.gridLayout_5 = QtWidgets.QGridLayout(self.visualization_tab)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.visualization_splitter = QtWidgets.QSplitter(
            self.visualization_tab)
        self.visualization_splitter.setOrientation(QtCore.Qt.Horizontal)
        self.visualization_splitter.setChildrenCollapsible(False)
        self.visualization_splitter.setObjectName(
            _fromUtf8("visualization_splitter"))
        self.visualization_group = QtWidgets.QGroupBox(
            self.visualization_splitter)
        self.visualization_group.setObjectName(
            _fromUtf8("visualization_group"))
        self.visualization_Options = QtWidgets.QPushButton(
            self.visualization_group)
        self.visualization_Options.setGeometry(QtCore.QRect(10, 30, 81, 27))
        self.visualization_Options.setObjectName(
            _fromUtf8("visualization_Options"))
        self.visualization_Run = QtWidgets.QPushButton(
            self.visualization_group)
        self.visualization_Run.setGeometry(QtCore.QRect(10, 60, 81, 27))
        self.visualization_Run.setObjectName(_fromUtf8("visualization_Run"))
        self.visualization_frame = QtWidgets.QFrame(self.visualization_splitter)
        self.visualization_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.visualization_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.visualization_frame.setObjectName(
            _fromUtf8("visualization_frame"))
        self.gridLayout_5.addWidget(self.visualization_splitter, 0, 0, 1, 1)
        self.tabWidget.addTab(self.visualization_tab, _fromUtf8(""))
        self.advanced_tab = QtWidgets.QWidget()
        self.advanced_tab.setObjectName(_fromUtf8("advanced_tab"))
        self.gridLayout_6 = QtWidgets.QGridLayout(self.advanced_tab)
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.advanced_group = QtWidgets.QGroupBox(self.advanced_tab)
        self.advanced_group.setObjectName(_fromUtf8("advanced_group"))
        self.clean_directories = QtWidgets.QPushButton(self.advanced_group)
        self.clean_directories.setGeometry(QtCore.QRect(10, 30, 201, 27))
        self.clean_directories.setObjectName(_fromUtf8("clean_directories"))
        self.run_tests = QtWidgets.QPushButton(self.advanced_group)
        self.run_tests.setGeometry(QtCore.QRect(10, 60, 201, 27))
        self.run_tests.setObjectName(_fromUtf8("run_tests"))
        self.gridLayout_6.addWidget(self.advanced_group, 0, 0, 1, 1)
        self.tabWidget.addTab(self.advanced_tab, _fromUtf8(""))
        self.gridLayout.addWidget(self.tabWidget, 2, 0, 1, 1)
        MainWindow.setCentralWidget(self.Centralwidget)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate(
            "MainWindow", "Procedural City Generation", None))
        self.console_header.setTitle(_translate(
            "MainWindow", "       Console", None))
        self.roadmap_group.setTitle(_translate("MainWindow", "Commands", None))
        self.roadmap_Options.setText(_translate("MainWindow", "Options", None))
        self.roadmap_Run.setText(_translate("MainWindow", "Run", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(
            self.roadmap_tab), _translate("MainWindow", "Roadmap Generation", None))
        self.polygons_group.setTitle(
            _translate("MainWindow", "Commands", None))
        self.polygons_Options.setText(
            _translate("MainWindow", "Options", None))
        self.polygons_Run.setText(_translate("MainWindow", "Run", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(
            self.polygons_tab), _translate("MainWindow", "Polygon Extraction", None))
        self.building_generation_group.setTitle(
            _translate("MainWindow", "Commands", None))
        self.building_generation_Options.setText(
            _translate("MainWindow", "Options", None))
        self.building_generation_Run.setText(
            _translate("MainWindow", "Run", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(
            self.building_generation_tab), _translate("MainWindow", "Building Generation", None))
        self.visualization_group.setTitle(
            _translate("MainWindow", "Commands", None))
        self.visualization_Options.setText(
            _translate("MainWindow", "Options", None))
        self.visualization_Run.setText(_translate("MainWindow", "Run", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(
            self.visualization_tab), _translate("MainWindow", "Visualize in Blender", None))
        self.advanced_group.setTitle(
            _translate("MainWindow", "Commands", None))
        self.clean_directories.setText(_translate(
            "MainWindow", "Clean Directories", None))
        self.run_tests.setText(_translate("MainWindow", "Run Tests", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(
            self.advanced_tab), _translate("MainWindow", "Advanced", None))
