# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add.ui'
##
## Created by: Qt User Interface Compiler version 6.6.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(700, 300)
        icon = QIcon()
        icon.addFile(u"icons/add.png", QSize(), QIcon.Normal,
                     QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setStyleSheet(u"QWidget {\n"
"	color: white;\n"
"	background-color: #212121;\n"
"	font-family: Rubik;\n"
"	font-size: 11pt;\n"
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
"}")
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.SFIO = QLineEdit(Form)
        self.SFIO.setObjectName(u"SFIO")

        self.horizontalLayout.addWidget(self.SFIO)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.SDOB = QLineEdit(Form)
        self.SDOB.setObjectName(u"SDOB")

        self.horizontalLayout_2.addWidget(self.SDOB)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_3.addWidget(self.label_3)

        self.SS = QLineEdit(Form)
        self.SS.setObjectName(u"SS")

        self.horizontalLayout_3.addWidget(self.SS)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_4.addWidget(self.label_4)

        self.SA = QLineEdit(Form)
        self.SA.setObjectName(u"SA")

        self.horizontalLayout_4.addWidget(self.SA)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.lbl12 = QLabel(Form)
        self.lbl12.setObjectName(u"lbl12")

        self.horizontalLayout_5.addWidget(self.lbl12)

        self.PFIO = QLineEdit(Form)
        self.PFIO.setObjectName(u"PFIO")

        self.horizontalLayout_5.addWidget(self.PFIO)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.lblb = QLabel(Form)
        self.lblb.setObjectName(u"lblb")

        self.horizontalLayout_6.addWidget(self.lblb)

        self.PPN = QLineEdit(Form)
        self.PPN.setObjectName(u"PPN")

        self.horizontalLayout_6.addWidget(self.PPN)


        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_7 = QLabel(Form)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_7.addWidget(self.label_7)

        self.PEM = QLineEdit(Form)
        self.PEM.setObjectName(u"PEM")

        self.horizontalLayout_7.addWidget(self.PEM)


        self.verticalLayout.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_5 = QLabel(Form)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_8.addWidget(self.label_5)

        self.checkBox = QCheckBox(Form)
        self.checkBox.setObjectName(u"checkBox")

        self.horizontalLayout_8.addWidget(self.checkBox)


        self.verticalLayout.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.add_btn = QPushButton(Form)
        self.add_btn.setObjectName(u"add_btn")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.add_btn.sizePolicy().hasHeightForWidth())
        self.add_btn.setSizePolicy(sizePolicy)

        self.horizontalLayout_9.addWidget(self.add_btn)

        self.generate_btn = QPushButton(Form)
        self.generate_btn.setObjectName(u"generate_btn")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.generate_btn.sizePolicy().hasHeightForWidth())
        self.generate_btn.setSizePolicy(sizePolicy1)
        icon = QIcon()
        icon.addFile(u"icons/generate.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.generate_btn.setIcon(icon)
        self.generate_btn.setIconSize(QSize(32, 32))

        self.horizontalLayout_9.addWidget(self.generate_btn)


        self.verticalLayout.addLayout(self.horizontalLayout_9)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Добавить", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u0424\u0418\u041e \u0443\u0447\u0435\u043d\u0438\u043a\u0430", None))
        self.SFIO.setInputMask("")
        self.SFIO.setPlaceholderText(QCoreApplication.translate("Form", u"\u041d\u0430\u043f\u0440\u0438\u043c\u0435\u0440, \u0418\u0432\u0430\u043d\u043e\u0432 \u0418\u043d\u0432\u0430\u043d \u0418\u0432\u0430\u043d\u043e\u0432\u0438\u0447", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u0414\u0430\u0442\u0430 \u0440\u043e\u0436\u0434\u0435\u043d\u0438\u044f \u0443\u0447\u0435\u043d\u0438\u043a\u0430", None))
        self.SDOB.setPlaceholderText(QCoreApplication.translate("Form", u"\u041d\u0430\u043f\u0440\u0438\u043c\u0435\u0440, 11.11.2011", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u041f\u043e\u0441\u0435\u0449\u0430\u0435\u043c\u044b\u0439 \u043a\u0440\u0443\u0436\u043e\u043a", None))
        self.SS.setPlaceholderText(QCoreApplication.translate("Form", u"\u041d\u0430\u043f\u0440\u0438\u043c\u0435\u0440, \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435 ", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"\u0410\u0434\u0440\u0435\u0441 \u043f\u0440\u043e\u0436\u0438\u0432\u0430\u043d\u0438\u044f", None))
        self.SA.setPlaceholderText(QCoreApplication.translate("Form", u"\u041d\u0430\u043f\u0440\u0438\u043c\u0435\u0440, \u0433. \u041c\u043e\u0441\u043a\u0432\u0430, \u0443\u043b. \u041f\u0443\u0448\u043a\u0438\u043d\u0430, \u0434.13", None))
        self.lbl12.setText(QCoreApplication.translate("Form", u"\u0424\u0418\u041e \u0440\u043e\u0434\u0438\u0442\u0435\u043b\u044f", None))
        self.PFIO.setPlaceholderText(QCoreApplication.translate("Form", u"\u041d\u0430\u043f\u0440\u0438\u043c\u0435\u0440, \u0418\u0432\u0430\u043d\u043e\u0432 \u0418\u0432\u0430\u043d \u0418\u0432\u0430\u043d\u043e\u0432\u0438\u0447", None))
        self.lblb.setText(QCoreApplication.translate("Form", u"\u041d\u043e\u043c\u0435\u0440 \u0442\u0435\u043b\u0435\u0444\u043e\u043d\u0430 \u0440\u043e\u0434\u0438\u0442\u0435\u043b\u044f", None))
        self.PPN.setPlaceholderText(QCoreApplication.translate("Form", u"\u041d\u0430\u043f\u0440\u0438\u043c\u0435\u0440, +79998887766", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"E-mail \u0440\u043e\u0434\u0438\u0442\u0435\u043b\u044f", None))
        self.PEM.setPlaceholderText(QCoreApplication.translate("Form", u"\u041d\u0430\u043f\u0440\u0438\u043c\u0435\u0440, examplemail@example.ru", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"\u041c\u043e\u0436\u0435\u0442  \u0434\u043e\u0431\u0438\u0440\u0430\u0442\u044c\u0441\u044f  \u0434\u043e\u043c\u043e\u0439  \u0441\u0430\u043c\u043e\u0441\u0442\u043e\u044f\u0442\u0435\u043b\u044c\u043d\u043e", None))
        self.checkBox.setText("")
        self.add_btn.setText(QCoreApplication.translate("Form", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.generate_btn.setText("")
    # retranslateUi