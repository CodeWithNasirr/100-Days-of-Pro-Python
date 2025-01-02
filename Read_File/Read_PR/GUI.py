import os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QMessageBox
import shutil
import platform

class Ui_MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.setObjectName("MainWindow")
        self.setEnabled(True)
        self.resize(554, 451)
        self.setMaximumSize(QtCore.QSize(554, 451))
        self.setStyleSheet("""
                QWidget#centralwidget {
                    background: qlineargradient(spread:pad, x1:0.136409, y1:0.131, x2:1, y2:1, stop:0 rgba(36, 110, 233, 255), stop:1 rgba(255, 255, 255, 255));
                }""")
        # Central Widget Open
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        # Drag And Drop Area.....
        self.Drag_Drop = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.Drag_Drop.setGeometry(QtCore.QRect(110, 20, 351, 300))
        self.Drag_Drop.setObjectName("Drag_Drop")
        self.Drag_Drop.setPlaceholderText("Drag Your File Here")
        self.Drag_Drop.setStyleSheet("background: rgb(176, 196, 222);font:25 italic 16pt Calibri;border-radius:20px")
        # Connect drag-and-drop events
        self.Drag_Drop.setAcceptDrops(True)
        self.Drag_Drop.dragEnterEvent = self.dragEnterEvent
        self.Drag_Drop.dropEvent = self.dropEvent

        # Central Widget End
        self.setCentralWidget(self.centralwidget)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow","MainWindow"))

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        for url in event.mimeData().urls():
            file_path = str(url.toLocalFile())
            self.Copy_Bin_File(file_path)
            path=os.path.basename(file_path)
            self.Drag_Drop.setPlainText(path)
            self.show_message("Dropped file", f"Dropped file: {path}")

    
    def Copy_Bin_File(self,Drop_File):
        target_directory=r'C:\aa'
        Not_match='old.bin'
        if not os.path.exists(target_directory):
            os.makedirs(target_directory)
        else:
            print('File Already Exists ')
        
        absolute_input_path = os.path.abspath(Drop_File)
        print(absolute_input_path)
        Drop_file_name=os.path.basename(Drop_File)
        print(Drop_file_name)
        with open(absolute_input_path,'rb') as f:
            a=f.read()
        target_hex=b'\x5A\xA5\xF0'
        offset=a.find(target_hex)
        if offset != -1:
            if offset ==0x10:
                print(True)
                next_three_bytes=a[0x10:0x13]
                if next_three_bytes == target_hex:
                    self.show_message("Success",f"Hex value {target_hex.hex()} matches")
                    target_path=os.path.join(target_directory,os.path.basename(Drop_File))
                    shutil.copy(absolute_input_path,target_path)
                else:
                    self.show_message("Success",f"Hex value {target_hex} not match Its a {Not_match}")
                    target_path=os.path.join(target_directory,Not_match)
                    shutil.copy(absolute_input_path,target_path)
            else:
                print(False)
                self.show_message("Error",f"offset value {offset:#x}  not match to Offset{hex(0x10)} ")
                self.show_message("Error",f"Its a {Not_match} File ")
                target_path=os.path.join(target_directory,Not_match)
                shutil.copy(absolute_input_path,target_path)
        else:
            self.show_message("Error","Hex Not Found")
            return 
        if os.path.exists(target_path):
            self.open_explorer(os.path.dirname(target_path))
        else:
            self.show_message("Error", "File copy Failed")

    def open_explorer(self, target_directory):
        system_platform = platform.system()
        try:
            if system_platform == "Windows":
                os.startfile(target_directory)
            elif system_platform == "Linux":
                os.system(f'xdg-open "{target_directory}"')
            else:
                self.show_message("Error", "Unsupported Operating System")
        except Exception as e:
            self.show_message("Error", f"Failed to open explorer: {str(e)}")

    def show_message(self, title, text, icon=QMessageBox.Information):
        msg_box = QMessageBox()
        msg_box.setIcon(icon)
        msg_box.setWindowTitle(title)
        msg_box.setText(text)
        msg_box.setStyleSheet("background:white;color:black")
        msg_box.exec_()


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    ui = Ui_MainWindow()
    ui.show()
    sys.exit(app.exec_())
