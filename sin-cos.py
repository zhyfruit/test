import numpy as np
import pylab as pl
import matplotlib.font_manager as fm

myfont = fm.FontProperties(fname=r'C:\Windows\Fonts\Arial.ttf')
#设置字体
t = np.arange(0.0,2.0*np.pi,0.01)
#自变量取值范围#
s = np.sin(t)
 #计算正弦函数值
z = np.cos(t)
#计算正弦函数值
pl.plot(t, s, label='sin')
pl.plot(t, z, label='cos')
pl.xlabel('x', fontproperties='Arial', fontsize=24)
#设置x标签
pl.ylabel('y', fontproperties='Arial', fontsize=24)
pl.title('sin-cos', fontproperties='Arial', fontsize=32)
#图形标题
pl.legend(prop=myfont)
#设置图例
pl.show()
