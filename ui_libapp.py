# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'libapp.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1121, 761)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(20)
        MainWindow.setFont(font)
        self.actionMain_menu = QAction(MainWindow)
        self.actionMain_menu.setObjectName(u"actionMain_menu")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.Stack = QStackedWidget(self.centralwidget)
        self.Stack.setObjectName(u"Stack")
        self.home = QWidget()
        self.home.setObjectName(u"home")
        self.gridLayout_5 = QGridLayout(self.home)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.homeLabel1 = QLabel(self.home)
        self.homeLabel1.setObjectName(u"homeLabel1")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.homeLabel1.sizePolicy().hasHeightForWidth())
        self.homeLabel1.setSizePolicy(sizePolicy1)
        font1 = QFont()
        font1.setFamily(u"DejaVu Sans")
        font1.setPointSize(28)
        font1.setBold(True)
        font1.setWeight(75)
        self.homeLabel1.setFont(font1)
        self.homeLabel1.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.verticalLayout.addWidget(self.homeLabel1)

        self.homeLabel2 = QLabel(self.home)
        self.homeLabel2.setObjectName(u"homeLabel2")
        sizePolicy1.setHeightForWidth(self.homeLabel2.sizePolicy().hasHeightForWidth())
        self.homeLabel2.setSizePolicy(sizePolicy1)
        font2 = QFont()
        font2.setPointSize(22)
        self.homeLabel2.setFont(font2)
        self.homeLabel2.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.homeLabel2)


        self.gridLayout_5.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.loginLineEdit = QLineEdit(self.home)
        self.loginLineEdit.setObjectName(u"loginLineEdit")
        self.loginLineEdit.setEnabled(True)
        sizePolicy2 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.loginLineEdit.sizePolicy().hasHeightForWidth())
        self.loginLineEdit.setSizePolicy(sizePolicy2)
        font3 = QFont()
        font3.setPointSize(21)
        self.loginLineEdit.setFont(font3)

        self.horizontalLayout_2.addWidget(self.loginLineEdit)

        self.submitLoginButton = QPushButton(self.home)
        self.submitLoginButton.setObjectName(u"submitLoginButton")
        sizePolicy3 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.submitLoginButton.sizePolicy().hasHeightForWidth())
        self.submitLoginButton.setSizePolicy(sizePolicy3)
        self.submitLoginButton.setFont(font2)

        self.horizontalLayout_2.addWidget(self.submitLoginButton)


        self.gridLayout_5.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)

        self.Stack.addWidget(self.home)
        self.client_home_page = QWidget()
        self.client_home_page.setObjectName(u"client_home_page")
        self.gridLayout_3 = QGridLayout(self.client_home_page)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.clientHomeQstLabel = QLabel(self.client_home_page)
        self.clientHomeQstLabel.setObjectName(u"clientHomeQstLabel")
        sizePolicy.setHeightForWidth(self.clientHomeQstLabel.sizePolicy().hasHeightForWidth())
        self.clientHomeQstLabel.setSizePolicy(sizePolicy)
        font4 = QFont()
        font4.setFamily(u"DejaVu Sans")
        font4.setPointSize(20)
        font4.setBold(True)
        font4.setWeight(75)
        self.clientHomeQstLabel.setFont(font4)
        self.clientHomeQstLabel.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.clientHomeQstLabel, 2, 0, 1, 1)

        self.clientHomeWelcomeLabel = QLabel(self.client_home_page)
        self.clientHomeWelcomeLabel.setObjectName(u"clientHomeWelcomeLabel")
        sizePolicy1.setHeightForWidth(self.clientHomeWelcomeLabel.sizePolicy().hasHeightForWidth())
        self.clientHomeWelcomeLabel.setSizePolicy(sizePolicy1)
        self.clientHomeWelcomeLabel.setFont(font4)
        self.clientHomeWelcomeLabel.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.clientHomeWelcomeLabel, 1, 0, 1, 1)

        self.helloClientLabel = QLabel(self.client_home_page)
        self.helloClientLabel.setObjectName(u"helloClientLabel")
        sizePolicy1.setHeightForWidth(self.helloClientLabel.sizePolicy().hasHeightForWidth())
        self.helloClientLabel.setSizePolicy(sizePolicy1)
        font5 = QFont()
        font5.setFamily(u"DejaVu Sans")
        font5.setPointSize(29)
        font5.setBold(True)
        font5.setWeight(75)
        self.helloClientLabel.setFont(font5)
        self.helloClientLabel.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.helloClientLabel, 0, 0, 1, 1)


        self.verticalLayout_4.addLayout(self.gridLayout)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.clientDisplayRentingsButton = QPushButton(self.client_home_page)
        self.clientDisplayRentingsButton.setObjectName(u"clientDisplayRentingsButton")
        sizePolicy4 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.MinimumExpanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.clientDisplayRentingsButton.sizePolicy().hasHeightForWidth())
        self.clientDisplayRentingsButton.setSizePolicy(sizePolicy4)
        font6 = QFont()
        font6.setFamily(u"DejaVu Sans")
        font6.setPointSize(20)
        font6.setBold(False)
        font6.setWeight(50)
        self.clientDisplayRentingsButton.setFont(font6)

        self.gridLayout_2.addWidget(self.clientDisplayRentingsButton, 1, 0, 1, 1)

        self.clientDisplayHistoryButton = QPushButton(self.client_home_page)
        self.clientDisplayHistoryButton.setObjectName(u"clientDisplayHistoryButton")
        sizePolicy4.setHeightForWidth(self.clientDisplayHistoryButton.sizePolicy().hasHeightForWidth())
        self.clientDisplayHistoryButton.setSizePolicy(sizePolicy4)
        self.clientDisplayHistoryButton.setFont(font6)

        self.gridLayout_2.addWidget(self.clientDisplayHistoryButton, 2, 0, 1, 1)

        self.clientDisplayBooksButton = QPushButton(self.client_home_page)
        self.clientDisplayBooksButton.setObjectName(u"clientDisplayBooksButton")
        sizePolicy4.setHeightForWidth(self.clientDisplayBooksButton.sizePolicy().hasHeightForWidth())
        self.clientDisplayBooksButton.setSizePolicy(sizePolicy4)
        self.clientDisplayBooksButton.setFont(font6)

        self.gridLayout_2.addWidget(self.clientDisplayBooksButton, 0, 0, 1, 1)

        self.clientLogoutButton = QPushButton(self.client_home_page)
        self.clientLogoutButton.setObjectName(u"clientLogoutButton")
        sizePolicy4.setHeightForWidth(self.clientLogoutButton.sizePolicy().hasHeightForWidth())
        self.clientLogoutButton.setSizePolicy(sizePolicy4)
        self.clientLogoutButton.setFont(font6)

        self.gridLayout_2.addWidget(self.clientLogoutButton, 3, 0, 1, 1)


        self.verticalLayout_4.addLayout(self.gridLayout_2)


        self.gridLayout_3.addLayout(self.verticalLayout_4, 0, 0, 1, 1)

        self.Stack.addWidget(self.client_home_page)
        self.client_display_books_page = QWidget()
        self.client_display_books_page.setObjectName(u"client_display_books_page")
        self.gridLayout_6 = QGridLayout(self.client_display_books_page)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.mainMenuButton0 = QPushButton(self.client_display_books_page)
        self.mainMenuButton0.setObjectName(u"mainMenuButton0")
        sizePolicy5 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Maximum)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.mainMenuButton0.sizePolicy().hasHeightForWidth())
        self.mainMenuButton0.setSizePolicy(sizePolicy5)
        font7 = QFont()
        font7.setFamily(u"DejaVu Sans")
        font7.setPointSize(21)
        font7.setBold(True)
        font7.setWeight(75)
        self.mainMenuButton0.setFont(font7)

        self.verticalLayout_5.addWidget(self.mainMenuButton0)

        self.splitter = QSplitter(self.client_display_books_page)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.listOfGenres = QListWidget(self.splitter)
        self.listOfGenres.setObjectName(u"listOfGenres")
        sizePolicy6 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.listOfGenres.sizePolicy().hasHeightForWidth())
        self.listOfGenres.setSizePolicy(sizePolicy6)
        font8 = QFont()
        font8.setFamily(u"DejaVu Sans")
        font8.setPointSize(17)
        self.listOfGenres.setFont(font8)
        self.splitter.addWidget(self.listOfGenres)
        self.genreStackWidget = QStackedWidget(self.splitter)
        self.genreStackWidget.setObjectName(u"genreStackWidget")
        sizePolicy7 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.genreStackWidget.sizePolicy().hasHeightForWidth())
        self.genreStackWidget.setSizePolicy(sizePolicy7)
        self.book_info_page = QWidget()
        self.book_info_page.setObjectName(u"book_info_page")
        self.verticalLayout_6 = QVBoxLayout(self.book_info_page)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.splitter_3 = QSplitter(self.book_info_page)
        self.splitter_3.setObjectName(u"splitter_3")
        self.splitter_3.setOrientation(Qt.Vertical)
        self.listOfBooks = QListWidget(self.splitter_3)
        self.listOfBooks.setObjectName(u"listOfBooks")
        sizePolicy8 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.listOfBooks.sizePolicy().hasHeightForWidth())
        self.listOfBooks.setSizePolicy(sizePolicy8)
        self.listOfBooks.setFont(font8)
        self.splitter_3.addWidget(self.listOfBooks)
        self.bookStackedWidget = QStackedWidget(self.splitter_3)
        self.bookStackedWidget.setObjectName(u"bookStackedWidget")
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.verticalLayout_7 = QVBoxLayout(self.page_3)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.chooseBookLabel = QLabel(self.page_3)
        self.chooseBookLabel.setObjectName(u"chooseBookLabel")
        self.chooseBookLabel.setFont(font7)
        self.chooseBookLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.chooseBookLabel)

        self.bookStackedWidget.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.verticalLayout_3 = QVBoxLayout(self.page_4)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.bookInfo = QLabel(self.page_4)
        self.bookInfo.setObjectName(u"bookInfo")
        sizePolicy1.setHeightForWidth(self.bookInfo.sizePolicy().hasHeightForWidth())
        self.bookInfo.setSizePolicy(sizePolicy1)
        font9 = QFont()
        font9.setFamily(u"DejaVu Sans")
        font9.setPointSize(15)
        font9.setBold(True)
        font9.setWeight(75)
        self.bookInfo.setFont(font9)
        self.bookInfo.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_3.addWidget(self.bookInfo)

        self.bookBorrowButton = QPushButton(self.page_4)
        self.bookBorrowButton.setObjectName(u"bookBorrowButton")
        sizePolicy9 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.bookBorrowButton.sizePolicy().hasHeightForWidth())
        self.bookBorrowButton.setSizePolicy(sizePolicy9)
        font10 = QFont()
        font10.setFamily(u"DejaVu Sans")
        font10.setPointSize(15)
        self.bookBorrowButton.setFont(font10)

        self.verticalLayout_3.addWidget(self.bookBorrowButton)

        self.reservationButton = QPushButton(self.page_4)
        self.reservationButton.setObjectName(u"reservationButton")
        sizePolicy9.setHeightForWidth(self.reservationButton.sizePolicy().hasHeightForWidth())
        self.reservationButton.setSizePolicy(sizePolicy9)
        self.reservationButton.setFont(font10)

        self.verticalLayout_3.addWidget(self.reservationButton)

        self.bookStackedWidget.addWidget(self.page_4)
        self.splitter_3.addWidget(self.bookStackedWidget)

        self.verticalLayout_6.addWidget(self.splitter_3)

        self.genreStackWidget.addWidget(self.book_info_page)
        self.book_home_page = QWidget()
        self.book_home_page.setObjectName(u"book_home_page")
        self.gridLayout_4 = QGridLayout(self.book_home_page)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.chooseGenreLabel = QLabel(self.book_home_page)
        self.chooseGenreLabel.setObjectName(u"chooseGenreLabel")
        self.chooseGenreLabel.setFont(font7)
        self.chooseGenreLabel.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.chooseGenreLabel, 0, 0, 1, 1)

        self.genreStackWidget.addWidget(self.book_home_page)
        self.splitter.addWidget(self.genreStackWidget)

        self.verticalLayout_5.addWidget(self.splitter)


        self.gridLayout_6.addLayout(self.verticalLayout_5, 0, 0, 1, 1)

        self.Stack.addWidget(self.client_display_books_page)
        self.client_display_rentings_page = QWidget()
        self.client_display_rentings_page.setObjectName(u"client_display_rentings_page")
        self.verticalLayout_8 = QVBoxLayout(self.client_display_rentings_page)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.mainMenuButtron1 = QPushButton(self.client_display_rentings_page)
        self.mainMenuButtron1.setObjectName(u"mainMenuButtron1")
        self.mainMenuButtron1.setFont(font7)

        self.verticalLayout_2.addWidget(self.mainMenuButtron1)

        self.splitter_2 = QSplitter(self.client_display_rentings_page)
        self.splitter_2.setObjectName(u"splitter_2")
        self.splitter_2.setOrientation(Qt.Horizontal)
        self.currentRentingList = QListWidget(self.splitter_2)
        self.currentRentingList.setObjectName(u"currentRentingList")
        self.splitter_2.addWidget(self.currentRentingList)
        self.curRentingStack = QStackedWidget(self.splitter_2)
        self.curRentingStack.setObjectName(u"curRentingStack")
        sizePolicy10 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy10.setHorizontalStretch(0)
        sizePolicy10.setVerticalStretch(0)
        sizePolicy10.setHeightForWidth(self.curRentingStack.sizePolicy().hasHeightForWidth())
        self.curRentingStack.setSizePolicy(sizePolicy10)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.verticalLayout_9 = QVBoxLayout(self.page)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.chooseRentingLabel = QLabel(self.page)
        self.chooseRentingLabel.setObjectName(u"chooseRentingLabel")
        self.chooseRentingLabel.setFont(font7)
        self.chooseRentingLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.chooseRentingLabel)

        self.curRentingStack.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.verticalLayout_11 = QVBoxLayout(self.page_2)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.rentingBookInfo = QLabel(self.page_2)
        self.rentingBookInfo.setObjectName(u"rentingBookInfo")
        sizePolicy11 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy11.setHorizontalStretch(0)
        sizePolicy11.setVerticalStretch(0)
        sizePolicy11.setHeightForWidth(self.rentingBookInfo.sizePolicy().hasHeightForWidth())
        self.rentingBookInfo.setSizePolicy(sizePolicy11)
        font11 = QFont()
        font11.setFamily(u"DejaVu Sans")
        font11.setPointSize(16)
        font11.setBold(True)
        font11.setWeight(75)
        self.rentingBookInfo.setFont(font11)

        self.verticalLayout_10.addWidget(self.rentingBookInfo)

        self.rentingInfo = QLabel(self.page_2)
        self.rentingInfo.setObjectName(u"rentingInfo")
        self.rentingInfo.setFont(font11)
        self.rentingInfo.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_10.addWidget(self.rentingInfo)

        self.returnBookButton = QPushButton(self.page_2)
        self.returnBookButton.setObjectName(u"returnBookButton")
        self.returnBookButton.setFont(font10)

        self.verticalLayout_10.addWidget(self.returnBookButton)

        self.renewRentingButton = QPushButton(self.page_2)
        self.renewRentingButton.setObjectName(u"renewRentingButton")
        self.renewRentingButton.setFont(font10)

        self.verticalLayout_10.addWidget(self.renewRentingButton)


        self.verticalLayout_11.addLayout(self.verticalLayout_10)

        self.curRentingStack.addWidget(self.page_2)
        self.splitter_2.addWidget(self.curRentingStack)

        self.verticalLayout_2.addWidget(self.splitter_2)


        self.verticalLayout_8.addLayout(self.verticalLayout_2)

        self.Stack.addWidget(self.client_display_rentings_page)
        self.client_display_history_page = QWidget()
        self.client_display_history_page.setObjectName(u"client_display_history_page")
        self.Stack.addWidget(self.client_display_history_page)
        self.librarian_home_page = QWidget()
        self.librarian_home_page.setObjectName(u"librarian_home_page")
        self.label = QLabel(self.librarian_home_page)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(120, 30, 59, 15))
        self.Stack.addWidget(self.librarian_home_page)

        self.horizontalLayout.addWidget(self.Stack)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.Stack.setCurrentIndex(3)
        self.genreStackWidget.setCurrentIndex(0)
        self.bookStackedWidget.setCurrentIndex(1)
        self.curRentingStack.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"LibApp", None))
        self.actionMain_menu.setText(QCoreApplication.translate("MainWindow", u"Main menu", None))
        self.homeLabel1.setText(QCoreApplication.translate("MainWindow", u"Welcome to LibApp", None))
        self.homeLabel2.setText(QCoreApplication.translate("MainWindow", u"Please, enter your login", None))
        self.loginLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter your login here...", None))
        self.submitLoginButton.setText(QCoreApplication.translate("MainWindow", u"Submit", None))
        self.clientHomeQstLabel.setText(QCoreApplication.translate("MainWindow", u"What would you like to do?", None))
        self.clientHomeWelcomeLabel.setText(QCoreApplication.translate("MainWindow", u"Welcome to your account.", None))
        self.helloClientLabel.setText(QCoreApplication.translate("MainWindow", u"Hello!", None))
        self.clientDisplayRentingsButton.setText(QCoreApplication.translate("MainWindow", u"Display current rentings", None))
        self.clientDisplayHistoryButton.setText(QCoreApplication.translate("MainWindow", u"Display my renting history", None))
        self.clientDisplayBooksButton.setText(QCoreApplication.translate("MainWindow", u"Display list of books", None))
        self.clientLogoutButton.setText(QCoreApplication.translate("MainWindow", u"Logout", None))
        self.mainMenuButton0.setText(QCoreApplication.translate("MainWindow", u"Main Menu", None))
        self.chooseBookLabel.setText(QCoreApplication.translate("MainWindow", u"Choose book from list", None))
        self.bookInfo.setText("")
        self.bookBorrowButton.setText(QCoreApplication.translate("MainWindow", u"Borrow book", None))
        self.reservationButton.setText(QCoreApplication.translate("MainWindow", u"Make reservation", None))
        self.chooseGenreLabel.setText(QCoreApplication.translate("MainWindow", u"Choose genre from list", None))
        self.mainMenuButtron1.setText(QCoreApplication.translate("MainWindow", u"Main Menu", None))
        self.chooseRentingLabel.setText(QCoreApplication.translate("MainWindow", u"Choose renting from list", None))
        self.rentingBookInfo.setText("")
        self.rentingInfo.setText("")
        self.returnBookButton.setText(QCoreApplication.translate("MainWindow", u"Return book to library", None))
        self.renewRentingButton.setText(QCoreApplication.translate("MainWindow", u"Renew renting", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
    # retranslateUi

