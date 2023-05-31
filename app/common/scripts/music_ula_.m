function xdata, ydata = music_ula(M, dd, snr, K, theta)
%music_ula - Description
%
% Syntax: xdata, ydata = music_ula(M, N, snr, K)
%
% M: 
% dd:
% snr:
% K:
% theta:
    
lambda = 1;
d = 0:dd:(M-1)*dd;                                                          %构建阵列坐标
A = exp(1j.*2*pi*d.'*sind(theta)/lambda);                                   %构建阵列流形，即信号来向

S = randn(N,K) + 1j.*randn(N,K);                                            %构建不相关信号
X = A*S;                                                                    %对信号来向进行仿真
X1 = awgn(X,snr,'measured');                                                %加入噪声，产生小特征值

Rxx = X1*X1'/K;                                                             %构建协方差矩阵
[EV,D] = eig(Rxx);                                                          %拿到特向量EV + 特征值D  新版本matlab已经从小到大排序好了

%   循环搜索特征向量正交的时候
idx = 1;
[SP,SP_inv] = deal(zeros(181,1));
scale = -90:90;
for angle_degree = scale
    a =exp(1j.*2*pi*d*sind(angle_degree)/lambda).';     %构建信号导向矢量，用共轭转至全部加负号
    En = EV(:,1:end-N);                                 %用前面的几个小特征值的特征向量
    SP(idx) = (a'*En)*(En'*a);                          %利用前面讲的正交来判断结果
    SP_inv(idx) = 1/abs((a'*En)*(En'*a));               %用倒数翻转一下 变成峰值

    idx = idx + 1;
end
SP_db = db(SP);                                         %转换为dB
SP_inv_db = db(abs(SP_inv));                            %转换为dB

xdata = scale
ydata = SP_inv_db
