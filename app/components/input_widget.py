# coding:utf-8
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QLabel

from qfluentwidgets import LineEdit

class InputWidget(QWidget):

    def __init__(self, text_label="Input", text_input="Input please",
                  label_length=120, input_length=100):
        """
        a widget consists of a label and an input box

        Args:
            text_label: text to show in label
            text_input: text to show in input box
            label_length: length of label
            input_length: length of input box
        """

        super().__init__()
        self.hBoxLayout = QHBoxLayout(self)  # 新建HBox容器
        self.lineEdit = LineEdit(self)  # 新建输入框
        self.label = QLabel(text_label, self)  # 新建文本标签

        self.label.setStyleSheet('''font: 15px 'Segoe UI';
                                    background: rgb(242,242,242);
                                    border-radius: 5px;
                                    ''')
        self.label.setAlignment(Qt.AlignCenter)  # 文字居中

        self.hBoxLayout.setAlignment(Qt.AlignCenter)

        # 将lineEdit和label加入容器
        self.hBoxLayout.addWidget(self.label, 0, Qt.AlignCenter)
        self.hBoxLayout.addWidget(self.lineEdit, 0, Qt.AlignCenter)

        self.lineEdit.setFixedSize(input_length, 33)
        self.lineEdit.setClearButtonEnabled(True)
        self.lineEdit.setText(text_input)
        
        self.label.setFixedSize(label_length, 33)


if __name__ == '__main__':
    # enable dpi scale
    QApplication.setHighDpiScaleFactorRoundingPolicy(
        Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)

    app = QApplication(sys.argv)
    w = InputWidget('snr')
    w.show()
    app.exec_()
