import ui
import eightDigital2


class UiExt(ui.Ui_MainWindow):

    srcLayout = ""
    targetLayout = ""

    def func(self):
        self.pushButton.clicked.connect(lambda :self.getSrcLayout())
        self.pushButton.clicked.connect(lambda :self.getTargetLayout())
        self.pushButton.clicked.connect(lambda :self.eightDigit())
        self.graphicsView


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

    def eightDigit(self):
        code, l = eightDigital2.solvePuzzle_span(self.srcLayout, self.targetLayout)
        print(l)