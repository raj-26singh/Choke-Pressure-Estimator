# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'upstream.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QCursor
from mresult_downstream import Ui_Downstream_Screen_Result
from math import sqrt
from decimal import Decimal
from scipy.optimize import fsolve


class Ui_Downstream_Screen(object):

    def _screen23(self):
        self.screen22 = QtWidgets.QMainWindow()
        self.up = Ui_Downstream_Screen_Result()
        self.up.setupUi(self.screen22)
        C7 = float(self.lineEdit_1.text())
        C8 = float(self.lineEdit_2.text())
        C9 = float(self.lineEdit_3.text())
        C10 = float(self.lineEdit_4.text())
        C12 = float(self.lineEdit_5.text())
        C11 = float(self.lineEdit_6.text())
        C14 = float(self.lineEdit_7.text())
        C13 = float(self.lineEdit_8.text())

        C18 = (3.14 / 4) * (C8 / 64) ** 2
        C19 = (2 / (C12 + 1)) ** (C12 / (C12 - 1))
        C20 = C7 * C19
        C21 = 879.0 * C14 * C18 * C7 * sqrt(C12 / C11 / (C13 + 460) * (2 / (C12 + 1)) ** ((C12 + 1) / (C12 - 1)))
        C22 = (C10 - C21) / abs(C10 - C21)
        C24 = C7 * C19

        def g(y):
            return (1248 * C14 * C18 * C7 * ((C12 / ((C12 - 1) * C11 * (C13 + 460))) * (
                        (y / C7) ** (2 / C12) - (y / C7) ** ((C12 + 1) / C12))) ** (0.5)) - C10

        y0 = C7 - 1.0
        ans2 = fsolve(lambda y: g(y), y0)
        C25 = ans2[0]
        # C25 = C21/(1248*C14*C18*((C12/((C12-1)*C11*(C13+460)))*((C7/C20)**(2/C12)-(C7/C20)**((C12+1)/C12)))**(0.5))

        C26 = (1 + C22) / 2 * C24 + (1 - C22) / 2 * C25

        if C22 == 1:
            flowtype = ' Sonic Flow'
        else:
            flowtype = ' Subsonic Flow'
        self.up.lineEdit_1.setAlignment(QtCore.Qt.AlignCenter)
        self.up.lineEdit_1.setText(str(C18) + ' sq. inches')
        self.up.lineEdit_2.setAlignment(QtCore.Qt.AlignCenter)
        self.up.lineEdit_2.setText(str(C19))
        self.up.lineEdit_3.setAlignment(QtCore.Qt.AlignCenter)
        self.up.lineEdit_3.setText(str(round(Decimal(C20), 3)) + ' psia')
        self.up.lineEdit_4.setAlignment(QtCore.Qt.AlignCenter)
        self.up.lineEdit_4.setText(str(round(Decimal(C21), 3)) + ' Mscf/day')
        self.up.lineEdit_6.setAlignment(QtCore.Qt.AlignCenter)
        self.up.lineEdit_6.setText(str(flowtype))
        self.up.lineEdit_5.setAlignment(QtCore.Qt.AlignCenter)
        self.up.lineEdit_5.setText(str(round(Decimal(C24), 3)) + ' psia')
        self.up.lineEdit_5.setAlignment(QtCore.Qt.AlignCenter)
        self.up.lineEdit_7.setAlignment(QtCore.Qt.AlignCenter)
        self.up.lineEdit_7.setText(str(round(Decimal(C25), 3)) + ' psia')
        self.up.lineEdit_8.setAlignment(QtCore.Qt.AlignCenter)
        self.up.lineEdit_8.setText(str(round(Decimal(C26), 3)) + ' psia')

        self.screen22.show()

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
        self.Background_label.setPixmap(QtGui.QPixmap("u1.jpg"))
        self.Background_label.setScaledContents(True)
        self.Background_label.setWordWrap(True)
        self.Background_label.setObjectName("Background_label")
        self.Topic_label = QtWidgets.QLabel(Downstream_Screen)
        self.Topic_label.setGeometry(QtCore.QRect(10, -10, 681, 91))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(21)
        font.setBold(True)
        font.setWeight(75)
        self.Topic_label.setFont(font)
        self.Topic_label.setObjectName("Topic_label")
        self.input_label1 = QtWidgets.QLabel(Downstream_Screen)
        self.input_label1.setGeometry(QtCore.QRect(89, 100, 211, 35))
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.input_label1.setFont(font)
        self.input_label1.setObjectName("input_label1")
        self.input_label2 = QtWidgets.QLabel(Downstream_Screen)
        self.input_label2.setGeometry(QtCore.QRect(75, 133, 201, 35))
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.input_label2.setFont(font)
        self.input_label2.setObjectName("input_label2")
        self.input_label5 = QtWidgets.QLabel(Downstream_Screen)
        self.input_label5.setGeometry(QtCore.QRect(25, 199, 251, 35))
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.input_label5.setFont(font)
        self.input_label5.setObjectName("input_label5")
        self.input_label4 = QtWidgets.QLabel(Downstream_Screen)
        self.input_label4.setGeometry(QtCore.QRect(35, 232, 241, 35))
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.input_label4.setFont(font)
        self.input_label4.setObjectName("input_label4")
        self.input_label6 = QtWidgets.QLabel(Downstream_Screen)
        self.input_label6.setGeometry(QtCore.QRect(85, 265, 191, 35))
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.input_label6.setFont(font)
        self.input_label6.setObjectName("input_label6")
        self.input_label7 = QtWidgets.QLabel(Downstream_Screen)
        self.input_label7.setGeometry(QtCore.QRect(40, 298, 250, 35))
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.input_label7.setFont(font)
        self.input_label7.setObjectName("input_label7")
        self.input_label3 = QtWidgets.QLabel(Downstream_Screen)
        self.input_label3.setGeometry(QtCore.QRect(105, 166, 171, 35))
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.input_label3.setFont(font)
        self.input_label3.setObjectName("input_label3")
        self.input_label8 = QtWidgets.QLabel(Downstream_Screen)
        self.input_label8.setGeometry(QtCore.QRect(40, 331, 231, 35))
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.input_label8.setFont(font)
        self.input_label8.setObjectName("input_label8")
        self.lineEdit_1 = QtWidgets.QLineEdit(Downstream_Screen)
        self.lineEdit_1.setGeometry(QtCore.QRect(285, 105, 150, 25))
        self.lineEdit_1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lineEdit_1.setInputMask("")
        self.lineEdit_1.setText("")
        self.lineEdit_1.setFrame(True)
        self.lineEdit_1.setObjectName("lineEdit_1")
        self.lineEdit_1.returnPressed.connect(self._screen23)
        self.lineEdit_2 = QtWidgets.QLineEdit(Downstream_Screen)
        self.lineEdit_2.setGeometry(QtCore.QRect(285, 138, 150, 25))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.returnPressed.connect(self._screen23)
        self.lineEdit_3 = QtWidgets.QLineEdit(Downstream_Screen)
        self.lineEdit_3.setGeometry(QtCore.QRect(285, 170, 150, 25))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_3.returnPressed.connect(self._screen23)
        self.lineEdit_4 = QtWidgets.QLineEdit(Downstream_Screen)
        self.lineEdit_4.setGeometry(QtCore.QRect(285, 202, 150, 25))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_4.returnPressed.connect(self._screen23)
        self.lineEdit_6 = QtWidgets.QLineEdit(Downstream_Screen)
        self.lineEdit_6.setGeometry(QtCore.QRect(285, 234, 150, 25))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_6.returnPressed.connect(self._screen23)
        self.lineEdit_5 = QtWidgets.QLineEdit(Downstream_Screen)
        self.lineEdit_5.setGeometry(QtCore.QRect(285, 268, 150, 25))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_5.returnPressed.connect(self._screen23)
        self.lineEdit_8 = QtWidgets.QLineEdit(Downstream_Screen)
        self.lineEdit_8.setGeometry(QtCore.QRect(285, 301, 150, 25))
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.lineEdit_8.returnPressed.connect(self._screen23)
        self.lineEdit_7 = QtWidgets.QLineEdit(Downstream_Screen)
        self.lineEdit_7.setGeometry(QtCore.QRect(285, 335, 150, 25))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.lineEdit_7.returnPressed.connect(self._screen23)
        self.calc_Button = QtWidgets.QPushButton(Downstream_Screen)
        self.calc_Button.setGeometry(QtCore.QRect(500, 210, 151, 51))
        font = QtGui.QFont()
        font.setFamily("Script MT Bold")
        font.setPointSize(22)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.calc_Button.setFont(font)
        self.calc_Button.setObjectName("calc_Button")
        self.calc_Button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.calc_Button.clicked.connect(self._screen23)

        self.retranslateUi(Downstream_Screen)
        QtCore.QMetaObject.connectSlotsByName(Downstream_Screen)

    def retranslateUi(self, Downstream_Screen):
        _translate = QtCore.QCoreApplication.translate
        Downstream_Screen.setWindowTitle(_translate("Upstream_Screen", "Choke Pressure Estimator - Downstream"))
        self.Topic_label.setText(
            _translate("Upstream_Screen", "Calculating Downstream Pressure at choke for dry gases"))
        self.input_label1.setText(_translate("Upstream_Screen", "Upstream Pressure (psi) :"))
        self.input_label2.setText(_translate("Upstream_Screen", "  Choke Size (1/64 inches) :"))
        self.input_label5.setText(_translate("Upstream_Screen", " Gas Production Rate (Mscf/day) :"))
        self.input_label4.setText(_translate("Upstream_Screen", "  Gas Specific Gravity (1 for air) :"))
        self.input_label6.setText(_translate("Upstream_Screen", " Gas Specific Heat Ratio :"))
        self.input_label7.setText(_translate("Upstream_Screen", "Downstream Temperature (°F) :"))
        self.input_label3.setText(_translate("Upstream_Screen", "  Flowline ID (inches) :"))
        self.input_label8.setText(_translate("Upstream_Screen", "  Choke Discharge Coefficient :"))
        self.lineEdit_1.setPlaceholderText(_translate("Upstream_Screen", "                Enter value"))
        self.lineEdit_2.setPlaceholderText(_translate("Upstream_Screen", "                Enter value"))
        self.lineEdit_3.setPlaceholderText(_translate("Upstream_Screen", "                Enter value"))
        self.lineEdit_4.setPlaceholderText(_translate("Upstream_Screen", "                Enter value"))
        self.lineEdit_6.setPlaceholderText(_translate("Upstream_Screen", "                Enter value"))
        self.lineEdit_5.setPlaceholderText(_translate("Upstream_Screen", "                Enter value"))
        self.lineEdit_8.setPlaceholderText(_translate("Upstream_Screen", "                Enter value"))
        self.lineEdit_7.setPlaceholderText(_translate("Upstream_Screen", "                Enter value"))
        self.calc_Button.setText(_translate("Upstream_Screen", "Calculate!"))



if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Downstream_Screen = QtWidgets.QWidget()
    ui = Ui_Downstream_Screen()
    ui.setupUi(Downstream_Screen)
    Downstream_Screen.show()
    sys.exit(app.exec_())
