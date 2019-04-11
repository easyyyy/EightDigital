import sys
import time
import threading

import cv2
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QDialog, QApplication

from winForm import Ui_Dialog


class EightDigital(QDialog,QThread):

    sig_out = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.working = True
        self.index = 0

        self.g_dict_layouts = {}
        self.g_dict_shifts = {0: [1, 3], 1: [0, 2, 4], 2: [1, 5],
                         3: [0, 4, 6], 4: [1, 3, 5, 7], 5: [2, 4, 8],
                         6: [3, 7], 7: [4, 6, 8], 8: [5, 7]}
        self.retCode = -1
        self.lst_steps = []

        self.srcLayout = ""
        self.destLayout = ""
        self.currentLayout = ""

        self.ui.calculateButton.clicked.connect(self.calculateFunc)
        self.ui.startButton.clicked.connect(self.startFunc)
        self.ui.stopButton.clicked.connect(self.stopFunc)

    def swap_chr(self, a, i, j):
        if i > j:
            i, j = j, i
        b = a[:i] + a[j] + a[i + 1:j] + a[i] + a[j + 1:]
        return b

    def solvePuzzle_span(self, srcLayout, destLayout):
        self.g_dict_layouts[srcLayout] = -1

        stack_layouts = []
        stack_layouts.append(srcLayout)
        i = 0
        try:
            bFound = False
            while len(stack_layouts) > 0:
                curLayout = stack_layouts[i]
                if curLayout == destLayout:
                    bFound = True
                    break
                i = i + 1
                # 寻找0 的位置。
                ind_slide = curLayout.index("0")
                lst_shifts = self.g_dict_shifts[ind_slide]
                for nShift in lst_shifts:
                    newLayout = self.swap_chr(curLayout, nShift, ind_slide)

                    if self.g_dict_layouts.get(newLayout) == None:
                        self.g_dict_layouts[newLayout] = curLayout
                        stack_layouts.append(newLayout)
        except:
            print("布局不可达！")
            bFound = False

        if bFound:
            self.lst_steps.append(curLayout)
            while self.g_dict_layouts[curLayout] != -1:
                curLayout = self.g_dict_layouts[curLayout]
                self.lst_steps.append(curLayout)
            self.lst_steps.reverse()
            return 0, self.lst_steps
        else:
            return -1, None

    def calculateFunc(self):
        # 获取源布局
        self.srcLayout = self.ui.src0LineEdit.text() + self.ui.src1LineEdit.text() + self.ui.src2LineEdit.text() + \
                         self.ui.src3LineEdit.text() + self.ui.src4LineEdit.text() + self.ui.src5LineEdit.text() + \
                         self.ui.src6LineEdit.text() + self.ui.src7LineEdit.text() + self.ui.src8LineEdit.text()
        # 获取目标布局
        self.destLayout = self.ui.dest0LineEdit.text() + self.ui.dest1LineEdit.text() + self.ui.dest2LineEdit.text() + \
                          self.ui.dest3LineEdit.text() + self.ui.dest4LineEdit.text() + self.ui.dest5LineEdit.text() + \
                          self.ui.dest6LineEdit.text() + self.ui.dest7LineEdit.text() + self.ui.dest8LineEdit.text()

        self.retCode, self.lst_steps = self.solvePuzzle_span(self.srcLayout, self.destLayout)

        img = cv2.imread("eight.jpg")
        img[1:76, 1:76] = cv2.imread(self.lst_steps[0][0]+".jpg")
        img[1:76, 76:151] = cv2.imread(self.lst_steps[0][1]+".jpg")
        img[1:76, 151:226] = cv2.imread(self.lst_steps[0][2]+".jpg")
        img[76:151, 1:76] = cv2.imread(self.lst_steps[0][3]+".jpg")
        img[76:151, 76:151] = cv2.imread(self.lst_steps[0][4]+".jpg")
        img[76:151, 151:226] = cv2.imread(self.lst_steps[0][5]+".jpg")
        img[151:226, 1:76] = cv2.imread(self.lst_steps[0][6]+".jpg")
        img[151:226, 76:151] = cv2.imread(self.lst_steps[0][7]+".jpg")
        img[151:226, 151:226] = cv2.imread(self.lst_steps[0][8]+".jpg")

        # 颜色空间的转换
        img_rgb = cv2.cvtColor(src=img, code=cv2.COLOR_BGR2RGB)
        height, width, channel = img_rgb.shape
        print(height)
        print(width)
        bytesPerLine = 3 * width
        img = QImage(img_rgb, width, height, bytesPerLine, QImage.Format_RGB888)
        img = QPixmap.fromImage(img)

        self.ui.imgLabel.setPixmap(img)

        self.ui.label.setText("1 / " + str(len(self.lst_steps)-1))



    def startFunc(self):
        for i in range(len(self.lst_steps)):
            img = cv2.imread("eight.jpg")
            img[1:76, 1:76] = cv2.imread(self.lst_steps[i][0] + ".jpg")
            img[1:76, 76:151] = cv2.imread(self.lst_steps[i][1] + ".jpg")
            img[1:76, 151:226] = cv2.imread(self.lst_steps[i][2] + ".jpg")
            img[76:151, 1:76] = cv2.imread(self.lst_steps[i][3] + ".jpg")
            img[76:151, 76:151] = cv2.imread(self.lst_steps[i][4] + ".jpg")
            img[76:151, 151:226] = cv2.imread(self.lst_steps[i][5] + ".jpg")
            img[151:226, 1:76] = cv2.imread(self.lst_steps[i][6] + ".jpg")
            img[151:226, 76:151] = cv2.imread(self.lst_steps[i][7] + ".jpg")
            img[151:226, 151:226] = cv2.imread(self.lst_steps[i][8] + ".jpg")

            # 颜色空间的转换
            img_rgb = cv2.cvtColor(src=img, code=cv2.COLOR_BGR2RGB)
            height, width, channel = img_rgb.shape
            print(height)
            print(width)
            bytesPerLine = 3 * width
            img = QImage(img_rgb, width, height, bytesPerLine, QImage.Format_RGB888)
            img = QPixmap.fromImage(img)

            self.ui.imgLabel.setPixmap(img)
            self.ui.label.setText(str(i) + " / " + str(len(self.lst_steps)-1))

    def stopFunc(self):

        pass

    def showDestLayout(self):
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    eightDigital = EightDigital()
    eightDigital.show()
    sys.exit(app.exec_())



