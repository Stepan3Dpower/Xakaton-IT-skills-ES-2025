# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'search.ui'
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
        Form.resize(600, 200)
        icon = QIcon()
        icon.addFile(u"icons/search.png", QSize(), QIcon.Normal,
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
        self.FN_CHB = QCheckBox(Form)
        self.FN_CHB.setObjectName(u"FN_CHB")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.FN_CHB.sizePolicy().hasHeightForWidth())
        self.FN_CHB.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.FN_CHB)

        self.label = QLabel(Form)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.FN_INP = QLineEdit(Form)
        self.FN_INP.setObjectName(u"FN_INP")

        self.horizontalLayout.addWidget(self.FN_INP)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.LN_CHB = QCheckBox(Form)
        self.LN_CHB.setObjectName(u"LN_CHB")
        sizePolicy.setHeightForWidth(self.LN_CHB.sizePolicy().hasHeightForWidth())
        self.LN_CHB.setSizePolicy(sizePolicy)

        self.horizontalLayout_2.addWidget(self.LN_CHB)

        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.LN_INP = QLineEdit(Form)
        self.LN_INP.setObjectName(u"LN_INP")

        self.horizontalLayout_2.addWidget(self.LN_INP)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.F_CHB = QCheckBox(Form)
        self.F_CHB.setObjectName(u"F_CHB")
        sizePolicy.setHeightForWidth(self.F_CHB.sizePolicy().hasHeightForWidth())
        self.F_CHB.setSizePolicy(sizePolicy)

        self.horizontalLayout_3.addWidget(self.F_CHB)

        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_3.addWidget(self.label_3)

        self.F_INP = QLineEdit(Form)
        self.F_INP.setObjectName(u"F_INP")

        self.horizontalLayout_3.addWidget(self.F_INP)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.SEC_CHB = QCheckBox(Form)
        self.SEC_CHB.setObjectName(u"SEC_CHB")
        sizePolicy.setHeightForWidth(self.SEC_CHB.sizePolicy().hasHeightForWidth())
        self.SEC_CHB.setSizePolicy(sizePolicy)

        self.horizontalLayout_6.addWidget(self.SEC_CHB)

        self.label_6 = QLabel(Form)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_6.addWidget(self.label_6)

        self.SEC_INP = QLineEdit(Form)
        self.SEC_INP.setObjectName(u"SEC_INP")

        self.horizontalLayout_6.addWidget(self.SEC_INP)


        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.PN_CHB = QCheckBox(Form)
        self.PN_CHB.setObjectName(u"PN_CHB")
        sizePolicy.setHeightForWidth(self.PN_CHB.sizePolicy().hasHeightForWidth())
        self.PN_CHB.setSizePolicy(sizePolicy)

        self.horizontalLayout_7.addWidget(self.PN_CHB)

        self.label_7 = QLabel(Form)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_7.addWidget(self.label_7)

        self.PN_INP = QLineEdit(Form)
        self.PN_INP.setObjectName(u"PN_INP")

        self.horizontalLayout_7.addWidget(self.PN_INP)


        self.verticalLayout.addLayout(self.horizontalLayout_7)

        self.Search_btn = QPushButton(Form)
        self.Search_btn.setObjectName(u"Search_btn")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.Search_btn.sizePolicy().hasHeightForWidth())
        self.Search_btn.setSizePolicy(sizePolicy1)

        self.verticalLayout.addWidget(self.Search_btn)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u041d\u0430\u0439\u0442\u0438", None))
        self.FN_CHB.setText("")
        self.label.setText(QCoreApplication.translate("Form", u"\u0424\u0430\u043c\u0438\u043b\u0438\u044f", None))
        self.FN_INP.setPlaceholderText(QCoreApplication.translate("Form", u"\u041d\u0430\u043f\u0440\u0438\u043c\u0435\u0440, \u0418\u0432\u0430\u043d\u043e\u0432", None))
        self.LN_CHB.setText("")
        self.label_2.setText(QCoreApplication.translate("Form", u"\u0418\u043c\u044f", None))
        self.LN_INP.setPlaceholderText(QCoreApplication.translate("Form", u"\u041d\u0430\u043f\u0440\u0438\u043c\u0435\u0440, \u0418\u0432\u0430\u043d", None))
        self.F_CHB.setText("")
        self.label_3.setText(QCoreApplication.translate("Form", u"\u041e\u0442\u0447\u0435\u0441\u0442\u0432\u043e", None))
        self.F_INP.setPlaceholderText(QCoreApplication.translate("Form", u"\u041d\u0430\u043f\u0440\u0438\u043c\u0435\u0440, \u0418\u0432\u0430\u043d\u043e\u0432\u0438\u0447", None))
        self.SEC_CHB.setText("")
        self.label_6.setText(QCoreApplication.translate("Form", u"\u041a\u0440\u0443\u0436\u043e\u043a", None))
        self.SEC_INP.setPlaceholderText(QCoreApplication.translate("Form", u"\u041d\u0430\u043f\u0440\u0438\u043c\u0435\u0440, \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435", None))
        self.PN_CHB.setText("")
        self.label_7.setText(QCoreApplication.translate("Form", u"\u041d\u043e\u043c\u0435\u0440 \u0442\u0435\u043b\u0435\u0444\u043e\u043d\u0430", None))
        self.PN_INP.setPlaceholderText(QCoreApplication.translate("Form", u"\u041d\u0430\u043f\u0440\u0438\u043c\u0435\u0440, +79998887766", None))
        self.Search_btn.setText(QCoreApplication.translate("Form", u"\u041d\u0430\u0439\u0442\u0438", None))
#if QT_CONFIG(shortcut)
        self.Search_btn.setShortcut(QCoreApplication.translate("Form", u"End", None))
#endif // QT_CONFIG(shortcut)
    # retranslateUi

