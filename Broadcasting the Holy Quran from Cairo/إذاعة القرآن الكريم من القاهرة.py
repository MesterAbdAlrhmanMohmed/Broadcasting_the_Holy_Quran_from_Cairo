from PyQt6 import QtWidgets as qt
from PyQt6 import QtGui as qt1
from PyQt6 import QtCore as qt2
from PyQt6.QtMultimedia import QMediaPlayer,QAudioOutput
class main (qt.QMainWindow):
    def __init__(self):
        super().__init__()
        self.showFullScreen
        self.setWindowTitle("إذاعة القرآن الكريم من القاهرة")
        self.m=QMediaPlayer()
        self.w=QAudioOutput()
        self.تشغيل=qt.QPushButton("تشغيل")
        self.تشغيل.setDefault(True)
        self.تشغيل.clicked.connect(self.play)
        self.حول=qt.QPushButton("حول البرنامج")
        self.حول.setDefault(True)
        self.حول.clicked.connect(self.ab)
        l=qt.QVBoxLayout()        
        l.addWidget(self.تشغيل)
        l.addWidget(self.حول)
        w=qt.QWidget()
        w.setLayout(l)
        self.setCentralWidget(w)        
        self.m.setAudioOutput(self.w)
        self.m.setSource(qt2.QUrl("https://stream.radiojar.com/8s5u5tpdtwzuv"))
    def play(self):
        if self.تشغيل.text() == "تشغيل":
            try:
                self.تشغيل.setText("إيقاف")
                self.m.play()
            except:
                qt.QMessageBox.warning(self, "تنبيه", "يرجى التأكد من الإتصال بالإنترنت")
        else:
            self.تشغيل.setText("تشغيل")
            self.m.stop()            
    def ab(self):
        qt.QMessageBox.information(self,"تنبيه","تم تطوير هذا البرنامج للإستماع الى إذاعة القرآن الكريم من القاهرة عبر الإنترنت, تحياتي مطور البرنامج, عبد الرحمن محمد")
app=qt.QApplication([])
app.setStyle('fusion')
w=main()
w.show()
app.exec()