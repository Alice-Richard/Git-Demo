import numpy as np
import matplotlib.pyplot as plt

# 生成连续信号：指数信号
t = np.linspace(0, 5, 1000)  # 时间从0到5，1000个点
continuous_signal = np.exp(-t)  # 指数衰减信号

# 生成离散信号：锯齿信号
n = np.arange(0, 20)  # 离散时间从0到19
discrete_signal = np.mod(n, 10)  # 周期为5的锯齿信号

# 绘制连续信号
plt.figure(figsize=(12, 6))

plt.subplot(2, 1, 1)
plt.plot(t, continuous_signal, label='Continuous Signal: Exponential Decay', color='blue')
plt.title('Continuous Exponential Signal')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.legend()
plt.grid(True)

# 绘制离散信号
plt.subplot(2, 1, 2)
plt.stem(n, discrete_signal, label='Discrete Signal: Sawtooth', linefmt='red', markerfmt='ro', basefmt=" ")
plt.title('Discrete Sawtooth Signal')
plt.xlabel('Sample')
plt.ylabel('Amplitude')
plt.legend()
plt.grid(True)

# 显示图形
plt.tight_layout()
plt.show()