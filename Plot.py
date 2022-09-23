# -*- coding: utf-8 -*-
"""
Created on Sat Jun 18 18:22:01 2022

@author: GIGABYTE
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.font_manager import FontProperties  # 步骤一


font = FontProperties(fname=r"C:/simsun.ttc", size=14)  
#(1)
plants_mass = pd.Series([33, 486.9,597.36, 64.219, 190000, 56800, 8683, 10247, 1.27],
                        index=['水星', '金星', '地球', '火星', '木星', '土星', '天王星', '海王星', '冥王星'],
                       dtype='float32')
plants_mass

#(2)
plants_mass = pd.Series([33, 486.9,597.36, 64.219, 190000, 56800, 8683, 10247, 1.27],
                        index=['水星', '金星', '地球', '火星', '木星', '土星', '天王星', '海王星', '冥王星'],
                       dtype='float32')
plants_distance2sun = pd.Series([0.5791, 1.08, 1.49, 2.27, 7.78, 14.29, 28.7, 45.04, 59.13],
                        index=['水星', '金星', '地球', '火星', '木星', '土星', '天王星', '海王星', '冥王星'],
                       dtype='float32')
plants = pd.DataFrame({'distance2sun':plants_distance2sun,'mass':plants_mass})
plants

#(3)
plants_mass.loc['地球':'海王星']

#(4)
plants.loc[plants.distance2sun<10][-2:]

#(5)
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['font.serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
subplt= plt.subplot(111, projection='polar')
subplt.set_title('九大行星距離太陽雷達圖', fontproperties=font)
distance2sun = np.log10(np.array([0.5791,1.08,1.49,2.27,7.78,14.29,28.70,45.04,59.13])*100)
theta=np.arange(0, 2*np.pi, 2*np.pi/9)
subplt.plot(theta,distance2sun,'.--')
subplt.fill(theta,distance2sun,alpha=0.2,color='r')
plt.savefig("C:/Users/GIGABYTE/Downloads/Matplotlib_gif/九大行星距離太陽雷達圖.png")