import math

# 本程序的单位制采用国际单位制
g = 9.8 # 重力加速度

def heightAndDistanceAndtime(h0, n):
    # 计算第n次反弹的高度
    h = h0 * (0.5 ** n)
    
    # 计算总路程
    d = h0  # 初始下落
    for i in range(1, n + 1):
        d += 2 * h0 * (0.5 ** i) # 上升和下降两部分的贡献
    
    # 计算总时间
    t = math.sqrt(2 * h0 / g) # 初始下落时间
    for i in range(1, n + 1):
        h_i = h0 * (0.5 ** i) # 第i次反弹的高度
        t += 2 * math.sqrt(2 * h_i / g) # 上升和下降两部分的贡献
    
    return h, d, t


# 计算第十次反弹的高度、距离和时间
h_10, d_10, t_10 = heightAndDistanceAndtime(100, 10)
print(f"第10次反弹的高度为{h_10}米，总路程为{d_10}米，总时间为{t_10}秒。")

# 任意n次
s = input("请输入两个数字，用空格分隔: ") 
h0, n = map(int, s.split()) # 将输入拆分为两部分并转换为整数
h,d,t = heightAndDistanceAndtime(h0, n)
print(f"第{n}次反弹的高度为{h}米，总路程为{d}米，总时间为{t}秒。")
