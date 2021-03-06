# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Trade_Settings_v1.7.2.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_TradeSet(object):
    def setupUi(self, TradeSet):
        TradeSet.setObjectName("TradeSet")
        TradeSet.resize(404, 204)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        TradeSet.setFont(font)
        TradeSet.setMouseTracking(False)
        TradeSet.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(TradeSet)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.groupBox_6 = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_6.sizePolicy().hasHeightForWidth())
        self.groupBox_6.setSizePolicy(sizePolicy)
        self.groupBox_6.setMinimumSize(QtCore.QSize(50, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.groupBox_6.setFont(font)
        self.groupBox_6.setStyleSheet("")
        self.groupBox_6.setObjectName("groupBox_6")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_6)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.rebuyTimeInSecondsLabel = QtWidgets.QLabel(self.groupBox_6)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.rebuyTimeInSecondsLabel.setFont(font)
        self.rebuyTimeInSecondsLabel.setStyleSheet("")
        self.rebuyTimeInSecondsLabel.setObjectName("rebuyTimeInSecondsLabel")
        self.gridLayout.addWidget(self.rebuyTimeInSecondsLabel, 0, 0, 1, 1)
        self.txtRebuyTimeInSeconds = QtWidgets.QLineEdit(self.groupBox_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtRebuyTimeInSeconds.sizePolicy().hasHeightForWidth())
        self.txtRebuyTimeInSeconds.setSizePolicy(sizePolicy)
        self.txtRebuyTimeInSeconds.setMinimumSize(QtCore.QSize(0, 30))
        self.txtRebuyTimeInSeconds.setStyleSheet("")
        self.txtRebuyTimeInSeconds.setObjectName("txtRebuyTimeInSeconds")
        self.gridLayout.addWidget(self.txtRebuyTimeInSeconds, 0, 1, 1, 1)
        self.lblRebuyPercentage = QtWidgets.QLabel(self.groupBox_6)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lblRebuyPercentage.setFont(font)
        self.lblRebuyPercentage.setStyleSheet("")
        self.lblRebuyPercentage.setObjectName("lblRebuyPercentage")
        self.gridLayout.addWidget(self.lblRebuyPercentage, 1, 0, 1, 1)
        self.txtRebuyPercentage = QtWidgets.QLineEdit(self.groupBox_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtRebuyPercentage.sizePolicy().hasHeightForWidth())
        self.txtRebuyPercentage.setSizePolicy(sizePolicy)
        self.txtRebuyPercentage.setMinimumSize(QtCore.QSize(0, 30))
        self.txtRebuyPercentage.setStyleSheet("")
        self.txtRebuyPercentage.setObjectName("txtRebuyPercentage")
        self.gridLayout.addWidget(self.txtRebuyPercentage, 1, 1, 1, 1)
        self.lblRebuyMaxLimit = QtWidgets.QLabel(self.groupBox_6)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lblRebuyMaxLimit.setFont(font)
        self.lblRebuyMaxLimit.setStyleSheet("")
        self.lblRebuyMaxLimit.setObjectName("lblRebuyMaxLimit")
        self.gridLayout.addWidget(self.lblRebuyMaxLimit, 2, 0, 1, 1)
        self.txtRebuyMaxLimit = QtWidgets.QLineEdit(self.groupBox_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtRebuyMaxLimit.sizePolicy().hasHeightForWidth())
        self.txtRebuyMaxLimit.setSizePolicy(sizePolicy)
        self.txtRebuyMaxLimit.setMinimumSize(QtCore.QSize(0, 30))
        self.txtRebuyMaxLimit.setStyleSheet("")
        self.txtRebuyMaxLimit.setObjectName("txtRebuyMaxLimit")
        self.gridLayout.addWidget(self.txtRebuyMaxLimit, 2, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.gridLayout_3.addWidget(self.groupBox_6, 0, 0, 1, 1)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.btnSaveTradeParameters = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnSaveTradeParameters.sizePolicy().hasHeightForWidth())
        self.btnSaveTradeParameters.setSizePolicy(sizePolicy)
        self.btnSaveTradeParameters.setMinimumSize(QtCore.QSize(0, 40))
        self.btnSaveTradeParameters.setMaximumSize(QtCore.QSize(160, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btnSaveTradeParameters.setFont(font)
        self.btnSaveTradeParameters.setStyleSheet("")
        self.btnSaveTradeParameters.setObjectName("btnSaveTradeParameters")
        self.verticalLayout_4.addWidget(self.btnSaveTradeParameters)
        self.btnStartOptimizationLoop_TradePar = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnStartOptimizationLoop_TradePar.sizePolicy().hasHeightForWidth())
        self.btnStartOptimizationLoop_TradePar.setSizePolicy(sizePolicy)
        self.btnStartOptimizationLoop_TradePar.setMinimumSize(QtCore.QSize(0, 40))
        self.btnStartOptimizationLoop_TradePar.setMaximumSize(QtCore.QSize(160, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btnStartOptimizationLoop_TradePar.setFont(font)
        self.btnStartOptimizationLoop_TradePar.setStyleSheet("")
        self.btnStartOptimizationLoop_TradePar.setObjectName("btnStartOptimizationLoop_TradePar")
        self.verticalLayout_4.addWidget(self.btnStartOptimizationLoop_TradePar)
        self.btnStartOptimization_TradePar = QtWidgets.QPushButton(self.centralwidget)
        self.btnStartOptimization_TradePar.setMinimumSize(QtCore.QSize(0, 40))
        self.btnStartOptimization_TradePar.setMaximumSize(QtCore.QSize(160, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btnStartOptimization_TradePar.setFont(font)
        self.btnStartOptimization_TradePar.setStyleSheet("")
        self.btnStartOptimization_TradePar.setObjectName("btnStartOptimization_TradePar")
        self.verticalLayout_4.addWidget(self.btnStartOptimization_TradePar)
        self.gridLayout_3.addLayout(self.verticalLayout_4, 0, 1, 1, 1)
        TradeSet.setCentralWidget(self.centralwidget)
        self.actionBot_Parameters = QtWidgets.QAction(TradeSet)
        self.actionBot_Parameters.setObjectName("actionBot_Parameters")

        self.retranslateUi(TradeSet)
        QtCore.QMetaObject.connectSlotsByName(TradeSet)

    def retranslateUi(self, TradeSet):
        _translate = QtCore.QCoreApplication.translate
        TradeSet.setWindowTitle(_translate("TradeSet", "SwT"))
        self.groupBox_6.setTitle(_translate("TradeSet", "Trade Parameters"))
        self.rebuyTimeInSecondsLabel.setText(_translate("TradeSet", "Rebuy Wait Time (s)"))
        self.lblRebuyPercentage.setText(_translate("TradeSet", "Rebuy CP > SP (%)"))
        self.lblRebuyMaxLimit.setText(_translate("TradeSet", "Maximum Rebuys"))
        self.btnSaveTradeParameters.setText(_translate("TradeSet", "Save"))
        self.btnStartOptimizationLoop_TradePar.setText(_translate("TradeSet", "Start Opti. Loop"))
        self.btnStartOptimization_TradePar.setText(_translate("TradeSet", "Start Optimization"))
        self.actionBot_Parameters.setText(_translate("TradeSet", "Bot Parameters"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    TradeSet = QtWidgets.QMainWindow()
    ui = Ui_TradeSet()
    ui.setupUi(TradeSet)
    TradeSet.show()
    sys.exit(app.exec_())
