import numpy as np
import random
import math

# 退火算法
# 定义目标函数（Rastrigin 函数）
def rastrigin(x, y):
    return 20 + x ** 2 + y ** 2 - 10 * (math.cos(2 * math.pi * x) + math.cos(2 * math.pi * y))


# 模拟退火算法
def simulated_annealing(max_iter=1000, initial_temp=100, cooling_rate=0.99):
    # 初始化解（随机选择 x, y）
    x, y = random.uniform(-5, 5), random.uniform(-5, 5)
    current_energy = rastrigin(x, y)

    # 设定初始温度
    temperature = initial_temp

    for i in range(max_iter):
        # 生成新解（在当前解附近小范围扰动）
        new_x = x + random.uniform(-0.5, 0.5)
        new_y = y + random.uniform(-0.5, 0.5)
        new_energy = rastrigin(new_x, new_y)

        # 计算能量变化
        delta_energy = new_energy - current_energy

        # 选择是否接受新解
        if delta_energy < 0 or random.random() < math.exp(-delta_energy / temperature):
            x, y, current_energy = new_x, new_y, new_energy

        # 降温
        temperature *= cooling_rate

        # 记录进度
        if i % 100 == 0:
            print(f"Iter {i}: x = {x:.4f}, y = {y:.4f}, f(x,y) = {current_energy:.4f}, T = {temperature:.4f}")

    return x, y, current_energy


# 运行模拟退火算法
best_x, best_y, best_value = simulated_annealing()

print(f"\n最优解: x = {best_x:.4f}, y = {best_y:.4f}, f(x,y) = {best_value:.4f}")
