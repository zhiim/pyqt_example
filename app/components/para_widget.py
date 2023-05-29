import typing
from PyQt5 import QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QFrame, QStackedWidget, QVBoxLayout, QLabel

from qfluentwidgets import FlowLayout
from qfluentwidgets import FluentIcon as FIF
from qframelesswindow import FramelessWindow, StandardTitleBar

from input_widget import InputWidget

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

        self.vbox.addWidget(self.title)
        self.vbox.addLayout(self.flowbox, 1)

    def addItem(self):
        """
        在ParaWidget内添加自定以组件InputWidget(带标签的输入框)
        """


