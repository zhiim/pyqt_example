from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QFrame, QStackedWidget, QHBoxLayout, QLabel

from qfluentwidgets import (NavigationInterface,NavigationItemPosition,
                            qrouter)
from qfluentwidgets import FluentIcon as FIF
from qframelesswindow import FramelessWindow, StandardTitleBar
from view.ula_interface import ULAInterface
from components.sample_widget import SampleWidget


class Window(FramelessWindow):

    def __init__(self):
        super().__init__()
        self.setTitleBar(StandardTitleBar(self))

        # 在Window容器内新建Horizontal Box（Box内的组件水平排布）
        self.hBoxLayout = QHBoxLayout(self)

        # 创建组件NavigationInterface，即导航栏
        self.navigationInterface = NavigationInterface(
            self, showMenuButton=True, showReturnButton=False)
        

        # 创建组件QStackedWidget，堆栈窗口，由多个不同窗口组成，但只显示其中一个
        # 实现通过NavigationInterface切换页面
        self.stackWidget = QStackedWidget(self)

        # 创建QstackedWidget中将要包含的Widgets
        self.ula_interface = ULAInterface()
        self.option2 = SampleWidget('Music Interface', self)
        self.option3 = SampleWidget('Video Interface', self)
        self.option4 = SampleWidget('Folder Interface', self)
        self.setting_interface = SampleWidget('Setting Interface', self)

        # initialize layout
        self.initLayout()

        # add items to navigation interface
        self.initNavigation()

        self.initWindow()

    def initLayout(self):
        self.hBoxLayout.setSpacing(0)
        self.hBoxLayout.setContentsMargins(0, self.titleBar.height(), 0, 0)
        
        # 将QStackedWidget和NavigationInterface添加到HBox容器中
        self.hBoxLayout.addWidget(self.navigationInterface)
        self.hBoxLayout.addWidget(self.stackWidget)

        self.hBoxLayout.setStretchFactor(self.stackWidget, 1)

    def initNavigation(self):
        self.addSubInterface(self.ula_interface, FIF.INFO, '均匀线阵')
        self.addSubInterface(self.option2, FIF.PIN, 'option2')
        self.addSubInterface(self.option3, FIF.SEARCH, 'option3')

        # 添加分隔线
        # self.navigationInterface.addSeparator()

        # add navigation items to scroll area
        self.addSubInterface(self.option4, FIF.QUESTION, 'option4')

        # add custom widget to bottom
        # self.navigationInterface.addWidget(
        #     routeKey='avatar',
        #     widget=AvatarWidget(),
        #     onClick=self.showMessageBox,
        #     position=NavigationItemPosition.BOTTOM
        # )

        self.addSubInterface(self.setting_interface, FIF.SETTING, 'Settings', NavigationItemPosition.BOTTOM)

        #!IMPORTANT: don't forget to set the default route key
        qrouter.setDefaultRouteKey(self.stackWidget, self.ula_interface.objectName())

        # set the maximum width
        self.navigationInterface.setExpandWidth(200)

        # 页面切换
        self.stackWidget.currentChanged.connect(self.onCurrentInterfaceChanged)
        # 初始时默认显示的页面
        self.navigationInterface.setCurrentItem(self.ula_interface.objectName())
        self.stackWidget.setCurrentIndex(0)

    def initWindow(self):
        self.resize(1080, 700)
        # 设置窗口logo
        self.setWindowIcon(QIcon('resource/logo.png'))
        # 设置窗口标题
        self.setWindowTitle('样例')
        self.titleBar.setAttribute(Qt.WA_StyledBackground)

        # 初始时使导航栏展开
        self.navigationInterface.panel.toggle()
        
        # 移动窗口到屏幕中央
        desktop = QApplication.desktop().availableGeometry()
        w, h = desktop.width(), desktop.height()
        self.move(w//2 - self.width()//2, h//2 - self.height()//2)

        # 启用css样式
        self.setQss()

    def addSubInterface(self, interface, icon, text: str, position=NavigationItemPosition.TOP):
        """ add sub interface """

        # QStackedWidget中添加Widget，在NavigationInterface中添加切换选项
        self.stackWidget.addWidget(interface)
        self.navigationInterface.addItem(
            routeKey=interface.objectName(),
            icon=icon,
            text=text,
            onClick=lambda: self.switchTo(interface),
            position=position,
            tooltip=text
        )

    def setQss(self):
        with open(f'resource/style.qss', encoding='utf-8') as f:
            self.setStyleSheet(f.read())

    def switchTo(self, widget):
        self.stackWidget.setCurrentWidget(widget)

    def onCurrentInterfaceChanged(self, index):
        widget = self.stackWidget.widget(index)
        # 在navigationInterface中选中对应的选项
        self.navigationInterface.setCurrentItem(widget.objectName())
        # 在stackWidget中切换到对应的页面
        qrouter.push(self.stackWidget, widget.objectName())
