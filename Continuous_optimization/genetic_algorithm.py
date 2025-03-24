import numpy as np

# 初始化种群
# 𝑓(𝑥)=−(𝑥−5)^2+10
def init_population(size, x_range):
    return np.random.uniform(x_range[0], x_range[1], size)

# 适应度函数
def fitness(x):
    return -(x - 5) ** 2 + 10

# 选择操作
def select(pop, fitness_scores):
    idx = np.argsort(fitness_scores)[-2:]  # 选择适应度最高的两个个体
    return pop[idx]

# 交叉操作
def crossover(parents):
    return (parents[0] + parents[1]) / 2

# 变异操作
def mutate(child, x_range):
    return child + np.random.uniform(-0.5, 0.5)

# 遗传算法
def genetic_algorithm(iterations=100):
    pop = init_population(10, (-10, 10))
    for _ in range(iterations):
        fitness_scores = fitness(pop)
        parents = select(pop, fitness_scores)
        child = crossover(parents)
        child = mutate(child, (-10, 10))
        pop = np.append(pop, child)  # 加入新个体
    return max(pop, key=fitness)

# 运行遗传算法
best_x = genetic_algorithm()
print(f"最优解：x = {best_x:.2f}, f(x) = {fitness(best_x):.2f}")