import sys
import matplotlib
matplotlib.use('Qt5Agg')
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure

import numpy as np

# FigureCanvasQTAgg是matplotlib中定义的pyqt绘图组件
class PlotWidget(FigureCanvasQTAgg):

    def __init__(self, width=4, height=3, dpi=100):
        """widget to show matplotlib plotted 2d figure"""
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axis = fig.add_subplot(1, 1, 1)
        self.xdata = None
        self.ydata = None

        # 将matplotlib Figure 加载到FigureCanvasQTAgg
        super().__init__(fig)

    def update_plot(self, xdata, ydata):
        """
        plot on the widget
        
        Args:
            xdata: array for x axis
            ydata: array for y axis
        """
        self.axis.cla()  # Clear the canvas.
        self.axis.plot(xdata, ydata)
        # Trigger the canvas to update and redraw.
        self.draw()



if __name__ == '__main__':
    # enable dpi scale
    QApplication.setHighDpiScaleFactorRoundingPolicy(
        Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)

    app = QApplication(sys.argv)
    x = np.linspace(0, 2*np.pi, 100)
    y = np.sin(x)
    w = PlotWidget()
    w.show()
    w.update_plot(x, y)
    app.exec_()
        