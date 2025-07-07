import sys

from PyQt5.QtWidgets import QApplication, QWidget, QLabel,QPushButton, QVBoxLayout, QHBoxLayout

from PyQt5.QtCore import QTime, QTimer, Qt

from PyQt5.QtGui import QFont, QFontDatabase


class Stopwatch(QWidget):
    def __init__(self):
        super().__init__()
        self.time = QTime(0, 0 ,0 ,0)
        self.label = QLabel( "00 : 00 : 00.00", self)
        self.start_button = QPushButton("Start", self)
        self.stop_button = QPushButton("Stop", self)
        self.reset_button = QPushButton("Reset", self)
        self.timer = QTimer(self)
        self.initUI()



    def initUI(self):
        self.setWindowTitle("Stop Watch")
        self.resize(600 , 300 )
       
        
        

        vbox = QVBoxLayout()

        vbox.addWidget(self.label)
        vbox.addWidget(self.start_button)
        vbox.addWidget(self.stop_button)
        vbox.addWidget(self.reset_button)

        self.setLayout(vbox)
        self.label.setAlignment(Qt.AlignCenter)

        hbox = QHBoxLayout()

        
        hbox.addWidget(self.start_button)
        hbox.addWidget(self.stop_button)
        hbox.addWidget(self.reset_button)

        vbox.addLayout(hbox)


        self.setStyleSheet("QPushButton,QLabel{ padding: 20px;font-weight:italic; font-family:calibry; } QPushButton{ font-size: 50px; padding: 20px; } QLabel{font-size: 120px; background-color: rgb(167, 195, 255); color: rgb(252, 65, 255); border-radius: 20px;}")

        self.start_button.clicked.connect(self.start)
        self.stop_button.clicked.connect(self.stop)
        self.reset_button.clicked.connect(self.reset)
        self.timer.timeout.connect(self.update_display)



    def start(self):
        self.timer.start(10)
    
    def stop(self):
        self.timer.stop()
    
    def reset(self):
        self.timer.stop()
        self.time = QTime(0, 0 ,0 ,0)
        self.label.setText(self.format_time(self.time))


    def format_time(self, time):
        hour = time.hour()
        minute = time.minute()
        second = time.second()
        milisec = time.msec() //10

        return f"{hour:02}:{minute:02}:{second:02}:{milisec:02}"



    def update_display(self):
        self.time = self.time.addMSecs(10)
        self.label.setText(self.format_time(self.time))










    



if __name__ == "__main__":
    app = QApplication(sys.argv)
    stopwatch= Stopwatch()
    stopwatch.show()
    sys.exit(app.exec_())
