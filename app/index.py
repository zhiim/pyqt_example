import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication
from view.main_windows import Window

# 设置UI可以缩放
QApplication.setHighDpiScaleFactorRoundingPolicy(
    Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)

# 创建QT Application
app = QApplication(sys.argv)
app.setAttribute(Qt.AA_DontCreateNativeWidgetSiblings)

# 创建窗口
w = Window()
w.show()

app.exec_()