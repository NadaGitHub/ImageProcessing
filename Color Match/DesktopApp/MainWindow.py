import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
from ColorDetector import ColorDetector
from PyQt5.QtWidgets import QMessageBox



class Ui_MainWindow(object):



    def openImageWindow(self):
        self.ui = Ui_ImageWindow()
        self.ui.setupUi_ImageWindow(ImageWindow)
        if ImageWindow.isHidden():
            ImageWindow.show()
            


    def Image_PushBtn_Clicked(self):
        if not MainWindow.isHidden():
            MainWindow.hide()
        self.openImageWindow()


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(538, 222)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(170, 40, 221, 16))
        font = QtGui.QFont()
        font.setFamily("Baskerville Old Face")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton_image = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_image.setGeometry(QtCore.QRect(216, 110, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Baskerville Old Face")
        font.setPointSize(14)
        self.pushButton_image.setFont(font)
        self.pushButton_image.setObjectName("pushButton_image")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 538, 21))#21
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        
        self.pushButton_image.clicked.connect(self.Image_PushBtn_Clicked)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Color Match"))
        #self.label.setText(_translate("MainWindow", "Please Select Your Source"))
        self.pushButton_image.setText(_translate("MainWindow", "Start"))

   



class Ui_ImageWindow(object):

    def __init__(self):
        self.black_flag = False
        self.white_flag = False
        self.red_flag = False
        self.lime_flag = False
        self.blue_flag = False
        self.yellow_flag = False
        self.cyan_flag = False
        self.magenda_flag = False
        self.silver_flag = False
        self.gray_flag = False
        self.maroon_flag = False
        self.olive_flag = False
        self.green_flag = False
        self.purple_flag = False
        self.teal_flag = False
        self.navy_flag = False
        self.skyblue_flag = False
        self.all_flag = False
        #################### Matching ####################
        self.Match_flag = False
        ###############################################################



    def setupUi_ImageWindow(self, ImageWindow):
        ImageWindow.setObjectName("ImageWindow")
        ImageWindow.resize(582, 286)
        self.centralwidget = QtWidgets.QWidget(ImageWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(190, 180, 201, 16))
        font = QtGui.QFont()
        font.setFamily("Baskerville Old Face")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        font = QtGui.QFont()
        font.setFamily("Baskerville Old Face")
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.pushButton_Browse = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Browse.setGeometry(QtCore.QRect(240, 210, 75, 23))
        self.pushButton_Browse.setObjectName("pushButton_Browse")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(120, 40, 341, 16))
        font = QtGui.QFont()
        font.setFamily("Baskerville Old Face")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.checkBox_Black = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_Black.setGeometry(QtCore.QRect(50, 70, 70, 17))
        self.checkBox_Black.setObjectName("checkBox_Black")
        self.checkBox_White = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_White.setGeometry(QtCore.QRect(140, 70, 70, 17))
        self.checkBox_White.setObjectName("checkBox_White")
        self.checkBox_Red = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_Red.setGeometry(QtCore.QRect(230, 70, 70, 17))
        self.checkBox_Red.setObjectName("checkBox_Red")
        self.checkBox_Lime = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_Lime.setGeometry(QtCore.QRect(310, 70, 70, 17))
        self.checkBox_Lime.setObjectName("checkBox_Lime")
        self.checkBox_Blue = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_Blue.setGeometry(QtCore.QRect(390, 70, 70, 17))
        self.checkBox_Blue.setObjectName("checkBox_Blue")
        self.checkBox_Yellow = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_Yellow.setGeometry(QtCore.QRect(470, 70, 70, 17))
        self.checkBox_Yellow.setObjectName("checkBox_Yellow")
        self.checkBox_Cyan = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_Cyan.setGeometry(QtCore.QRect(50, 100, 70, 17))
        self.checkBox_Cyan.setObjectName("checkBox_Cyan")
        self.checkBox_Magenda = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_Magenda.setGeometry(QtCore.QRect(140, 100, 70, 17))
        self.checkBox_Magenda.setObjectName("checkBox_Magenda")
        self.checkBox_Sliver = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_Sliver.setGeometry(QtCore.QRect(230, 100, 70, 17))
        self.checkBox_Sliver.setObjectName("checkBox_Sliver")
        self.checkBox_Gray = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_Gray.setGeometry(QtCore.QRect(310, 100, 70, 17))
        self.checkBox_Gray.setObjectName("checkBox_Gray")
        self.checkBox_Maroon = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_Maroon.setGeometry(QtCore.QRect(390, 100, 70, 17))
        self.checkBox_Maroon.setObjectName("checkBox_Maroon")
        self.checkBox_Olive = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_Olive.setGeometry(QtCore.QRect(470, 100, 70, 17))
        self.checkBox_Olive.setObjectName("checkBox_Olive")
        self.checkBox_Green = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_Green.setGeometry(QtCore.QRect(50, 130, 70, 17))
        self.checkBox_Green.setObjectName("checkBox_Green")
        self.checkBox_Purple = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_Purple.setGeometry(QtCore.QRect(140, 130, 70, 17))
        self.checkBox_Purple.setObjectName("checkBox_Purple")
        self.checkBox_Navy = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_Navy.setGeometry(QtCore.QRect(310, 130, 70, 17))
        self.checkBox_Navy.setObjectName("checkBox_Navy")
        self.checkBox_Teal = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_Teal.setGeometry(QtCore.QRect(230, 130, 70, 17))
        self.checkBox_Teal.setObjectName("checkBox_Teal")
        self.checkBox_Skyblue = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_Skyblue.setGeometry(QtCore.QRect(390, 130, 70, 17))
        self.checkBox_Skyblue.setObjectName("checkBox_Skyblue")
        self.checkBox_All = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_All.setGeometry(QtCore.QRect(470, 130, 70, 17))
        self.checkBox_All.setObjectName("checkBox_All")

        #################### Matching ####################
        self.checkBox_Match = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_Match.setGeometry(QtCore.QRect(250, 160, 70, 17))
        self.checkBox_Match.setObjectName("checkBox_Match")
        ##################################################################

        ImageWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ImageWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 582, 21))
        self.menubar.setObjectName("menubar")
        ImageWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ImageWindow)
        self.statusbar.setObjectName("statusbar")
        ImageWindow.setStatusBar(self.statusbar)
        
        self.pushButton_Browse.clicked.connect(self.Browse_onClick)
        self.checkBox_Black.toggled.connect(self.checkbox_toggled)
        self.checkBox_White.toggled.connect(self.checkbox_toggled)
        self.checkBox_Red.toggled.connect(self.checkbox_toggled)
        self.checkBox_Lime.toggled.connect(self.checkbox_toggled)
        self.checkBox_Blue.toggled.connect(self.checkbox_toggled)
        self.checkBox_Yellow.toggled.connect(self.checkbox_toggled)
        self.checkBox_Cyan.toggled.connect(self.checkbox_toggled)
        self.checkBox_Magenda.toggled.connect(self.checkbox_toggled)
        self.checkBox_Sliver.toggled.connect(self.checkbox_toggled)
        self.checkBox_Gray.toggled.connect(self.checkbox_toggled)
        self.checkBox_Maroon.toggled.connect(self.checkbox_toggled)
        self.checkBox_Olive.toggled.connect(self.checkbox_toggled)
        self.checkBox_Green.toggled.connect(self.checkbox_toggled)
        self.checkBox_Purple.toggled.connect(self.checkbox_toggled)
        self.checkBox_Teal.toggled.connect(self.checkbox_toggled)
        self.checkBox_Navy.toggled.connect(self.checkbox_toggled)
        self.checkBox_Skyblue.toggled.connect(self.checkbox_toggled)
        self.checkBox_All.toggled.connect(self.checkbox_toggled)

        ###################### Matching ####################
        self.checkBox_Match.toggled.connect(self.checkbox_toggled)
        #################################################################
        self.retranslateUi_ImageWindow(ImageWindow)
        QtCore.QMetaObject.connectSlotsByName(ImageWindow)

    def retranslateUi_ImageWindow(self, ImageWindow):
        _translate = QtCore.QCoreApplication.translate
        ImageWindow.setWindowTitle(_translate("ImageWindow", "Color Detector"))
        self.label.setText(_translate("ImageWindow", "Please browse your file"))
        
        self.pushButton_Browse.setText(_translate("ImageWindow", "Browse"))
        self.label_2.setText(_translate("ImageWindow", "Please Select the colors you want to detect"))
        self.checkBox_Black.setText(_translate("ImageWindow", "Black"))
        self.checkBox_White.setText(_translate("ImageWindow", "White"))
        self.checkBox_Red.setText(_translate("ImageWindow", "Red"))
        self.checkBox_Lime.setText(_translate("ImageWindow", "Lime"))
        self.checkBox_Blue.setText(_translate("ImageWindow", "Blue"))
        self.checkBox_Yellow.setText(_translate("ImageWindow", "Yellow"))
        self.checkBox_Cyan.setText(_translate("ImageWindow", "Cyan"))
        self.checkBox_Magenda.setText(_translate("ImageWindow", "Magenda"))
        self.checkBox_Sliver.setText(_translate("ImageWindow", "Silver"))
        self.checkBox_Gray.setText(_translate("ImageWindow", "Gray"))
        self.checkBox_Maroon.setText(_translate("ImageWindow", "Maroon"))
        self.checkBox_Olive.setText(_translate("ImageWindow", "Olive"))
        self.checkBox_Green.setText(_translate("ImageWindow", "Green"))
        self.checkBox_Purple.setText(_translate("ImageWindow", "Purple"))
        self.checkBox_Navy.setText(_translate("ImageWindow", "Navy"))
        self.checkBox_Teal.setText(_translate("ImageWindow", "Teal"))
        self.checkBox_Skyblue.setText(_translate("ImageWindow", "SkyBlue"))
        self.checkBox_All.setText(_translate("ImageWindow", "All of Them"))
        #################### Matching ####################
        self.checkBox_Match.setText(_translate("ImageWindow", "Match/Not"))
        ############################################################### 

    def checkbox_toggled(self):

        if self.checkBox_All.isChecked():
            self.all_flag = True

        else:
            self.all_flag = False

            if self.checkBox_Black.isChecked():
                self.black_flag = True
               
            else:
                self.black_flag = False

            if self.checkBox_White.isChecked():
                self.white_flag = True
            else:
                self.white_flag = False

            if self.checkBox_Red.isChecked():
                self.red_flag = True
            else:
                self.red_flag = False

            if self.checkBox_Lime.isChecked():
                self.lime_flag = True
            else:
                self.lime_flag = False

            if self.checkBox_Blue.isChecked():
                self.blue_flag = True
            else:
                self.blue_flag = False

            if self.checkBox_Yellow.isChecked():
                self.yellow_flag = True
            else:
                self.yellow_flag = False

            if self.checkBox_Cyan.isChecked():
                self.cyan_flag = True
            else:
                self.cyan_flag = False

            if self.checkBox_Magenda.isChecked():
                self.magenda_flag = True
            else:
                self.magenda_flag = False

            if self.checkBox_Sliver.isChecked():
                self.silver_flag = True
            else:
                self.silver_flag = False

            if self.checkBox_Gray.isChecked():
                self.gray_flag = True
            else:
                self.gray_flag = False

            if self.checkBox_Maroon.isChecked():
                self.maroon_flag = True
            else:
                self.maroon_flag = False

            if self.checkBox_Olive.isChecked():
                self.olive_flag = True
            else:
                self.olive_flag = False

            if self.checkBox_Green.isChecked():
                self.green_flag = True
            else:
                self.green_flag = False

            if self.checkBox_Purple.isChecked():
                self.purple_flag = True
            else:
                self.purple_flag = False

            if self.checkBox_Teal.isChecked():
                self.teal_flag = True
            else:
                self.teal_flag = False

            if self.checkBox_Navy.isChecked():
                self.navy_flag = True
            else:
                self.navy_flag = False

            if self.checkBox_Skyblue.isChecked():
                self.skyblue_flag = True
            else:
                self.skyblue_flag = False

            ###################### Matching ####################
            if self.checkBox_Match.isChecked():
                self.Match_flag = True
              
            else:
                self.Match_flag = False
            ############################################################### 


    def imageDetection_onClick(self,imagePath):
        detector = ColorDetector()
        detector.ImageDetection(imagePath, Black=self.black_flag, White=self.white_flag, Red=self.red_flag,
                                Lime=self.lime_flag, Blue=self.blue_flag,Yellow=self.yellow_flag, Cyan=self.cyan_flag,
                                Magenda=self.magenda_flag, Silver=self.silver_flag, Gray=self.gray_flag,
                                Maroon=self.maroon_flag, Olive=self.olive_flag, Green=self.green_flag,
                                Purple=self.purple_flag, Teal=self.teal_flag, Navy=self.navy_flag,
                                Skyblue=self.skyblue_flag, All=self.all_flag, Match=self.Match_flag)

    ####################### Matching ####################
        if self.checkBox_Black.isChecked():
                self.black_flag = True
                msg = QMessageBox()
                msg.setWindowTitle("                Suggestion                ")
                msg.setText("                Black matchs with : (White , Green , Yellow , Red)                ")
                            
                x = msg.exec_()
        if self.checkBox_White.isChecked():
                self.white_flag = True
                msg = QMessageBox()
                msg.setWindowTitle("                Suggestion                ")
                msg.setText("                White matchs with : (Black , Red , Blue)            ")
                            
                x = msg.exec_()
        if self.checkBox_Red.isChecked():
                self.red_flag = True
                msg = QMessageBox()
                msg.setWindowTitle("                Suggestion                ")
                msg.setText("                Red matchs with : (Black , Yellow , Blue , Green , Cyan , Silver , Olive , Purple)            ")
                            
                x = msg.exec_()
        if self.checkBox_Lime.isChecked():
                self.lime_flag = True
                msg = QMessageBox()
                msg.setWindowTitle("                Suggestion                ")
                msg.setText("                Lime matchs with : (Yellow , Green)            ")
                            
                x = msg.exec_()
        if self.checkBox_Blue.isChecked():
                self.blue_flag = True
                msg = QMessageBox()
                msg.setWindowTitle("                Suggestion                ")
                msg.setText("                Blue matchs with : (White , Red , Green , Gray , Magenda , Silver , Purple)            ")
                            
                x = msg.exec_()
        if self.checkBox_Yellow.isChecked():
                self.yellow_flag = True
                msg = QMessageBox()
                msg.setWindowTitle("                Suggestion                ")
                msg.setText("                Yellow matchs with : (Lime , Red , Black , Gray , Cyan , Green)            ")
                            
                x = msg.exec_()
        if self.checkBox_Cyan.isChecked():
                self.cyan_flag = True
                msg = QMessageBox()
                msg.setWindowTitle("                Suggestion                ")
                msg.setText("                Cyan matchs with : (Yellow , Red , White , Gray)            ")
                            
                x = msg.exec_()
        if self.checkBox_Magenda.isChecked():
                self.magenda_flag = True
                msg = QMessageBox()
                msg.setWindowTitle("                Suggestion                ")
                msg.setText("                Magenda matchs with : (Green , Blue , Purple)            ")
                            
                x = msg.exec_()
        if self.checkBox_Sliver.isChecked():
                self.sliver_flag = True
                msg = QMessageBox()
                msg.setWindowTitle("                Suggestion                ")
                msg.setText("                Sliver matchs with : (Green , Blue , Purple , Red)            ")
                            
                x = msg.exec_()
        if self.checkBox_Gray.isChecked():
                self.gray_flag = True
                msg = QMessageBox()
                msg.setWindowTitle("                Suggestion                ")
                msg.setText("                Gray matchs with : (Yellow , Blue , Cyan , Maroon , Olive , Skyblue)            ")
                            
                x = msg.exec_()
        if self.checkBox_Maroon.isChecked():
                self.maroon_flag = True
                msg = QMessageBox()
                msg.setWindowTitle("                Suggestion                ")
                msg.setText("                Maroon matchs with : (White , Gray , Teal , Olive)            ")
                            
                x = msg.exec_()
        if self.checkBox_Olive.isChecked():
                self.olive_flag = True
                msg = QMessageBox()
                msg.setWindowTitle("                Suggestion                ")
                msg.setText("                Olive matchs with : (Red , Gray , Maroon , Purple, Navy)            ")
                            
                x = msg.exec_()
        if self.checkBox_Green.isChecked():
                self.green_flag = True
                msg = QMessageBox()
                msg.setWindowTitle("                Suggestion                ")
                msg.setText("                Green matchs with : (Black, Lime , Blue , Yellow , Magenda , Silver, Skyblue)            ")
                            
                x = msg.exec_()
        if self.checkBox_Purple.isChecked():
                self.purple_flag = True
                msg = QMessageBox()
                msg.setWindowTitle("                Suggestion                ")
                msg.setText("                Purple matchs with : (Black , Lime , Blue , Yellow , Magenda , Silver)            ")
                            
                x = msg.exec_()
        if self.checkBox_Teal.isChecked():
                self.teal_flag = True
                msg = QMessageBox()
                msg.setWindowTitle("                Suggestion                ")
                msg.setText("                Teal matchs with : (Maroon , Navy)            ")
                            
                x = msg.exec_()
        if self.checkBox_Navy.isChecked():
                self.navy_flag = True
                msg = QMessageBox()
                msg.setWindowTitle("                Suggestion                ")
                msg.setText("                Navy matchs with : (Teal , Olive)            ")
                            
                x = msg.exec_()
        if self.checkBox_Skyblue.isChecked():
                self.skyblue_flag = True
                msg = QMessageBox()
                msg.setWindowTitle("                Suggestion                ")
                msg.setText("                Skyblue matchs with : (Black , Gray , Purple)            ")
                            
                x = msg.exec_()
            
    ###############################################################

    def Browse_onClick(self):
        app = QApplication(sys.argv)
        ex = FileDialog()
        fileName = ex.openFileNameDialog()
        self.imageDetection_onClick(fileName)
        

    def openMainWindow(self):
        self.ui = Ui_MainWindow()
        self.ui.setupUi(MainWindow)
        if MainWindow.isHidden():
            MainWindow.show()




class FileDialog(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'Image to detect its colors'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

    def openFileNameDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self, "Image to detect its colors", "",
                                                  "JPEG Files (*.JPG);;Portable Network Graphic file(PNG) (*.PNG)", options=options)
        if fileName:
            return fileName



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ImageWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())