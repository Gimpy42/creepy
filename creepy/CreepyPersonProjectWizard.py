# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'personProjectWizard.ui'
#
# Created: Mon Jan 28 20:52:41 2013
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_personProjectWizard(object):
    def setupUi(self, personProjectWizard):
        personProjectWizard.setObjectName(_fromUtf8("personProjectWizard"))
        personProjectWizard.resize(879, 658)
        self.personProjecWizardPage1 = QtGui.QWizardPage()
        self.personProjecWizardPage1.setObjectName(_fromUtf8("personProjecWizardPage1"))
        self.gridLayoutWidget = QtGui.QWidget(self.personProjecWizardPage1)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 861, 591))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.gridLayout_3 = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout_3.setMargin(0)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.personProjectDescriptionValue = QtGui.QPlainTextEdit(self.gridLayoutWidget)
        self.personProjectDescriptionValue.setObjectName(_fromUtf8("personProjectDescriptionValue"))
        self.gridLayout_3.addWidget(self.personProjectDescriptionValue, 2, 1, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem, 3, 1, 1, 1)
        self.personProjectNameValue = QtGui.QLineEdit(self.gridLayoutWidget)
        self.personProjectNameValue.setObjectName(_fromUtf8("personProjectNameValue"))
        self.gridLayout_3.addWidget(self.personProjectNameValue, 0, 1, 1, 1)
        self.personProjectNameLabel = QtGui.QLabel(self.gridLayoutWidget)
        self.personProjectNameLabel.setEnabled(True)
        self.personProjectNameLabel.setObjectName(_fromUtf8("personProjectNameLabel"))
        self.gridLayout_3.addWidget(self.personProjectNameLabel, 0, 0, 1, 1)
        self.personProjectKeywordsValue = QtGui.QLineEdit(self.gridLayoutWidget)
        self.personProjectKeywordsValue.setObjectName(_fromUtf8("personProjectKeywordsValue"))
        self.gridLayout_3.addWidget(self.personProjectKeywordsValue, 1, 1, 1, 1)
        self.personProjectDescriptionLabel = QtGui.QLabel(self.gridLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.personProjectDescriptionLabel.sizePolicy().hasHeightForWidth())
        self.personProjectDescriptionLabel.setSizePolicy(sizePolicy)
        self.personProjectDescriptionLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.personProjectDescriptionLabel.setObjectName(_fromUtf8("personProjectDescriptionLabel"))
        self.gridLayout_3.addWidget(self.personProjectDescriptionLabel, 2, 0, 1, 1)
        self.personProkectKeywordsLabel = QtGui.QLabel(self.gridLayoutWidget)
        self.personProkectKeywordsLabel.setObjectName(_fromUtf8("personProkectKeywordsLabel"))
        self.gridLayout_3.addWidget(self.personProkectKeywordsLabel, 1, 0, 1, 1)
        personProjectWizard.addPage(self.personProjecWizardPage1)
        self.newPersonBasedProjecWizardPage2 = QtGui.QWizardPage()
        self.newPersonBasedProjecWizardPage2.setObjectName(_fromUtf8("newPersonBasedProjecWizardPage2"))
        self.gridLayout = QtGui.QGridLayout(self.newPersonBasedProjecWizardPage2)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 3, 2, 1, 1)
        self.personProjectSearchResultsLabel = QtGui.QLabel(self.newPersonBasedProjecWizardPage2)
        self.personProjectSearchResultsLabel.setObjectName(_fromUtf8("personProjectSearchResultsLabel"))
        self.gridLayout.addWidget(self.personProjectSearchResultsLabel, 4, 0, 1, 1)
        self.personProjectAvailablePluginsScrollArea = QtGui.QScrollArea(self.newPersonBasedProjecWizardPage2)
        self.personProjectAvailablePluginsScrollArea.setWidgetResizable(True)
        self.personProjectAvailablePluginsScrollArea.setObjectName(_fromUtf8("personProjectAvailablePluginsScrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 729, 155))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.verticalLayout = QtGui.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.personProjectAvailablePluginsListView = QtGui.QListView(self.scrollAreaWidgetContents)
        self.personProjectAvailablePluginsListView.setObjectName(_fromUtf8("personProjectAvailablePluginsListView"))
        self.verticalLayout.addWidget(self.personProjectAvailablePluginsListView)
        self.personProjectAvailablePluginsScrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.personProjectAvailablePluginsScrollArea, 1, 2, 1, 2)
        self.personProjectSearchForDetailsLabel = QtGui.QLabel(self.newPersonBasedProjecWizardPage2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.personProjectSearchForDetailsLabel.sizePolicy().hasHeightForWidth())
        self.personProjectSearchForDetailsLabel.setSizePolicy(sizePolicy)
        self.personProjectSearchForDetailsLabel.setObjectName(_fromUtf8("personProjectSearchForDetailsLabel"))
        self.gridLayout.addWidget(self.personProjectSearchForDetailsLabel, 0, 3, 1, 1)
        self.personProjectTargetsList = QtGui.QListView(self.newPersonBasedProjecWizardPage2)
        self.personProjectTargetsList.setObjectName(_fromUtf8("personProjectTargetsList"))
        self.gridLayout.addWidget(self.personProjectTargetsList, 7, 2, 1, 2)
        self.personProjectSearchForLabel = QtGui.QLabel(self.newPersonBasedProjecWizardPage2)
        self.personProjectSearchForLabel.setObjectName(_fromUtf8("personProjectSearchForLabel"))
        self.gridLayout.addWidget(self.personProjectSearchForLabel, 0, 0, 1, 2)
        self.personProjectTargetSeperatorLine = QtGui.QFrame(self.newPersonBasedProjecWizardPage2)
        self.personProjectTargetSeperatorLine.setLineWidth(4)
        self.personProjectTargetSeperatorLine.setFrameShape(QtGui.QFrame.HLine)
        self.personProjectTargetSeperatorLine.setFrameShadow(QtGui.QFrame.Sunken)
        self.personProjectTargetSeperatorLine.setObjectName(_fromUtf8("personProjectTargetSeperatorLine"))
        self.gridLayout.addWidget(self.personProjectTargetSeperatorLine, 5, 1, 1, 3)
        self.personProjectSearchInLabel = QtGui.QLabel(self.newPersonBasedProjecWizardPage2)
        self.personProjectSearchInLabel.setObjectName(_fromUtf8("personProjectSearchInLabel"))
        self.gridLayout.addWidget(self.personProjectSearchInLabel, 1, 0, 1, 2)
        self.personProjectSearchForValue = QtGui.QLineEdit(self.newPersonBasedProjecWizardPage2)
        self.personProjectSearchForValue.setObjectName(_fromUtf8("personProjectSearchForValue"))
        self.gridLayout.addWidget(self.personProjectSearchForValue, 0, 2, 1, 1)
        self.personProjectSelectedTargetsLabel = QtGui.QLabel(self.newPersonBasedProjecWizardPage2)
        self.personProjectSelectedTargetsLabel.setObjectName(_fromUtf8("personProjectSelectedTargetsLabel"))
        self.gridLayout.addWidget(self.personProjectSelectedTargetsLabel, 7, 0, 1, 1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.personProjectSearchButton = QtGui.QPushButton(self.newPersonBasedProjecWizardPage2)
        self.personProjectSearchButton.setObjectName(_fromUtf8("personProjectSearchButton"))
        self.horizontalLayout_2.addWidget(self.personProjectSearchButton)
        self.gridLayout.addLayout(self.horizontalLayout_2, 3, 3, 1, 1)
        self.personProjectSearchResultsTable = QtGui.QTableView(self.newPersonBasedProjecWizardPage2)
        self.personProjectSearchResultsTable.setObjectName(_fromUtf8("personProjectSearchResultsTable"))
        self.gridLayout.addWidget(self.personProjectSearchResultsTable, 4, 2, 1, 2)
        personProjectWizard.addPage(self.newPersonBasedProjecWizardPage2)
        self.newPersonBasedProjecWizardPage3 = QtGui.QWizardPage()
        self.newPersonBasedProjecWizardPage3.setObjectName(_fromUtf8("newPersonBasedProjecWizardPage3"))
        self.gridLayout_2 = QtGui.QGridLayout(self.newPersonBasedProjecWizardPage3)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        personProjectWizard.addPage(self.newPersonBasedProjecWizardPage3)

        self.retranslateUi(personProjectWizard)
        QtCore.QMetaObject.connectSlotsByName(personProjectWizard)

    def retranslateUi(self, personProjectWizard):
        personProjectWizard.setWindowTitle(QtGui.QApplication.translate("personProjectWizard", "New Person Project", None, QtGui.QApplication.UnicodeUTF8))
        self.personProjecWizardPage1.setTitle(QtGui.QApplication.translate("personProjectWizard", "Step 1 - Set Project Metadata", None, QtGui.QApplication.UnicodeUTF8))
        self.personProjecWizardPage1.setSubTitle(QtGui.QApplication.translate("personProjectWizard", "Add project related information", None, QtGui.QApplication.UnicodeUTF8))
        self.personProjectNameLabel.setText(QtGui.QApplication.translate("personProjectWizard", "Project Name ", None, QtGui.QApplication.UnicodeUTF8))
        self.personProjectDescriptionLabel.setText(QtGui.QApplication.translate("personProjectWizard", "Description", None, QtGui.QApplication.UnicodeUTF8))
        self.personProkectKeywordsLabel.setText(QtGui.QApplication.translate("personProjectWizard", "Keywords", None, QtGui.QApplication.UnicodeUTF8))
        self.newPersonBasedProjecWizardPage2.setTitle(QtGui.QApplication.translate("personProjectWizard", "Step 1 - Set the target", None, QtGui.QApplication.UnicodeUTF8))
        self.newPersonBasedProjecWizardPage2.setSubTitle(QtGui.QApplication.translate("personProjectWizard", "Search for the person you want to track using the available plugins and add it to the selected targets", None, QtGui.QApplication.UnicodeUTF8))
        self.personProjectSearchResultsLabel.setText(QtGui.QApplication.translate("personProjectWizard", "Search Results ", None, QtGui.QApplication.UnicodeUTF8))
        self.personProjectSearchForDetailsLabel.setText(QtGui.QApplication.translate("personProjectWizard", "Search by username, mail, full name, id", None, QtGui.QApplication.UnicodeUTF8))
        self.personProjectSearchForLabel.setText(QtGui.QApplication.translate("personProjectWizard", "Search for", None, QtGui.QApplication.UnicodeUTF8))
        self.personProjectSearchInLabel.setText(QtGui.QApplication.translate("personProjectWizard", "Search In", None, QtGui.QApplication.UnicodeUTF8))
        self.personProjectSelectedTargetsLabel.setText(QtGui.QApplication.translate("personProjectWizard", "Selected Targets", None, QtGui.QApplication.UnicodeUTF8))
        self.personProjectSearchButton.setText(QtGui.QApplication.translate("personProjectWizard", "Search", None, QtGui.QApplication.UnicodeUTF8))
        self.newPersonBasedProjecWizardPage3.setTitle(QtGui.QApplication.translate("personProjectWizard", "Configure the Search Parameters", None, QtGui.QApplication.UnicodeUTF8))

