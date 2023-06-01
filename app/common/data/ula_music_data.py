import matlab.engine
import numpy as np

class ULAMusicData():

    # 定义初始化数据
    def __init__(self) -> None:

        # 阵列参数的默认值
        self.M = 8 # 阵元数
        self.dd = 0.5  # 阵元间距

        # 信号参数的默认值
        self.snr = 10  # 信噪比
        self.K = 300  # 快拍数
        self.theta = 30  # 入射角度
        

        self.xdata = []  # 绘图使用的x轴值
        self.ydata = []  # 绘图使用的y轴值

    def updataValue(self, M, dd, snr, K, theta):
        """更新数据"""
        self.M = int(M)
        self.dd = float(dd)
        self.snr = int(snr)
        self.K = int(K)
        self.theta = float(theta)

    def getMusicDataMatlab(self):
        """执行matlab脚本得到绘图需要的数据"""
        eng = matlab.engine.start_matlab()
        eng.addpath("common\scripts")  # 将matlab脚本添加到路径
        (self.xdata, self.ydata) = eng.music_ula(self.M, 
                                                 self.dd, 
                                                 self.snr, 
                                                 self.K, 
                                                 self.theta, 
                                                 nargout=2)
        eng.quit()

    def getDataTest(self):
        self.xdata = np.linspace(0, 2*np.pi, self.K)
        self.ydata = np.sin(self.xdata)
        