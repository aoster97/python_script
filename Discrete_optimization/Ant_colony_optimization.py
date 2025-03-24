import numpy as np

# 参数设置
num_cities = 5  # 城市数量
num_ants = 10  # 蚂蚁数量
num_iterations = 100  # 迭代次数
alpha = 1  # 信息素重要性因子
beta = 2  # 启发式因子
evaporation = 0.5  # 信息素挥发率
Q = 100  # 信息素更新常数

# 随机生成城市坐标
np.random.seed(42)
cities = np.random.rand(num_cities, 2) * 100

# 计算城市间距离矩阵
distances = np.linalg.norm(cities[:, np.newaxis] - cities, axis=2)

# 初始化信息素矩阵
pheromones = np.ones((num_cities, num_cities))

# 计算启发式信息（城市间的吸引力）
heuristic = 1 / (distances + np.eye(num_cities))  # 避免除零错误

def select_next_city(ant, unvisited, pheromones, heuristic, alpha, beta):
    """ 选择下一座城市 """
    current_city = ant[-1]
    pheromone_levels = pheromones[current_city, unvisited] ** alpha
    attractiveness = heuristic[current_city, unvisited] ** beta
    probabilities = pheromone_levels * attractiveness
    probabilities /= probabilities.sum()
    return np.random.choice(unvisited, p=probabilities)

def ant_colony_optimization():
    global pheromones
    best_path, best_path_length = None, float('inf')

    for iteration in range(num_iterations):
        paths = []
        path_lengths = []

        # 每只蚂蚁寻找路径
        for _ in range(num_ants):
            ant_path = [np.random.randint(num_cities)]
            unvisited = set(range(num_cities)) - {ant_path[0]}

            while unvisited:
                next_city = select_next_city(ant_path, list(unvisited), pheromones, heuristic, alpha, beta)
                ant_path.append(next_city)
                unvisited.remove(next_city)

            ant_path.append(ant_path[0])  # 回到起点
            path_length = sum(distances[ant_path[i], ant_path[i+1]] for i in range(num_cities))

            paths.append(ant_path)
            path_lengths.append(path_length)

            # 更新最优解
            if path_length < best_path_length:
                best_path, best_path_length = ant_path, path_length

        # 信息素更新（挥发 + 新增）
        pheromones *= (1 - evaporation)
        for path, length in zip(paths, path_lengths):
            for i in range(num_cities):
                pheromones[path[i], path[i+1]] += Q / length

        if iteration % 10 == 0:
            print(f"Iteration {iteration}: Best Path Length = {best_path_length:.2f}")

    return best_path, best_path_length

# 运行蚁群算法
best_path, best_length = ant_colony_optimization()
print(f"\n最优路径: {best_path}\n路径长度: {best_length:.2f}")
