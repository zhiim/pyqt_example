import matlab.engine

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

    def getMusicData(self):
        eng = matlab.engine.start_matlab()
        eng.addpath("common\scripts")  # 将matlab脚本添加到路径
        (self.xdata, self.ydata) = eng.music_ula(self.M, 
                                                 self.dd, 
                                                 self.snr, 
                                                 self.K, 
                                                 self.theta, 
                                                 nargout=2)
        eng.quit()

    def updataValue(self, M, dd, snr, K, theta):
        self.M = float(M)
        self.dd = float(dd)
        self.snr = float(snr)
        self.K = float(K)
        self.theta = float(theta)
        