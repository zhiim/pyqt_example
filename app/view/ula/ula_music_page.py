from PyQt5.QtWidgets import QVBoxLayout, QWidget, QHBoxLayout
from qfluentwidgets import PushButton
from components.para_widget import ParaWidget
from components.plot_widget import PlotWidget

class ULAMUSIC(QWidget):
    def __init__(self):
        super().__init__()

        self.vbox = QVBoxLayout(self)  # 垂直布局
        self.hboxInVbox = QHBoxLayout(self)  # 最下方
        self.vboxForBtn = QVBoxLayout(self)
        self.arrayPara = ParaWidget('阵列参数')
        self.signalPara = ParaWidget('信号参数')
        self.plotwidget = PlotWidget(width=5, height=3)
        self.btn = PushButton('运行')

        self.arrayPara.addItem(text_label='阵元数（个）', text_input="8")
        self.arrayPara.addItem(text_label='阵元间距（倍波长）', text_input="0.5", label_length=150)

        self.signalPara.addItem(text_label='信噪比（dB）', text_input='10')
        self.signalPara.addItem(text_label='载波频率（MHz）', text_input='0.8')
        self.signalPara.addItem(text_label='入射角（度）', text_input='30')

        self.vboxForBtn.addWidget(self.btn)
        self.vboxForBtn.addStretch(1)
        
        self.hboxInVbox.addWidget(self.plotwidget)
        self.hboxInVbox.addLayout(self.vboxForBtn)
        self.hboxInVbox.addStretch(1)
        
        self.vbox.addWidget(self.arrayPara)
        self.vbox.addWidget(self.signalPara)
        self.vbox.addLayout(self.hboxInVbox, 1)

        self.setStyleSheet('''
            background-color: rgb(249, 249, 249);
        ''')
