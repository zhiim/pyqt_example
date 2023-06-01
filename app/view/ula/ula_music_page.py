from PyQt5.QtWidgets import QVBoxLayout, QWidget, QHBoxLayout
from qfluentwidgets import PushButton, LineEdit
from components.para_widget import ParaWidget
from components.plot_widget import PlotWidget
from common.data.ula_music_data import ULAMusicData

class ULAMUSIC(QWidget):
    def __init__(self):
        super().__init__()

        self.ulaMusicData = ULAMusicData()  # 页面数据

        self.vbox = QVBoxLayout(self)  # 垂直布局
        self.hboxInVbox = QHBoxLayout(self)  # 最下方
        self.vboxForBtn = QVBoxLayout(self)
        self.arrayPara = ParaWidget('阵列参数')
        self.signalPara = ParaWidget('信号参数')
        self.plotwidget = PlotWidget(width=5, height=3)
        self.btn = PushButton('运行')

        self.arrayPara.addItem(text_label='阵元数（个）', 
                               text_input=str(self.ulaMusicData.M))
        self.arrayPara.addItem(text_label='阵元间距（倍波长）', 
                               text_input=str(self.ulaMusicData.dd), 
                               label_length=150)

        self.signalPara.addItem(text_label='信噪比（dB）', 
                                text_input=str(self.ulaMusicData.snr))
        self.signalPara.addItem(text_label='快拍数', 
                                text_input=str(self.ulaMusicData.K))
        self.signalPara.addItem(text_label='入射角（度）', 
                                text_input=str(self.ulaMusicData.theta))

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

        self.btn.clicked.connect(self.plot)  # 运行按钮与绘图绑定

    def plot(self):

        # 使用输入框的内容更新数据
        self.ulaMusicData.updataValue(M=self.arrayPara.btns['阵元数（个）'].text(), 
                                      dd=self.arrayPara.btns['阵元间距（倍波长）'].text(), 
                                      snr=self.signalPara.btns['信噪比（dB）'].text(), 
                                      K=self.signalPara.btns['快拍数'].text(), 
                                      theta=self.signalPara.btns['入射角（度）'].text())

        # # 执行matlab函数得到输出
        # self.ulaMusicData.getMusicData()

        self.ulaMusicData.getDataTest()

        # 绘图
        self.plotwidget.update_plot(self.ulaMusicData.xdata, 
                                    self.ulaMusicData.ydata)
