# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Show_Hide_Trades.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Trades_ShowHide(object):
    def setupUi(self, Trades_ShowHide):
        Trades_ShowHide.setObjectName("Trades_ShowHide")
        Trades_ShowHide.setEnabled(True)
        Trades_ShowHide.resize(234, 678)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        Trades_ShowHide.setFont(font)
        Trades_ShowHide.setFocusPolicy(QtCore.Qt.StrongFocus)
        Trades_ShowHide.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        Trades_ShowHide.setStyleSheet("url:/Resources/Combinear.qss")
        Trades_ShowHide.setUnifiedTitleAndToolBarOnMac(True)
        self.centralwidget = QtWidgets.QWidget(Trades_ShowHide)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.btn_colId = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_colId.sizePolicy().hasHeightForWidth())
        self.btn_colId.setSizePolicy(sizePolicy)
        self.btn_colId.setMinimumSize(QtCore.QSize(75, 40))
        self.btn_colId.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_colId.setFont(font)
        self.btn_colId.setToolTip("")
        self.btn_colId.setToolTipDuration(2)
        self.btn_colId.setWhatsThis("")
        self.btn_colId.setAccessibleDescription("")
        self.btn_colId.setAutoFillBackground(False)
        self.btn_colId.setStyleSheet("background-color: rgb(0, 255, 0);")
        self.btn_colId.setCheckable(True)
        self.btn_colId.setAutoDefault(False)
        self.btn_colId.setObjectName("btn_colId")
        self.gridLayout.addWidget(self.btn_colId, 0, 0, 1, 1)
        self.btn_EntryTimeCndl = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_EntryTimeCndl.sizePolicy().hasHeightForWidth())
        self.btn_EntryTimeCndl.setSizePolicy(sizePolicy)
        self.btn_EntryTimeCndl.setMinimumSize(QtCore.QSize(75, 40))
        self.btn_EntryTimeCndl.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_EntryTimeCndl.setFont(font)
        self.btn_EntryTimeCndl.setToolTip("")
        self.btn_EntryTimeCndl.setToolTipDuration(2)
        self.btn_EntryTimeCndl.setWhatsThis("")
        self.btn_EntryTimeCndl.setAccessibleDescription("")
        self.btn_EntryTimeCndl.setAutoFillBackground(False)
        self.btn_EntryTimeCndl.setStyleSheet("background-color: rgb(0, 255, 0);")
        self.btn_EntryTimeCndl.setCheckable(True)
        self.btn_EntryTimeCndl.setAutoDefault(False)
        self.btn_EntryTimeCndl.setObjectName("btn_EntryTimeCndl")
        self.gridLayout.addWidget(self.btn_EntryTimeCndl, 2, 0, 1, 1)
        self.btn_EnrtyTime = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_EnrtyTime.sizePolicy().hasHeightForWidth())
        self.btn_EnrtyTime.setSizePolicy(sizePolicy)
        self.btn_EnrtyTime.setMinimumSize(QtCore.QSize(75, 40))
        self.btn_EnrtyTime.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_EnrtyTime.setFont(font)
        self.btn_EnrtyTime.setToolTip("")
        self.btn_EnrtyTime.setToolTipDuration(2)
        self.btn_EnrtyTime.setWhatsThis("")
        self.btn_EnrtyTime.setAccessibleDescription("")
        self.btn_EnrtyTime.setAutoFillBackground(False)
        self.btn_EnrtyTime.setStyleSheet("background-color: rgb(0, 255, 0);")
        self.btn_EnrtyTime.setCheckable(True)
        self.btn_EnrtyTime.setAutoDefault(False)
        self.btn_EnrtyTime.setObjectName("btn_EnrtyTime")
        self.gridLayout.addWidget(self.btn_EnrtyTime, 1, 0, 1, 1)
        self.btn_LastUpdate = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_LastUpdate.sizePolicy().hasHeightForWidth())
        self.btn_LastUpdate.setSizePolicy(sizePolicy)
        self.btn_LastUpdate.setMinimumSize(QtCore.QSize(75, 40))
        self.btn_LastUpdate.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_LastUpdate.setFont(font)
        self.btn_LastUpdate.setToolTip("")
        self.btn_LastUpdate.setToolTipDuration(2)
        self.btn_LastUpdate.setWhatsThis("")
        self.btn_LastUpdate.setAccessibleDescription("")
        self.btn_LastUpdate.setAutoFillBackground(False)
        self.btn_LastUpdate.setStyleSheet("background-color: rgb(0, 255, 0);")
        self.btn_LastUpdate.setCheckable(True)
        self.btn_LastUpdate.setAutoDefault(False)
        self.btn_LastUpdate.setObjectName("btn_LastUpdate")
        self.gridLayout.addWidget(self.btn_LastUpdate, 3, 0, 1, 1)
        self.btn_Strat = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_Strat.sizePolicy().hasHeightForWidth())
        self.btn_Strat.setSizePolicy(sizePolicy)
        self.btn_Strat.setMinimumSize(QtCore.QSize(75, 40))
        self.btn_Strat.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_Strat.setFont(font)
        self.btn_Strat.setToolTip("")
        self.btn_Strat.setToolTipDuration(2)
        self.btn_Strat.setWhatsThis("")
        self.btn_Strat.setAccessibleDescription("")
        self.btn_Strat.setAutoFillBackground(False)
        self.btn_Strat.setStyleSheet("background-color: rgb(0, 255, 0);")
        self.btn_Strat.setCheckable(True)
        self.btn_Strat.setAutoDefault(False)
        self.btn_Strat.setObjectName("btn_Strat")
        self.gridLayout.addWidget(self.btn_Strat, 5, 0, 1, 1)
        self.btn_Synbol = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_Synbol.sizePolicy().hasHeightForWidth())
        self.btn_Synbol.setSizePolicy(sizePolicy)
        self.btn_Synbol.setMinimumSize(QtCore.QSize(75, 40))
        self.btn_Synbol.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_Synbol.setFont(font)
        self.btn_Synbol.setToolTip("")
        self.btn_Synbol.setToolTipDuration(2)
        self.btn_Synbol.setWhatsThis("")
        self.btn_Synbol.setAccessibleDescription("")
        self.btn_Synbol.setAutoFillBackground(False)
        self.btn_Synbol.setStyleSheet("background-color: rgb(0, 255, 0);")
        self.btn_Synbol.setCheckable(True)
        self.btn_Synbol.setAutoDefault(False)
        self.btn_Synbol.setObjectName("btn_Synbol")
        self.gridLayout.addWidget(self.btn_Synbol, 4, 0, 1, 1)
        self.btn_EntryPrice = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_EntryPrice.sizePolicy().hasHeightForWidth())
        self.btn_EntryPrice.setSizePolicy(sizePolicy)
        self.btn_EntryPrice.setMinimumSize(QtCore.QSize(75, 40))
        self.btn_EntryPrice.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_EntryPrice.setFont(font)
        self.btn_EntryPrice.setToolTip("")
        self.btn_EntryPrice.setToolTipDuration(2)
        self.btn_EntryPrice.setWhatsThis("")
        self.btn_EntryPrice.setAccessibleDescription("")
        self.btn_EntryPrice.setAutoFillBackground(False)
        self.btn_EntryPrice.setStyleSheet("background-color: rgb(0, 255, 0);")
        self.btn_EntryPrice.setCheckable(True)
        self.btn_EntryPrice.setAutoDefault(False)
        self.btn_EntryPrice.setObjectName("btn_EntryPrice")
        self.gridLayout.addWidget(self.btn_EntryPrice, 6, 0, 1, 1)
        self.btn_CurPrice = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_CurPrice.sizePolicy().hasHeightForWidth())
        self.btn_CurPrice.setSizePolicy(sizePolicy)
        self.btn_CurPrice.setMinimumSize(QtCore.QSize(75, 40))
        self.btn_CurPrice.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_CurPrice.setFont(font)
        self.btn_CurPrice.setToolTip("")
        self.btn_CurPrice.setToolTipDuration(2)
        self.btn_CurPrice.setWhatsThis("")
        self.btn_CurPrice.setAccessibleDescription("")
        self.btn_CurPrice.setAutoFillBackground(False)
        self.btn_CurPrice.setStyleSheet("background-color: rgb(0, 255, 0);")
        self.btn_CurPrice.setCheckable(True)
        self.btn_CurPrice.setAutoDefault(False)
        self.btn_CurPrice.setObjectName("btn_CurPrice")
        self.gridLayout.addWidget(self.btn_CurPrice, 7, 0, 1, 1)
        self.btn_TSL = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_TSL.sizePolicy().hasHeightForWidth())
        self.btn_TSL.setSizePolicy(sizePolicy)
        self.btn_TSL.setMinimumSize(QtCore.QSize(75, 40))
        self.btn_TSL.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_TSL.setFont(font)
        self.btn_TSL.setToolTip("")
        self.btn_TSL.setToolTipDuration(2)
        self.btn_TSL.setWhatsThis("")
        self.btn_TSL.setAccessibleDescription("")
        self.btn_TSL.setAutoFillBackground(False)
        self.btn_TSL.setStyleSheet("background-color: rgb(0, 255, 0);")
        self.btn_TSL.setCheckable(True)
        self.btn_TSL.setAutoDefault(False)
        self.btn_TSL.setObjectName("btn_TSL")
        self.gridLayout.addWidget(self.btn_TSL, 9, 0, 1, 1)
        self.btn_TargPrice = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_TargPrice.sizePolicy().hasHeightForWidth())
        self.btn_TargPrice.setSizePolicy(sizePolicy)
        self.btn_TargPrice.setMinimumSize(QtCore.QSize(75, 40))
        self.btn_TargPrice.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_TargPrice.setFont(font)
        self.btn_TargPrice.setToolTip("")
        self.btn_TargPrice.setToolTipDuration(2)
        self.btn_TargPrice.setWhatsThis("")
        self.btn_TargPrice.setAccessibleDescription("")
        self.btn_TargPrice.setAutoFillBackground(False)
        self.btn_TargPrice.setStyleSheet("background-color: rgb(0, 255, 0);")
        self.btn_TargPrice.setCheckable(True)
        self.btn_TargPrice.setAutoDefault(False)
        self.btn_TargPrice.setObjectName("btn_TargPrice")
        self.gridLayout.addWidget(self.btn_TargPrice, 8, 0, 1, 1)
        self.btn_QuoteAmt = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_QuoteAmt.sizePolicy().hasHeightForWidth())
        self.btn_QuoteAmt.setSizePolicy(sizePolicy)
        self.btn_QuoteAmt.setMinimumSize(QtCore.QSize(75, 40))
        self.btn_QuoteAmt.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_QuoteAmt.setFont(font)
        self.btn_QuoteAmt.setToolTip("")
        self.btn_QuoteAmt.setToolTipDuration(2)
        self.btn_QuoteAmt.setWhatsThis("")
        self.btn_QuoteAmt.setAccessibleDescription("")
        self.btn_QuoteAmt.setAutoFillBackground(False)
        self.btn_QuoteAmt.setStyleSheet("background-color: rgb(0, 255, 0);")
        self.btn_QuoteAmt.setCheckable(True)
        self.btn_QuoteAmt.setAutoDefault(False)
        self.btn_QuoteAmt.setObjectName("btn_QuoteAmt")
        self.gridLayout.addWidget(self.btn_QuoteAmt, 11, 0, 1, 1)
        self.btn_BaseAmt = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_BaseAmt.sizePolicy().hasHeightForWidth())
        self.btn_BaseAmt.setSizePolicy(sizePolicy)
        self.btn_BaseAmt.setMinimumSize(QtCore.QSize(75, 40))
        self.btn_BaseAmt.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_BaseAmt.setFont(font)
        self.btn_BaseAmt.setToolTip("")
        self.btn_BaseAmt.setToolTipDuration(2)
        self.btn_BaseAmt.setWhatsThis("")
        self.btn_BaseAmt.setAccessibleDescription("")
        self.btn_BaseAmt.setAutoFillBackground(False)
        self.btn_BaseAmt.setStyleSheet("background-color: rgb(0, 255, 0);")
        self.btn_BaseAmt.setCheckable(True)
        self.btn_BaseAmt.setAutoDefault(False)
        self.btn_BaseAmt.setObjectName("btn_BaseAmt")
        self.gridLayout.addWidget(self.btn_BaseAmt, 10, 0, 1, 1)
        self.btn_PL = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_PL.sizePolicy().hasHeightForWidth())
        self.btn_PL.setSizePolicy(sizePolicy)
        self.btn_PL.setMinimumSize(QtCore.QSize(75, 40))
        self.btn_PL.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_PL.setFont(font)
        self.btn_PL.setToolTip("")
        self.btn_PL.setToolTipDuration(2)
        self.btn_PL.setWhatsThis("")
        self.btn_PL.setAccessibleDescription("")
        self.btn_PL.setAutoFillBackground(False)
        self.btn_PL.setStyleSheet("background-color: rgb(0, 255, 0);")
        self.btn_PL.setCheckable(True)
        self.btn_PL.setAutoDefault(False)
        self.btn_PL.setObjectName("btn_PL")
        self.gridLayout.addWidget(self.btn_PL, 12, 0, 1, 1)
        self.btn_PLpercent = QtWidgets.QPushButton(self.centralwidget)
        self.btn_PLpercent.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_PLpercent.sizePolicy().hasHeightForWidth())
        self.btn_PLpercent.setSizePolicy(sizePolicy)
        self.btn_PLpercent.setMinimumSize(QtCore.QSize(75, 40))
        self.btn_PLpercent.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_PLpercent.setFont(font)
        self.btn_PLpercent.setToolTip("")
        self.btn_PLpercent.setToolTipDuration(2)
        self.btn_PLpercent.setWhatsThis("")
        self.btn_PLpercent.setAccessibleDescription("")
        self.btn_PLpercent.setAutoFillBackground(False)
        self.btn_PLpercent.setStyleSheet("background-color: rgb(0, 255, 0);")
        self.btn_PLpercent.setCheckable(True)
        self.btn_PLpercent.setAutoDefault(False)
        self.btn_PLpercent.setObjectName("btn_PLpercent")
        self.gridLayout.addWidget(self.btn_PLpercent, 13, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        Trades_ShowHide.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Trades_ShowHide)
        self.statusbar.setObjectName("statusbar")
        Trades_ShowHide.setStatusBar(self.statusbar)

        self.retranslateUi(Trades_ShowHide)
        QtCore.QMetaObject.connectSlotsByName(Trades_ShowHide)
        Trades_ShowHide.setTabOrder(self.btn_colId, self.btn_EnrtyTime)
        Trades_ShowHide.setTabOrder(self.btn_EnrtyTime, self.btn_EntryTimeCndl)
        Trades_ShowHide.setTabOrder(self.btn_EntryTimeCndl, self.btn_LastUpdate)
        Trades_ShowHide.setTabOrder(self.btn_LastUpdate, self.btn_Synbol)
        Trades_ShowHide.setTabOrder(self.btn_Synbol, self.btn_Strat)
        Trades_ShowHide.setTabOrder(self.btn_Strat, self.btn_EntryPrice)
        Trades_ShowHide.setTabOrder(self.btn_EntryPrice, self.btn_CurPrice)
        Trades_ShowHide.setTabOrder(self.btn_CurPrice, self.btn_TargPrice)
        Trades_ShowHide.setTabOrder(self.btn_TargPrice, self.btn_TSL)
        Trades_ShowHide.setTabOrder(self.btn_TSL, self.btn_BaseAmt)
        Trades_ShowHide.setTabOrder(self.btn_BaseAmt, self.btn_QuoteAmt)
        Trades_ShowHide.setTabOrder(self.btn_QuoteAmt, self.btn_PL)
        Trades_ShowHide.setTabOrder(self.btn_PL, self.btn_PLpercent)

    def retranslateUi(self, Trades_ShowHide):
        _translate = QtCore.QCoreApplication.translate
        Trades_ShowHide.setWindowTitle(_translate("Trades_ShowHide", "Show/Hide Columns"))
        Trades_ShowHide.setWindowFilePath(_translate("Trades_ShowHide", "url:/Resources/Combinear.qss"))
        self.btn_colId.setText(_translate("Trades_ShowHide", "Id"))
        self.btn_EntryTimeCndl.setText(_translate("Trades_ShowHide", "Entry Time\n"
"Candle"))
        self.btn_EnrtyTime.setText(_translate("Trades_ShowHide", "Entry Time"))
        self.btn_LastUpdate.setText(_translate("Trades_ShowHide", "Last\n"
"Update"))
        self.btn_Strat.setText(_translate("Trades_ShowHide", "Strategy"))
        self.btn_Synbol.setText(_translate("Trades_ShowHide", "Symbol"))
        self.btn_EntryPrice.setText(_translate("Trades_ShowHide", "Entry\n"
"Price"))
        self.btn_CurPrice.setText(_translate("Trades_ShowHide", "Current\n"
"Price"))
        self.btn_TSL.setText(_translate("Trades_ShowHide", "TSL"))
        self.btn_TargPrice.setText(_translate("Trades_ShowHide", "Target\n"
"Price"))
        self.btn_QuoteAmt.setText(_translate("Trades_ShowHide", "Quote\n"
"Amount"))
        self.btn_BaseAmt.setText(_translate("Trades_ShowHide", "Base\n"
"Amount"))
        self.btn_PL.setText(_translate("Trades_ShowHide", "PL"))
        self.btn_PLpercent.setText(_translate("Trades_ShowHide", "PL%"))
import Combinear.qss_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Trades_ShowHide = QtWidgets.QMainWindow()
    ui = Ui_Trades_ShowHide()
    ui.setupUi(Trades_ShowHide)
    Trades_ShowHide.show()
    sys.exit(app.exec_())
