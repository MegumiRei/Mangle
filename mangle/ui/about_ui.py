# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mangle/dev/ui/about.ui'
#
# Created: Fri Jun 24 14:44:08 2011
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_DialogAbout(object):
    def setupUi(self, DialogAbout):
        DialogAbout.setObjectName(_fromUtf8("DialogAbout"))
        DialogAbout.resize(468, 262)
        self.horizontalLayout = QtGui.QHBoxLayout(DialogAbout)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setSizeConstraint(QtGui.QLayout.SetFixedSize)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(DialogAbout)
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8(":/img/img/banner_about.png")))
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setMargin(9)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.labelReadme = QtGui.QLabel(DialogAbout)
        self.labelReadme.setMinimumSize(QtCore.QSize(350, 0))
        self.labelReadme.setWordWrap(True)
        self.labelReadme.setOpenExternalLinks(True)
        self.labelReadme.setObjectName(_fromUtf8("labelReadme"))
        self.verticalLayout.addWidget(self.labelReadme)
        spacerItem = QtGui.QSpacerItem(0, 0, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.buttonBox = QtGui.QDialogButtonBox(DialogAbout)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonBox.sizePolicy().hasHeightForWidth())
        self.buttonBox.setSizePolicy(sizePolicy)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)
        self.horizontalLayout.addLayout(self.verticalLayout)

        self.retranslateUi(DialogAbout)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), DialogAbout.accept)
        QtCore.QMetaObject.connectSlotsByName(DialogAbout)

    def retranslateUi(self, DialogAbout):
        DialogAbout.setWindowTitle(QtGui.QApplication.translate("DialogAbout", "About", None, QtGui.QApplication.UnicodeUTF8))
        self.labelReadme.setText(QtGui.QApplication.translate("DialogAbout", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans\'; font-size:14pt;\">Mangle</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans\'; font-size:10pt;\">Version 2.4.3</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Sans\'; font-size:10pt;\"></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans\'; font-size:10pt;\">Manga processor by Alex Yatskov for the Kindle e-book reader. Please see </span><span style=\" font-family:\'Sans\'; font-size:10pt; font-style:italic;\">license.txt</span><span style=\" font-family:\'Sans\'; font-size:10pt;\"> for licensing information. Visit the homepage at </span><a href=\"http://foosoft.net/mangle\"><span style=\" font-family:\'Sans\'; font-size:10pt; text-decoration: underline; color:#0000ff;\">http://foosoft.net/mangle</span></a><span style=\" font-family:\'Sans\'; font-size:10pt;\">.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Sans\'; font-size:10pt;\"></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans\'; font-size:10pt;\">For now this program developed by Stanislav (proDOOMman) Kosolapov. Sources avaliable at </span><a href=\"http://github.com/proDOOMman/Mangle\"><span style=\" font-family:\'Sans\'; font-size:10pt; text-decoration: underline; color:#0000ff;\">http://github.com/proDOOMman/Mangle</span></a></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))

import resources_rc
