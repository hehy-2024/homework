import numpy as np
import math

# 本程序的单位制采用国际单位制
g = 9.8  # 重力加速度

def heightAndDistanceAndTime(h0, n):
    h = h0 * (0.5 ** n)
    d = h0  # 路程，初始路程为第一次高度
    for i in range(1, n + 1):
        d += 2 * h0 * (0.5 ** i)  # 上升和下降两部分的贡献
    t = math.sqrt(2 * h0 / g)  # 初始下落时间
    for i in range(1, n + 1):
        h_i = h0 * (0.5 ** i)  # 第 i 次反弹的高度
        t += 2 * math.sqrt(2 * h_i / g)  # 上升和下降两部分的贡献
    return h, d, t

h, d, t = heightAndDistanceAndTime(100, 10)
print("第十次反弹的高度",h, "第十次反弹所经过的距离",d, "第十次反弹运动的总时间",t,)