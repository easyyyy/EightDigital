from PyQt5.QtCore import QTimer, QThread, pyqtSignal
import threading
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QMessageBox

import ui
import eightDigital2
import time





class UiExt(ui.Ui_MainWindow):
    num=0

    def __init__(self):
        self.srcLayout = ""
        self.targetLayout = ""
        self.code = None

        self.tempS = 1
        self.isRun = True
        # l = ['541203786', '501243786', '510243786', '513240786', '513204786', '503214786']
        self.l = ['541203786', '501243786', '510243786', '513240786', '513204786', '503214786', '053214786', '253014786', '253104786', '203154786', '230154786', '234150786', '234105786', '234185706', '234185760', '234180765', '230184765', '203184765', '023184765', '123084765', '123804765']

        self.tempLenth = len(self.l)

    def func(self):
        self.timer=QTimer()
        self.timer.timeout.connect(self.pixLoad)
        self.pushButton.clicked.connect(lambda :self.getSrcLayout())
        self.pushButton.clicked.connect(lambda :self.getTargetLayout())
        # self.label_pix1.picture()
        self.pushButton_2.clicked.connect(lambda : self.start())
        self.pushButton.clicked.connect(lambda :self.cal())
        self.pushButton_3.clicked.connect(lambda: self.stop())
        # self.pixLoad(['541203786', '501243786', '510243786', '513240786', '513204786', '503214786', '053214786', '253014786', '253104786', '203154786', '230154786', '234150786', '234105786', '234185706', '234185760', '234180765', '230184765', '203184765', '023184765', '123084765', '123804765'])

    def cal(self):
        if self.srcLayout == "" or self.targetLayout == "":
            QMessageBox.information(self.centralwidget, "错误", "请检查输入是否正确", QMessageBox.Cancel)
            return
        self.code,self.l = self.eightDigit()
        if self.code == -1:
            QMessageBox.information(self.centralwidget, "错误", "无法到达该布局",QMessageBox.Cancel)
            return
        if self.l == "":
            QMessageBox.information(self.centralwidget, "错误", "请检查输入是否正确",QMessageBox.Cancel)
            return

        self.label_result.setText("0/{}".format(len(self.l)))


    def start(self):
        self.timer.start(1000)


    def stop(self):
        self.timer.stop()

    def pixLoad(self):

        # index=0
        # for i in self.l:
        #     # print(self.l)
        #     for inx, val in enumerate(i):
        #
        #         eval('self.label_pix{}.setPixmap(QPixmap("pix/{}.PNG"))'.format(inx,val))
        #         eval('self.label_pix{}.setScaledContents(True)'.format(inx))
        #         eval('self.label_pix{}.repaint()'.format(inx))
        #     index = index + 1
        #     self.label_result.setText("{}/{}".format(index,len(self.l)))
        #     QApplication.processEvents()
        #     time.sleep(0.5)


        if self.l[0] is not None:


            for inx, val in enumerate(self.l[0]):

                eval('self.label_pix{}.setPixmap(QPixmap("pix/{}.PNG"))'.format(inx,val))
                eval('self.label_pix{}.setScaledContents(True)'.format(inx))
                eval('self.label_pix{}.repaint()'.format(inx))


            self.label_result.setText("{}/{}".format(self.tempS,self.tempLenth))

            self.tempS = self.tempS + 1
            # QApplication.processEvents()
            time.sleep(0.5)
            self.l.pop(0)




    def getSrcLayout(self):
        srcLayout = []

        srcLayout.append(self.lineEdit_1.text())
        srcLayout.append(self.lineEdit_2.text())
        srcLayout.append(self.lineEdit_3.text())
        srcLayout.append(self.lineEdit_4.text())
        srcLayout.append(self.lineEdit_5.text())
        srcLayout.append(self.lineEdit_6.text())
        srcLayout.append(self.lineEdit_7.text())
        srcLayout.append(self.lineEdit_8.text())
        srcLayout.append(self.lineEdit_9.text())

        srcLayout = ''.join(srcLayout)
        self.srcLayout = srcLayout

        # if self.srcLayout == "":
        #     QMessageBox.information(self.centralwidget, "错误", "请检查输入是否正确",QMessageBox.Cancel)
        #     return



    def getTargetLayout(self):

        targetLayout = []

        targetLayout.append(self.lineEdit_target_1.text())
        targetLayout.append(self.lineEdit_target_2.text())
        targetLayout.append(self.lineEdit_target_3.text())
        targetLayout.append(self.lineEdit_target_4.text())
        targetLayout.append(self.lineEdit_target_5.text())
        targetLayout.append(self.lineEdit_target_6.text())
        targetLayout.append(self.lineEdit_target_7.text())
        targetLayout.append(self.lineEdit_target_8.text())
        targetLayout.append(self.lineEdit_target_9.text())

        targetLayout = ''.join(targetLayout)
        self.targetLayout = targetLayout

        # if self.targetLayout == "":
        #     QMessageBox.information(self.centralwidget, "错误", "请检查输入是否正确",QMessageBox.Cancel)
        #     return

    def eightDigit(self):
        code, l = eightDigital2.solvePuzzle_span(self.srcLayout, self.targetLayout)
        return code,l