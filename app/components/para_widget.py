import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QFrame, QVBoxLayout, QLabel, QHBoxLayout

from qfluentwidgets import FlowLayout

from components.input_widget import InputWidget

class ParaWidget(QFrame):
    def __init__(self, title):
        """
        用于参数设置的组件，包含几个参数输入框

        Args:
            title: 参数组件的标题
        """

        super().__init__()

        self.vbox = QVBoxLayout(self)
        self.flowbox = FlowLayout()  # PyQt-Fluent-Widgets定义的流

        self.title = QLabel(title, self)
        self.title.setStyleSheet('''
            font: 15px 'Segoe UI';
            font-weight: bold;
        ''')

        self.flowbox.setVerticalSpacing(5)
        self.flowbox.setHorizontalSpacing(10)

        self.vbox.addWidget(self.title, 1)
        self.vbox.addLayout(self.flowbox, 1)

        self.vbox.setAlignment(Qt.AlignVCenter)
        self.vbox.addStretch(1)

        self.btns = {}  # 用来保存添加的所有输入框，保存为dict键值对的形式

    def addItem(self, text_label, text_input, label_length=120, input_length=100):
        """
        在ParaWidget内添加自定以组件InputWidget(带标签的输入框)

        Args:
            text_label: text to show in label
            text_input: text to show in input box
            label_length: length of label
            input_length: length of input box
        """

        # 新建自定义输入框组件InputWidget
        input = InputWidget(text_label, text_input, label_length, input_length)
        # 向self.btns中添加键值对
        self.btns[text_label] = input
        self.flowbox.addWidget(input)


if __name__ == '__main__':
    # enable dpi scale
    QApplication.setHighDpiScaleFactorRoundingPolicy(
        Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)

    app = QApplication(sys.argv)
    w = ParaWidget('阵列参数')
    w.show()
    w.addItem(text_label='阵元数（个）', text_input="8")
    w.addItem(text_label='阵元间距（倍波长）', text_input="0.5", label_length=150)
    app.exec_()
