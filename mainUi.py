# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Temp/untitled.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import pywintypes

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setGeometry(0, 0, 400, 550)
        MainWindow.setWindowModality(QtCore.Qt.ApplicationModal)
        MainWindow.resize(400, 550)
        MainWindow.setMinimumSize(QtCore.QSize(400, 550))
        icon = QtGui.QIcon()
        icon.addFile("icon/KSB_2.ico", QtCore.QSize(48, 48))
        MainWindow.setWindowIcon(icon)
        MainWindow.setWindowOpacity(2.0)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.lo_main = QtWidgets.QVBoxLayout()
        self.lo_main.setObjectName("lo_main")
        self.tab_main = QtWidgets.QTabWidget(self.centralwidget)
        self.tab_main.setEnabled(True)
        self.tab_main.setTabPosition(QtWidgets.QTabWidget.North)
        self.tab_main.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tab_main.setUsesScrollButtons(True)
        self.tab_main.setDocumentMode(False)
        self.tab_main.setTabsClosable(False)
        self.tab_main.setMovable(False)
        self.tab_main.setTabBarAutoHide(False)
        self.tab_main.setObjectName("tab_main")

        self.w_student_news = QtWidgets.QWidget()
        self.w_student_news.setObjectName("w_student_news")
        self.horizontalLayout_1 = QtWidgets.QHBoxLayout(self.w_student_news)
        self.horizontalLayout_1.setObjectName("horizontalLayout_1")
        self.li_student_news = QtWidgets.QListWidget(self.w_student_news)
        self.li_student_news.setObjectName("li_student_news")
        self.horizontalLayout_1.addWidget(self.li_student_news)
        self.tab_main.addTab(self.w_student_news, "")

        self.w_executive_news = QtWidgets.QWidget()
        self.w_executive_news.setObjectName("w_executive_news")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.w_executive_news)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.li_executive_news = QtWidgets.QListWidget(self.w_executive_news)
        self.li_executive_news.setObjectName("li_executive_news")
        self.horizontalLayout_2.addWidget(self.li_executive_news)
        self.tab_main.addTab(self.w_executive_news, "")

        self.w_work_news = QtWidgets.QWidget()
        self.w_work_news.setObjectName("w_work_news")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.w_work_news)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.li_work_news = QtWidgets.QListWidget(self.w_work_news)
        self.li_work_news.setObjectName("li_work_news")
        self.horizontalLayout_3.addWidget(self.li_work_news)
        self.tab_main.addTab(self.w_work_news, "")

        self.w_hot_news = QtWidgets.QWidget()
        self.w_hot_news.setObjectName("w_hot_news")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.w_hot_news)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.li_hot_news = QtWidgets.QListWidget(self.w_hot_news)
        self.li_hot_news.setObjectName("li_hot_news")
        self.horizontalLayout_4.addWidget(self.li_hot_news)
        self.tab_main.addTab(self.w_hot_news, "")

        self.w_career = QtWidgets.QWidget()
        self.w_career.setObjectName("w_career")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.w_career)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.li_career = QtWidgets.QListWidget(self.w_career)
        self.li_career.setObjectName("li_career")
        self.horizontalLayout_5.addWidget(self.li_career)
        self.tab_main.addTab(self.w_career, "")

        self.lo_main.addWidget(self.tab_main)
        self.gridLayout.addLayout(self.lo_main, 1, 0, 1, 1)
        self.lo_menu = QtWidgets.QHBoxLayout()
        self.lo_menu.setObjectName("lo_menu")



        self.bt_set = QtWidgets.QPushButton(self.centralwidget)
        self.bt_set.setText("")
        iconSet = QtGui.QIcon()
        iconSet.addPixmap(QtGui.QPixmap("icon/icon_set.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bt_set.setIcon(iconSet)
        self.bt_set.setObjectName("bt_set")
        self.lo_menu.addWidget(self.bt_set)

        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.lo_menu.addItem(spacerItem)

        self.bt_home = QtWidgets.QPushButton(self.centralwidget)
        self.bt_home.setText("")
        iconSet = QtGui.QIcon()
        iconSet.addPixmap(QtGui.QPixmap("icon/icon_home.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bt_home.setIcon(iconSet)
        self.bt_home.setObjectName("bt_home")
        self.lo_menu.addWidget(self.bt_home)

        self.bt_diet = QtWidgets.QPushButton(self.centralwidget)
        self.bt_diet.setText("")
        iconDiet = QtGui.QIcon()
        iconDiet.addPixmap(QtGui.QPixmap("icon/icon_diet.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bt_diet.setIcon(iconDiet)
        self.bt_diet.setObjectName("bt_diet")
        self.lo_menu.addWidget(self.bt_diet)

        self.bt_refresh = QtWidgets.QPushButton(self.centralwidget)
        self.bt_refresh.setText("")
        self.iconRefresh = QtGui.QIcon()
        self.iconRefresh.addPixmap(QtGui.QPixmap("icon/icon_refresh.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bt_refresh.setIcon(self.iconRefresh)
        self.bt_refresh.setObjectName("bt_refresh")
        self.lo_menu.addWidget(self.bt_refresh)

        self.gridLayout.addLayout(self.lo_menu, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tab_main.setCurrentIndex(0)
        self.tab_main.currentChanged.connect(MainWindow.remove_dot)

        # self.bt_set.clicked.connect(MainWindow.set)
        self.bt_home.clicked.connect(MainWindow.to_home)
        self.bt_diet.clicked.connect(MainWindow.diet)
        self.bt_refresh.clicked.connect(MainWindow.refresh)

        # 아이콘
        self.iconDot = QtGui.QIcon()
        self.iconDot.addPixmap(QtGui.QPixmap("icon/icon_dot.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.iconNull = QtGui.QIcon()

        self.li_student_news.setSpacing(3)
        self.li_executive_news.setSpacing(3)
        self.li_work_news.setSpacing(3)
        self.li_hot_news.setSpacing(3)
        self.li_career.setSpacing(3)

        self.li_student_news.itemDoubleClicked.connect(
            lambda: MainWindow.to_page(self.tab_main.currentIndex(), self.li_student_news.currentItem().text()))
        self.li_executive_news.itemDoubleClicked.connect(
            lambda: MainWindow.to_page(self.tab_main.currentIndex(), self.li_executive_news.currentItem().text()))
        self.li_work_news.itemDoubleClicked.connect(
            lambda: MainWindow.to_page(self.tab_main.currentIndex(), self.li_work_news.currentItem().text()))
        self.li_hot_news.itemDoubleClicked.connect(
            lambda: MainWindow.to_page(self.tab_main.currentIndex(), self.li_hot_news.currentItem().text()))
        self.li_career.itemDoubleClicked.connect(
            lambda: MainWindow.to_page(self.tab_main.currentIndex(), self.li_career.currentItem().text()))

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "KongjuSoBa"))
        self.tab_main.setTabText(self.tab_main.indexOf(self.w_student_news), _translate("MainWindow", "학생"))
        self.tab_main.setTabText(self.tab_main.indexOf(self.w_executive_news), _translate("MainWindow", "행정"))
        self.tab_main.setTabText(self.tab_main.indexOf(self.w_work_news), _translate("MainWindow", "행사"))
        self.tab_main.setTabText(self.tab_main.indexOf(self.w_hot_news), _translate("MainWindow", "HOT"))
        self.tab_main.setTabText(self.tab_main.indexOf(self.w_career), _translate("MainWindow", "취업"))
