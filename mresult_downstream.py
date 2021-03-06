# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'result_upstream.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QFont


class Ui_Downstream_Screen_Result(object):
    def setupUi(self, Downstream_Screen):

        Downstream_Screen.setWindowIcon(QtGui.QIcon("unnamed.png"))
        Downstream_Screen.setObjectName("Upstream_Screen")
        Downstream_Screen.resize(691, 492)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Downstream_Screen.sizePolicy().hasHeightForWidth())
        Downstream_Screen.setSizePolicy(sizePolicy)
        Downstream_Screen.setMinimumSize(QtCore.QSize(691, 492))
        Downstream_Screen.setMaximumSize(QtCore.QSize(691, 492))
        self.Background_label = QtWidgets.QLabel(Downstream_Screen)
        self.Background_label.setGeometry(QtCore.QRect(0, 0, 691, 492))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Background_label.sizePolicy().hasHeightForWidth())
        self.Background_label.setSizePolicy(sizePolicy)
        self.Background_label.setMinimumSize(QtCore.QSize(691, 492))
        self.Background_label.setMaximumSize(QtCore.QSize(691, 492))
        self.Background_label.setText("")
        self.Background_label.setPixmap(QtGui.QPixmap("pic3.jpg"))
        self.Background_label.setScaledContents(True)
        self.Background_label.setWordWrap(True)
        self.Background_label.setObjectName("Background_label")
        self.Topic_label = QtWidgets.QLabel(Downstream_Screen)
        self.Topic_label.setGeometry(QtCore.QRect(75, 0, 600, 91))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(21)
        font.setBold(True)
        font.setWeight(75)
        self.Topic_label.setFont(font)
        self.Topic_label.setObjectName("Topic_label")
        self.input_label1 = QtWidgets.QLabel(Downstream_Screen)
        self.input_label1.setGeometry(QtCore.QRect(360, 108, 450, 35))
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.input_label1.setFont(font)
        self.input_label1.setObjectName("input_label1")
        self.input_label2 = QtWidgets.QLabel(Downstream_Screen)
        self.input_label2.setGeometry(QtCore.QRect(285, 140, 450, 35))
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.input_label2.setFont(font)
        self.input_label2.setObjectName("input_label2")
        self.input_label5 = QtWidgets.QLabel(Downstream_Screen)
        self.input_label5.setGeometry(QtCore.QRect(102, 207, 450, 35))
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.input_label5.setFont(font)
        self.input_label5.setObjectName("input_label5")
        self.input_label4 = QtWidgets.QLabel(Downstream_Screen)
        self.input_label4.setGeometry(QtCore.QRect(353, 240, 450, 35))
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.input_label4.setFont(font)
        self.input_label4.setObjectName("input_label4")
        self.input_label6 = QtWidgets.QLabel(Downstream_Screen)
        self.input_label6.setGeometry(QtCore.QRect(48, 290, 450, 35))  ###
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.input_label6.setFont(font)
        self.input_label6.setObjectName("input_label6")
        self.input_label7 = QtWidgets.QLabel(Downstream_Screen)
        self.input_label7.setGeometry(QtCore.QRect(38, 323, 450, 35))  ####
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.input_label7.setFont(font)
        self.input_label7.setObjectName("input_label7")
        self.input_label3 = QtWidgets.QLabel(Downstream_Screen)
        self.input_label3.setGeometry(QtCore.QRect(29, 178, 450, 35))
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.input_label3.setFont(font)
        self.input_label3.setObjectName("input_label3")
        self.input_label8 = QtWidgets.QLabel(Downstream_Screen)
        self.input_label8.setGeometry(QtCore.QRect(213, 375, 450, 35))
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.input_label8.setFont(font)
        self.input_label8.setObjectName("input_label8")
        self.lineEdit_1 = QtWidgets.QLabel(Downstream_Screen)
        self.lineEdit_1.setGeometry(QtCore.QRect(470, 113, 165, 25))
        self.lineEdit_1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lineEdit_1.setStyleSheet("background-color: white")
        #self.lineEdit_1.setInputMask("")
        #self.lineEdit_1.setFrame(True)
        self.lineEdit_1.setObjectName("lineEdit_1")
        self.lineEdit_2 = QtWidgets.QLabel(Downstream_Screen)
        self.lineEdit_2.setGeometry(QtCore.QRect(470, 145, 165, 25))
        self.lineEdit_2.setStyleSheet("background-color: white")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLabel(Downstream_Screen)
        self.lineEdit_3.setGeometry(QtCore.QRect(470, 179, 165, 25))
        self.lineEdit_3.setStyleSheet("background-color: white")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLabel(Downstream_Screen)
        self.lineEdit_4.setGeometry(QtCore.QRect(470, 211, 165, 25))
        self.lineEdit_4.setStyleSheet("background-color: white")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLabel(Downstream_Screen)
        self.lineEdit_5.setGeometry(QtCore.QRect(470, 295, 165, 25))
        self.lineEdit_5.setStyleSheet("background-color: white")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLabel(Downstream_Screen)
        self.lineEdit_6.setGeometry(QtCore.QRect(470, 243, 165, 25))
        self.lineEdit_6.setStyleSheet("background-color: white")
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_8 = QtWidgets.QLabel(Downstream_Screen)
        self.lineEdit_8.setGeometry(QtCore.QRect(470, 379, 165, 25))
        self.lineEdit_8.setStyleSheet("background-color: white")
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.lineEdit_7 = QtWidgets.QLabel(Downstream_Screen)
        self.lineEdit_7.setGeometry(QtCore.QRect(470, 326, 165, 25))
        self.lineEdit_7.setStyleSheet("background-color: white")
        self.lineEdit_7.setObjectName("lineEdit_7")

        self.retranslateUi(Downstream_Screen)
        QtCore.QMetaObject.connectSlotsByName(Downstream_Screen)

    def retranslateUi(self, Downstream_Screen):
        _translate = QtCore.QCoreApplication.translate
        Downstream_Screen.setWindowTitle(_translate("Upstream_Screen", "Choke Pressure Estimator - Downstream Results"))
        self.Topic_label.setText(_translate("Upstream_Screen", "Results for Downstream Pressure Calculation"))
        self.input_label1.setText(_translate("Upstream_Screen", "Choke Area :"))
        self.input_label2.setText(_translate("Upstream_Screen", "Critical Pressure Ratio :"))
        self.input_label5.setText(_translate("Upstream_Screen", "Flow Rate at the minimum sonic flow condition :"))
        self.input_label4.setText(_translate("Upstream_Screen", "Flow Regime :"))
        self.input_label6.setText(_translate("Upstream_Screen", "Maximum possible Downstream Pressure in sonic flow :"))
        self.input_label7.setText(_translate("Upstream_Screen", " Downstream Pressure given by sub-sonic flow equation :"))
        self.input_label3.setText(_translate("Upstream_Screen", "Maximum Downstream Pressure for minimum sonic flow :"))
        self.input_label8.setText(_translate("Upstream_Screen", "Estimated Downstream Pressure :"))
        self.lineEdit_2.setFont(QFont("Times New Roman", 12, weight=QFont.Bold))
        self.lineEdit_1.setFont(QFont("Times New Roman", 12, weight=QFont.Bold))
        self.lineEdit_3.setFont(QFont("Times New Roman", 12, weight=QFont.Bold))
        self.lineEdit_4.setFont(QFont("Times New Roman", 12, weight=QFont.Bold))
        self.lineEdit_5.setFont(QFont("Times New Roman", 12, weight=QFont.Bold))
        self.lineEdit_8.setFont(QFont("Times New Roman", 12, weight=QFont.Bold))
        self.lineEdit_6.setFont(QFont("Times New Roman", 12, weight=QFont.Bold))
        self.lineEdit_7.setFont(QFont("Times New Roman", 12, weight=QFont.Bold))





if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Downstream_Screen = QtWidgets.QWidget()
    ui = Ui_Downstream_Screen_Result()
    ui.setupUi(Downstream_Screen)
    Downstream_Screen.show()
    sys.exit(app.exec_())
