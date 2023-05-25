# coding:utf-8
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QLabel

from qfluentwidgets import LineEdit


class Demo(QWidget):

    def __init__(self, text):
        super().__init__()
        self.hBoxLayout = QHBoxLayout(self)  # 新建HBox容器
        self.lineEdit = LineEdit(self)  # 新建输入框
        self.label = QLabel(text, self)  # 新建文本标签

        self.resize(280, 35)  # 设置窗口大小
        self.hBoxLayout.setAlignment(Qt.AlignCenter)

        # 将lineEdit和label加入容器
        self.hBoxLayout.addWidget(self.label, 0, Qt.AlignCenter)
        self.hBoxLayout.addWidget(self.lineEdit, 0, Qt.AlignCenter)

        self.lineEdit.setFixedSize(200, 33)
        self.lineEdit.setClearButtonEnabled(True)
        self.lineEdit.setPlaceholderText('Search icon')
        
        self.label.setFixedSize(50, 33)


if __name__ == '__main__':
    # enable dpi scale
    QApplication.setHighDpiScaleFactorRoundingPolicy(
        Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)

    app = QApplication(sys.argv)
    w = Demo('snr')
    w.show()
    app.exec_()