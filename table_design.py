# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'table_design.ui'
##
## Created by: Qt User Interface Compiler version 6.6.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QSize, Qt)
from PySide6.QtGui import (QCursor,
                           QFont, QIcon)
from PySide6.QtWidgets import (QHBoxLayout, QLabel,
                               QLayout, QPushButton, QSizePolicy,
                               QTableWidget, QVBoxLayout, QWidget, QHeaderView)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QSize(0, 0))
        icon = QIcon()
        icon.addFile(u"icons/main.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"QWidget {\n"
"	color: white;\n"
"	background-color: #212121;\n"
"	font-family: Rubik;\n"
"	font-size: 14pt;\n"
"	font-weight: 600;\n"
"}\n"
"\n"
"QPushButton {\n"
"	background-color: transparent;\n"
"	border: none;\n"
"}\n"
"\n"
"QPushButton:hover{background-color: #666;}\n"
"QPushButton:pressed{background-color: #888;}\n"
"\n"
"#lbl_by {\n"
"	font-size: 11pt;\n"
"\n"
"}\n"
"\n"
"#hint {\n"
"	font-size: 11pt;\n"
"	font-weight: 400;\n"
"}\n"
"\n"
"\n"
"QListView {\n"
"		font-weight: 400;\n"
"}")
        MainWindow.setIconSize(QSize(75, 75))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_4 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)

        self.verticalLayout_3.addWidget(self.label)

        self.lbl_by = QLabel(self.centralwidget)
        self.lbl_by.setObjectName(u"lbl_by")
        sizePolicy.setHeightForWidth(self.lbl_by.sizePolicy().hasHeightForWidth())
        self.lbl_by.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamilies([u"Rubik"])
        font.setPointSize(11)
        font.setBold(True)
        self.lbl_by.setFont(font)

        self.verticalLayout_3.addWidget(self.lbl_by)


        self.horizontalLayout_2.addLayout(self.verticalLayout_3)

        self.add_main_btn = QPushButton(self.centralwidget)
        self.add_main_btn.setObjectName(u"add_main_btn")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.add_main_btn.sizePolicy().hasHeightForWidth())
        self.add_main_btn.setSizePolicy(sizePolicy1)
        self.add_main_btn.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_2.addWidget(self.add_main_btn)

        self.del_main_btn = QPushButton(self.centralwidget)
        self.del_main_btn.setObjectName(u"del_main_btn")
        sizePolicy1.setHeightForWidth(self.del_main_btn.sizePolicy().hasHeightForWidth())
        self.del_main_btn.setSizePolicy(sizePolicy1)
        self.del_main_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.del_main_btn.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_2.addWidget(self.del_main_btn)

        self.search_main_btn = QPushButton(self.centralwidget)
        self.search_main_btn.setObjectName(u"search_main_btn")
        sizePolicy1.setHeightForWidth(self.search_main_btn.sizePolicy().hasHeightForWidth())
        self.search_main_btn.setSizePolicy(sizePolicy1)
        self.search_main_btn.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_2.addWidget(self.search_main_btn)

        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy2)
        icon1 = QIcon()
        icon1.addFile(u"icons/all.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QSize(24, 25))

        self.horizontalLayout_2.addWidget(self.pushButton)


        self.verticalLayout_4.addLayout(self.horizontalLayout_2)

        self.tableWidget = QTableWidget(self.centralwidget)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)


        # Применяем стиль для основной таблицы
        table_style = """
                    QTableWidget {
                        gridline-color: gray;
                        background-color: #212121;
                        font-size: 10pt;
                        font-weight: 400;
                    }
                    QTableCornerButton::section {
                        background-color: #4c4c4c;
                    }
                """
        self.tableWidget.setStyleSheet(table_style)
        self.tableWidget.setCornerButtonEnabled(False)

        # Отдельно применяем стиль для секций заголовков
        header_style = """
                    QHeaderView::section {
                        color: white;
                        background-color: #4c4c4c;
                        font-size: 8pt;
                    }
                """


        self.tableWidget.horizontalHeader().setStyleSheet(header_style)
        self.tableWidget.verticalHeader().setStyleSheet(header_style)

        self.tableWidget.verticalHeader().setVisible(True)

        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents)

        self.verticalLayout_4.addWidget(self.tableWidget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Xakaton_IT-cube_ES", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Xakaton for IT-cube", None))
        self.lbl_by.setText(QCoreApplication.translate("MainWindow", u"by Egorcov Stepan", None))
        self.add_main_btn.setText(QCoreApplication.translate("MainWindow", u"\u0434\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
#if QT_CONFIG(shortcut)
        self.add_main_btn.setShortcut(QCoreApplication.translate("MainWindow", u"\\", None))
#endif // QT_CONFIG(shortcut)
        self.del_main_btn.setText(QCoreApplication.translate("MainWindow", u"\u0443\u0434\u0430\u043b\u0438\u0442\u044c", None))
#if QT_CONFIG(shortcut)
        self.del_main_btn.setShortcut(QCoreApplication.translate("MainWindow", u"Del", None))
#endif // QT_CONFIG(shortcut)
        self.search_main_btn.setText(QCoreApplication.translate("MainWindow", u"\u043f\u043e\u0438\u0441\u043a", None))
#if QT_CONFIG(shortcut)
        self.search_main_btn.setShortcut(QCoreApplication.translate("MainWindow", u"End", None))
#endif // QT_CONFIG(shortcut)
        self.pushButton.setText("")
    # retranslateUi