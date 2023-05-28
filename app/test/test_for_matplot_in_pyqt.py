import sys
import matplotlib
matplotlib.use('Qt5Agg')

from PyQt5.QtWidgets import QWidget, QApplication

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
import numpy as np

# FigureCanvasQTAgg是matplotlib中定义的pyqt绘图组件
class MplCanvas(FigureCanvasQTAgg):

    def __init__(self, scalex, scaley, width=5, height=4, dpi=100):
        """
        widget to show matplotlib plotted 2d figure

        Args:
            scalex: array for x axis
            scaley: array for y axis
        """
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axis = fig.add_subplot(1, 1, 1)
        self.axis.plot(scalex, scaley)

        # 将matplotlib Figure 加载到FigureCanvasQTAgg
        super().__init__(fig)

app = QApplication(sys.argv)
x = np.linspace(0, 2*np.pi, 100)
y = np.sin(x) 
w = MplCanvas(x, y)
w.show()
app.exec_()