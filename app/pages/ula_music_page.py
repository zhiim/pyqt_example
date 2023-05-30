import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QFrame, QVBoxLayout, QLabel, QWidget
from qfluentwidgets import PushButton

from ..components.para_widget import ParaWidget
from ..components.plot_widget import PlotWidget

class ULAMUSIC(QWidget):
    def __init__(self):
        super().__init__()

        self.vbox = QVBoxLayout(self)
        self.hboxInVbox = QVBoxLayout(self)
        self.arrayPara = ParaWidget('阵列参数')
        self.signalPara = ParaWidget('信号参数')
        self.plot = PlotWidget()
        self.btn = PushButton('运行')

        self.arrayPara.addItem(text_label='阵元数（个）', text_input="8")
        self.arrayPara.addItem(text_label='阵元间距（倍波长）', text_input="0.5", label_length=150)

        self.signalPara.addItem(text_label='信噪比（dB）', text_input='10')
        self.signalPara.addItem(text_label='载波频率（MHz）', text_input='0.8')
        self.signalPara.addItem(text_label='入射角（度）', text_input='30')
        
        self.vbox.addWidget(self.arrayPara)
        self.vbox.addWidget(self.signalPara)
        self.vbox.addLayout(self.hboxInVbox, 1)

        self.hboxInVbox.addWidget(self.plot)
        self.hboxInVbox.addWidget(self.btn)

if __name__ == '__main__':
    # enable dpi scale
    QApplication.setHighDpiScaleFactorRoundingPolicy(
        Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)

    app = QApplication(sys.argv)
    w = ULAMUSIC()
    w.show()
    app.exec_()
